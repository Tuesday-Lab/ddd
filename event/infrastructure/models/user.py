from django.db import models


class User(models):
    id = models.BigAutoField()
    email = models.EmailField()
    name = models.CharField()
