from user.models import UserModel


class UserRepo:
    def create_user(self, email: str, name: str, password: str):
        # 에러를 레포에서 발생시킴
        # service단은 레포의 기능 활용, 유효성 검사는 repo에서 하는게 좋을 것 같아서
        if self.is_exist(email):
            raise ConflictResource(detail="duplicate email")

        user = UserModel.objects.create(
           email=email, name=name, password=password
        )
        return user

    def is_exist(self, email):
        return UserModel.objects.filter(email=email).exists()

