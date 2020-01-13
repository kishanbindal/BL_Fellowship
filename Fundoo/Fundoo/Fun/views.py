import os
import json
from django_short_url.models import ShortURL
from dotenv import load_dotenv
import jwt
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django_short_url.views import get_surl
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from.serializers import UserRegistrationSerializer, UserLoginSerializer, UserForgotPasswordSerializer

# ??? Need to learn how to mask this path ???
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = os.path.join(base, '.env')
load_dotenv(dotenv_path=env)


class UserRegistrationView(GenericAPIView):

    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        '''
        :param request: Takes in Http request
        :return: if user is not in database, creates a User, sends activation email and returns HTTP 201
                if user already exists in database, returns HTTP Response 208
                If some error arises, HTTP 400 is returned
        '''

        try:

            # Get user attributes from the request
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            confirm_password = request.data.get('confirm_password')

            if username is None or username == '':
                raise ValueError("Username cannot be type(None) or empty!")  # Username field cannot be empty string

            if User.objects.filter(email=email).exists():
                return Response(status=status.HTTP_208_ALREADY_REPORTED)  # user should not be registered in DB

            else:
                if (email and password) is not None and password == confirm_password:
                    payload = {
                        'username': username,
                        'email': email,
                    }
                    secret = os.getenv('secret')

                    # Encoding of the token
                    token = jwt.encode(payload, secret, os.getenv('algorithm')).decode('utf-8')
                    s_url = get_surl(str(token))  # Creation of short URL
                    s_url = s_url.split('/')

                    user = User.objects.create_user(username, email, password)

                    # send_mail = (subject, message, from_email, to_email[], fail_silently=True)
                    current_site = get_current_site(request)  # Mail related variables
                    mail_subject = "Account Activation Link"
                    message = render_to_string('activate.html', {
                        'user': username,
                        'domain': current_site.domain,
                        'token': s_url[2],
                    })
                    # Remember to change code here!!!<<<<<------[Change receiver email during production]------>>>>>
                    send_mail(mail_subject, message, os.getenv('EMAIL_HOST_USER'), ['kishan.bindal@gmail.com'],
                              fail_silently=True)

                    # is_active set to false so that user cannot login without activating account from mail
                    user.is_active = False
                    user.save()
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    raise Exception("Password and Confirm Password do not match!")
        except Exception:
            return Response(data=Exception, status=status.HTTP_400_BAD_REQUEST)


def activate(self, token):

    '''

    :param self:
    :param token: short url, converts it back to original token
    :return: returns HTTP202 if account activation was a success, HTTP406 if s_url was not acceptable
            returns HTTP 404 if user is None, or there are any uncaught Exceptions
    '''

    try:

        token_object = ShortURL.objects.get(surl=token)  # Converting s_url to l_url, getting ShortURL object from DB
        token1 = token_object.lurl
        decoded_token = jwt.decode(token1, os.getenv('secret'), algorithm=os.getenv('algorithm'))
        username = decoded_token.get('username')

        user = User.objects.get(username=username)

        if user is not None:  # If user is not None and found, set is_active to True so user can Log-in
            user.is_active = True
            user.save()
            smd_response = {
                'message': 'Successfully activated',
            }
            return JsonResponse(data=smd_response, status=status.HTTP_202_ACCEPTED)

        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)  # Mail link isn't acceptable
    except Exception:
        return Response(data=Exception, status=status.HTTP_404_NOT_FOUND)


class UserLoginView(GenericAPIView):

    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        '''

        :param request: Takes in HTTP Request containing user email and password
        :return: if user is found and authenticated, returns HTTP 200, If not found, asks to check provided credentials
                if serializer/ input data is not valid raises a HTTP 404.
        '''

        try:

            # import pdb
            # pdb.set_trace()

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
                    raise ValueError("Please check credentials!!")
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):

    def post(self, request, *args, **kwargs):
        '''
        :param request: takes in a post request with no attributes
        :return: Returns a HTTP 200 after logging user out.
        '''
        auth.logout(request)
        smd = {
            'message': 'Successfully Logged out',
            'status:': 'You are logged out',
        }
        return Response(status=status.HTTP_200_OK)


class UserForgotPasswordView(GenericAPIView):

    serializer_class = UserForgotPasswordSerializer

    def post(self, request, *args, **kwargs):

        '''
        :param request: takes in a HTTP request with only email ID
        :return: sends a mail to given email ID(if user is found) and returns HTTP202
                If input credentials do not match serializer, HTTP 400 is returned
                If any uncaught errors exist(eg:- user does not exist), HTTP 404 is returned
        '''

        try:

            email = request.data.get('email')
            serializer = UserForgotPasswordSerializer(data=request.data)

            if serializer.is_valid():

                user = User.objects.get(email=email)
                payload = {
                    'username': user.username,
                    'email': email,
                }
                token = jwt.encode(payload, os.getenv('secret'), algorithm=os.getenv('algorithm')).decode('utf-8')
                s_url = get_surl(str(token))
                print(s_url)
                s_url = s_url.split('/')

                current_site = get_current_site(request)
                subject = f"Receiving this message because you clicked forgot password on {current_site.domain}"
                from_email = os.getenv('EMAIL_HOST_USER')
                to_email = ['kishan.bindal@gmail.com']  # Change to user email at time of production
                message = render_to_string('reset.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'token': s_url[2],
                })
                send_mail(subject, message, from_email, to_email, fail_silently=True)

                smd = {
                    'message': f'mail successfully sent to {to_email}'
                }
                return JsonResponse(smd, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


def reset(request, token):
    '''
    :param request: Contains New Password
    :param token: token from reset.html
    :return: Http200 for successful change, Http406 in case user is None, Http404 in case of uncaught Exceptions
    '''
    smd = {
        'message': 'ping to reset successful',
        'status': 'Password change unsuccessful'
    }

    try:

        print(request.body)
        request_data = json.loads(request.body)  # Convert incoming data into python dict() object
        new_password = request_data.get('new_password')

        if new_password is None or new_password == '':
            raise ValueError('Password Value cannot be None or empty')

        token_object = ShortURL.objects.get(surl=token)
        token1 = token_object.lurl
        decoded_token = jwt.decode(token1, os.getenv('secret'), algorithm=os.getenv('algorithm'))
        username = decoded_token.get('username')

        user = User.objects.get(username=username)

        if user is not None:
            user.set_password(new_password)
            user.save()
            # response = HttpResponse()
            # return redirect('get-user-credentials')
            smd = {
                'message': 'ping to reset successful',
                'status': 'Password Successfully Reset/Changed',
            }

            return JsonResponse(smd, status=status.HTTP_200_OK)

        return JsonResponse(smd, status=status.HTTP_406_NOT_ACCEPTABLE)

    except Exception:
        return JsonResponse(smd, status=status.HTTP_404_NOT_FOUND)
