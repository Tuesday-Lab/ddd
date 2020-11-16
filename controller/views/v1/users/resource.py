from rest_framework import routers, viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from user.services import service as user_service
from ..users.parameter import SignupParameters, SigninParameters
from ..users.schema import SignupSchema

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(viewsets.ViewSet):
    @action(
        methods=["POST"],
        detail=False,
    )
    def signup(self, request):
        # TODO: 이것도 pydantic으로??
        serializer = SignupParameters(data=request.data)
        serializer.is_valid(raise_exception=True)
        validate_data = serializer.validated_data

        new_user = user_service.signup(
            email=validate_data.get("email"),
            name=validate_data.get("name"),
            password=validate_data.get("password"),
        )

        response = SignupSchema(new_user)
        return Response({"user": response.data})

    @action(methods=["POST"], detail=False)
    def signin(self, request):
        serializer = SigninParameters(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"message": "is not valid body."}, status=status.HTTP_409_CONFLICT
            )

        validate_data = serializer.validated_data
        user = authenticate(
            email=validate_data.get("email"),
            password=validate_data.get("password"),
        )
        if not user:
            return Response(
                {"message": "not exist user"}, status=status.HTTP_400_BAD_REQUEST
            )

        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        update_last_login(None, user)

        return Response(
            {
                "token": jwt_token,
            }
        )


router = routers.DefaultRouter()
router.register(r"", UserViewSet, basename="users")
