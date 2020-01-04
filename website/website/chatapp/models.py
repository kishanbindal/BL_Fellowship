from django.db import models


class User(models.Model):

    objects = None
    username = models.CharField(max_length=16, )
    email = models.EmailField(max_length=32, )
    password = models.CharField(max_length=16)
