from django.db import models


class User(models.Model):

    objects = None
    user_name = models.CharField(max_length=16, )
    user_email = models.EmailField(max_length=32, )
    user_password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)