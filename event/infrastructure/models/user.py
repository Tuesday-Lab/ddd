from django.db import models

from event.infrastructure.models.base import TimestampMixin


# Todo CustomUser
class User(TimestampMixin):
    id = models.BigAutoField()
    email = models.EmailField()
    name = models.CharField()
    phone_number = models.CharField()

    # Todo 직군/직무, 학교, 소속회사
