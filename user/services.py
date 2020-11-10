from django.db import transaction

from user.models import UserModel


class UserService:
    @transaction.atomic
    def signup(self, email: str, name: str, password: str):
        user = UserModel.objects.create_user(email, password, name)
        return user


service = UserService()
