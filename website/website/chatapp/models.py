from django.db import models


class User(models.Model):

    user_name = models.CharField(max_length=16, unique=True)
    user_email = models.EmailField(max_length=32, unique=True)
    user_password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)