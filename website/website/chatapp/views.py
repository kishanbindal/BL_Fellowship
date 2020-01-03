import json
import jwt
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib import auth
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework import permissions


# class UserRegistration(GenericAPIView):
#
#     serializer_class = UserSerializer
#
#     # def get(self, request, *args, **kwargs):
#     #     users = User.objects.all()
#     #     # serializer = UserSerializer(users, many=True)
#     #     return Response('Some info')
#
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         # take credentials
#
#         if serializer.is_valid():
#             serializer.save()
#             # send_mail(subject, from_email, to_list, fail_silently=True)
#             subject = "Please click the link to activate your account"
#             from_email = ''
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserLogin(GenericAPIView):
#
#     serializer_class = UserLoginSerializer
#
#     @ensure_csrf_cookie
#     def post(self, request, *args, **kwargs):
#         import pdb
#         pdb.set_trace()
#
#         data = request.data
#         serializer = UserLoginSerializer(data=data)
#
#         if serializer.is_valid():
#             entry_email = serializer.data.get('user_email')
#             entry_password = serializer.data.get('user_password')
#             query_set = User.objects.get(user_email=entry_email)
#             serialized_query = UserLoginSerializer(data=query_set)
#             if serialized_query.data.get('user_password') == entry_password and serialized_query:
#                 payload = {'user_email': entry_email, 'user_password': data['user_password']}
#                 encoded_token = jwt.encode(payload, 'secret', algorithm='HS256')
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistration(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user_name = request.data['user_name']
            user_email = request.data['user_email']
            user_password = request.data['user_password']
            confirm_password = request.data['confirm_password']
            # query_set = User.objects.all()
            User = get_user_model()
            if user_password == confirm_password and confirm_password != '':
                if User.objects.filter(user_name=user_name, user_email=user_email).exists():
                    return Response(status=status.HTTP_208_ALREADY_REPORTED)
                else:
                    user = User.objects.create(user_name=user_name, user_email=user_email, user_password=user_password)
                    user.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):

    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        try:

            data = request.data
            entry_email = data['user_email']
            entry_password = data['user_password']
            user = auth.authenticate(user_email=entry_email, user_password=entry_password)
            # user = User.get.model()
            if user is not None and user != ' ':
                auth.login(request, user)
                serializer = UserLoginSerializer(user)
                return Response(serializer.data)
            return Response({
                'user': user,
                'message': 'Account is disabled',
                'status': 'UnAuthorized'
            }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return HttpResponse(Exception)



        # serializer = UserLoginSerializer(data=data)
        #
        # if serializer.is_valid():
        #     entry_email = data['user_email']
        #     entry_password = data['user_password']
        #     query_set = User.objects.get(user_email=entry_email)
        #     serialized_query = UserLoginSerializer(data=query_set)
        #     if serialized_query.is_valid():
        #         if serialized_query.data.get('user_password') == entry_password and serialized_query:
        #             payload = {'user_email': entry_email, 'user_password': data['user_password']}
        #             encoded_token = jwt.encode(payload, 'secret', algorithm='HS256')
        #         return Response(serializer.data, status=status.HTTP_200_OK)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
