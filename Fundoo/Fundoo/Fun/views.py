import os
from dotenv import load_dotenv
import jwt
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from.serializers import UserRegistrationSerializer, UserLoginSerializer, UserForgotPasswordSerializer, \
    UserGetPasswordSerializer


base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = os.path.join(base, '.env')
load_dotenv(dotenv_path=env)


class UserRegistrationView(GenericAPIView):

    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):

        try:

            # import pdb
            # pdb.set_trace()

            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            confirm_password = request.data.get('confirm_password')
            serializer = UserRegistrationSerializer(data=request.data)

            if serializer.is_valid():

                if User.objects.filter(email=email).exists():
                    return Response(status=status.HTTP_208_ALREADY_REPORTED)

                else:
                    if (email and password) is not None and password == confirm_password:
                        payload = {
                            'username': username,
                            'email': email,
                        }
                        secret = os.getenv('secret')
                        token = jwt.encode(payload, secret, os.getenv('algorithm')).decode('utf-8')
                        user = User.objects.create_user(username, email, password)
                        current_site = get_current_site(request)
                        mail_subject = "Account Activation Link"
                        message = render_to_string('activate.html', {
                            'user': username,
                            'domain': current_site.domain,
                            'token': token
                        })
                        # Remember to change code here!!!<<<<<------------------------------->>>>>
                        send_mail(mail_subject, message, os.getenv('EMAIL_HOST_USER'), ['kishan.bindal@gmail.com'],
                                  fail_silently=True)
                        user.is_active = False
                        user.save()
                        return Response(status=status.HTTP_201_CREATED)
                    else:
                        raise Exception("Password and Confirm Password do not match!")
            else:
                return Response(data='Fail', status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception:
            return Response(data=Exception, status=status.HTTP_400_BAD_REQUEST)


def activate(self, token):

    try:

        decoded_token = jwt.decode(token, os.getenv('secret'), algorithm='HS256')
        username = decoded_token.get('username')

        user = User.objects.get(username=username)

        if user is not None:
            user.is_active = True
            user.save()
            smd_response = {
                'message': 'Successfully activated',
            }
            return JsonResponse(data=smd_response, status=status.HTTP_202_ACCEPTED)

        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception:
        return Response(data=Exception, status=status.HTTP_404_NOT_FOUND)


class UserLoginView(GenericAPIView):

    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):

        try:

            email = request.data.get('email')
            password = request.data.get('password')

            serializer = UserLoginSerializer(data=request.data)

            if serializer.is_valid():

                username = User.objects.get(email=email).username
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    smd = {
                        'message': 'Logged in Successfully'
                    }
                    return JsonResponse(smd, status=status.HTTP_200_OK)
                else:
                    raise ValueError("User Value is None! Please check credentials")
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):

    def post(self, request, *args, **kwargs):
        auth.logout(request)


class UserForgotPasswordView(GenericAPIView):

    serializer_class = UserForgotPasswordSerializer

    def post(self, request, *args, **kwargs):

        try:

            # import pdb
            # pdb.set_trace()

            email = request.data.get('email')
            serializer = UserForgotPasswordSerializer(data=request.data)

            if serializer.is_valid():

                user = User.objects.get(email=email)
                payload = {
                    'username:': user.username,
                    'email': email,
                }
                token = jwt.encode(payload, os.getenv('secret'), os.getenv('algorithm'))

                current_site = get_current_site(request)
                subject = f"Receiving this message because you clicked forgot password on {current_site.domain}"
                from_email = os.getenv('EMAIL_HOST_USER')
                to_email = ['kishan.bindal@gmail.com']  # Change to user email at tim eof production
                message = render_to_string('reset.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'token': token,
                })
                send_mail(subject, message, from_email, to_email, fail_silently=True)
                smd = {
                    'message': f'mail successfully sent to {to_email}'
                }
                return JsonResponse(smd, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


def reset(self, token):

    try:

        decoded_token = jwt.decode(token, os.getenv('secret'), os.getenv('algorithm'))
        username = decoded_token.get('username')

        user = User.objects.get(username=username)

        if user is not None:
            user.save()
            smd = {
                'message': 'ping to reset successful'
            }
            return JsonResponse(smd, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserGetPasswordView(GenericAPIView):

    serializer_class = UserGetPasswordSerializer

    def post(self, request, *args, **kwargs):

        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        serializer = UserGetPasswordSerializer(data=request.data)
        User = get

        if serializer.is_valid():
            return Response(status=status.HTTP_201_CREATED)

