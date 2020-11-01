from django.db import transaction

from base.exceptions import ConflictResource
from user.models import User


class UserService:
    @transaction.atomic
    def signup(self, email: str, name: str, password: str):
        # TODO:  트랜잭션 관리 + 로직 + 인프라까지 다 가져도 되는걸까?
        if self._is_exist(email):
            raise ConflictResource(detail="duplicate name")

        user = User.objects.create(
            email=email, name=name, password=password
        )
        return user

    def _is_exist(self, email):
        return User.objects.filter(email=email).exists()


service = UserService()
