from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username

#
# class UserProfile(models.Model):
#
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

