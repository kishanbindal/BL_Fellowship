from .models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'email', 'password']


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['email', 'password']


class UserForgotPasswordSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['email']


class UploadImageSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['profile_image']


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk','username', 'email', 'profile_image']

# class UserGetPasswordSerializer(serializers.ModelSerializer):
#
#     class Meta:
#
#         model = User
#         fields = ['password', 'confirm_password']
