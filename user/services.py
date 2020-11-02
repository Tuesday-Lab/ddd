from django.db import transaction

from user.models import UserModel


# from user.repositories import UserRepo


class UserService:
    # def __init__(self):
    #     self.user_repo = UserRepo()

    @transaction.atomic
    def signup(self, email: str, name: str, password: str):
        # 심플한 레포일 때도 서비스 레이어에서 트랜잭션 관리하는게 좋을까?

        # user = self.user_repo.create_user(email, name, password)
        user = UserModel.objects.create_user(email, password, name)
        return user


service = UserService()
