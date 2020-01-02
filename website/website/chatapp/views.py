from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from django.views.decorators.csrf import ensure_csrf_cookie


class UserRegistration(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # send_mail(subject, from_email, to_list, fail_silently=True)
            subject = "Please click the link to activate your account"
            from_email = ''
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):

    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
