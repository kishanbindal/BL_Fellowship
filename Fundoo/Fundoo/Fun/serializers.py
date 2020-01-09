from .models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['username', 'email', 'password', 'confirm_password']


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['email', 'password']


class UserForgotPasswordSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['email']


class UserGetPasswordSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['password', 'confirm_password']
