from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from base.exceptions import ConflictResource


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Custom User 모델을 사용하다 보니 매니저를 활용할 수 밖에 없어서
# 레포 레이어 삭제..
# -> 매니저&모델 사용하는걸 레포레이어로 감쌀까 했으나
# 어떤건 매니저 어떤건 레포 등으로 분리될 것 같아 안나눔
class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, name: str):
        if self.is_exist(email):
            raise ConflictResource(detail="duplicate email")

        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def is_exist(self, email):
        return UserModel.objects.filter(email=email).exists()


class UserModel(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=20, null=False, unique=False)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = "user"
