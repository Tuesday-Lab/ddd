from rest_framework import routers, viewsets
from rest_framework.response import Response

from user.services import service as user_service
from ..users.parameter import SignupParameters
from ..users.schema import SignupSchema


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        # TODO: 이것도 pydantic으로??
        serializer = SignupParameters(data=request.data)
        serializer.is_valid(raise_exception=True)
        validate_data = serializer.validated_data

        new_user = user_service.signup(
            email=validate_data.get("email"),
            name=validate_data.get("name"),
            password=validate_data.get("password")
        )

        response = SignupSchema(new_user)
        return Response({"user": response.data})


router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename="users")
