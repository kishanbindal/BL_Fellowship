from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    confirm_password = models.CharField(max_length=16, )


    def __str__(self):
        return self.email
