from django.db import transaction

from user.models import UserModel


# from user.repositories import UserRepo


class UserService:
    # def __init__(self):
    #     self.user_repo = UserRepo()

    @transaction.atomic
    def signup(self, email: str, name: str, password: str):
        # user = self.user_repo.create_user(email, name, password)
        user = UserModel.objects.create_user(email, password, name)
        return user


service = UserService()
