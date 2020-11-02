from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class UserModel(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        max_length=20,
        null=False,
        unique=False
    )
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = 'user'

