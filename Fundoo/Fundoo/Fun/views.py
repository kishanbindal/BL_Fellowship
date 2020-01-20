"""

"""
from services import UserCredentialValidation, TokenService, MailServices
from Fundoo import redis_class
import logging
from PIL import Image
import requests
from .aws_services import AmazonServicesS3Util
import boto3
import os
import json
from django_short_url.models import ShortURL
from dotenv import load_dotenv
import jwt
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django_short_url.views import get_surl
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserForgotPasswordSerializer, \
    UploadImageSerializer

# ??? Need to learn how to mask this path ???
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = os.path.join(base, '.env')
load_dotenv(dotenv_path=env)


rdb = redis_class.Redis()


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

            # # Get user attributes from the request
            # username = request.data.get('username')
            # email = request.data.get('email')
            # password = request.data.get('password')

            # if username is None or username == '' or password == '' or email == '':
            #     raise ValueError("Field cannot be type(None) or empty!")  # Username field cannot be empty string
            '''Validation Done here'''

            username, email, password = UserCredentialValidation.is_empty_register(request.data)

            #business logic TODO
            # response=UserRegistrationService.fj()
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                return Response(status=status.HTTP_208_ALREADY_REPORTED)  # user should not be registered in DB

            else:
                if (email and password) is not None:
                    # payload = {
                    #     'username': username,
                    #     'email': email,
                    # }
                    # secret = os.getenv('secret')

                    # Encoding of the token
                    # token = jwt.encode(payload, secret, os.getenv('algorithm')).decode('utf-8')  # TODO token wrapper
                    token = TokenService().generate_token(username, email)
                    print(token)

                    s_url = get_surl(str(token))  # Creation of short URL
                    s_url = s_url.split('/')

                    user = User.objects.create_user(username, email, password)

                    # send_mail = (subject, message, from_email, to_email[], fail_silently=True)
                    current_site = get_current_site(request)  # Mail related variables
                    # mail_subject = "Account Activation Link"
                    # message = render_to_string('activate.html', {
                    #     'user': username,
                    #     'domain': current_site.domain,
                    #     'token': s_url[2],
                    # })
                    # # Remember to change code here!!!<<<<<------[Change receiver email during production]------>>>>>
                    # send_mail(mail_subject, message, os.getenv('EMAIL_HOST_USER'), ['kishan.bindal@gmail.com'],
                    #           fail_silently=True)  # TODO email wrapper

                    MailServices.send_registration_email(username, current_site, s_url)
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

            email = request.data.get('email')
            password = request.data.get('password')

            serializer = UserLoginSerializer(data=request.data)

            if serializer.is_valid():

                username = User.objects.get(email=email).username
                user = auth.authenticate(username=username, password=password)
                print(user.id)
                if user is not None:
                    payload = {
                        'id': user.id,
                    }
                    secret = os.getenv('secret')
                    algorithm = os.getenv('algorithm')
                    token = jwt.encode(payload, secret, algorithm=algorithm).decode('utf-8')

                    smd = {
                        'message': 'Logged in Successfully',
                        'token': token
                    }
                    print(token)
                    # REDIS CONTENT GOES HERE
                    rdb.set(user.id, token)
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

        token = request.headers.get('token')
        payload = jwt.decode(token, os.getenv('secret'), algorithm=os.getenv('algorithm'))
        user_id = payload.get('id')
        rdb.delete(user_id)
        smd = {
            'success': 'Success',
            'message': 'Successfully Logged out',
            'data': []
        }

        return Response(data=smd, status=status.HTTP_200_OK)


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


class UploadImage(GenericAPIView):

    serializer_class = UploadImageSerializer

    # @login_required(login_url='api/login')
    def post(self, request, *args, **kwargs):
        smd = {
            'message': 'Successfully Added Image',
            'success': 'Success',
            'data': []
            }

        # request_data = json.loads(request.body)
        img_file = request.FILES['image']
        token = request.headers.get('token')
        decoded_token = jwt.decode(token, os.getenv('secret'), os.getenv('algorithm'))
        user_id = str(decoded_token.get('id'))

        if user_id:

            s3 = AmazonServicesS3Util.create_s3_client()
            AmazonServicesS3Util.upload_image_file(s3, img_file, user_id)
            url = AmazonServicesS3Util.generate_url(user_id)
            presign_url = AmazonServicesS3Util.generate_presigned_url(user_id)
            print(presign_url)

            # s3 = boto3.client('s3')
            # s3.upload_fileobj(img_file, os.getenv('AWS_STORAGE_BUCKET_NAME'), user_id)

            # s3 = boto3.client('s3')
            # s3.Bucket(os.getenv('AWS_STORAGE_BUCKET_NAME')).put_object(Key=email, Body=image_file)
            # url = "https://django-fundoo.s3.ap-south-1.amazonaws.com/{}".format(email)
            # url = f"https://{os.getenv('AWS_STORAGE_BUCKET_NAME')}.s3.ap-south.amazonaws.com/{user_id}"

            user = User.objects.get(pk=user_id)
            user.__setattr__("profile_image", url)
            user.save()

            return JsonResponse(smd, status=status.HTTP_202_ACCEPTED)
        else:
            smd = {
                'message': 'Upload Failed',
                'status': 'fail'
            }
            return JsonResponse(smd, status=status.HTTP_400_BAD_REQUEST)


def get_auth_code(response):

    authorization_code = response.GET['code']
    print(f'authorization_code is : {authorization_code}')
    return authorization_code


def get_username(token, url):

    # headers = {'authorize': "bearer " + token}
    # api_response = requests.post('https://www.googleapis.com/gmail/v1/users/userId/profile', headers=token)
    # api_response = requests.get('https://www.googleapis.com/auth/userinfo.profile', headers=headers)
    headers = {
        "Authorization": f"Bearer {token}",
    }
    # api_response = requests.get('https://www.googleapis.com/oauth2/v1/userinfo', headers=headers)
    api_response = requests.get(url, headers=headers)
    return api_response


class LoginGoogleAuthorization(GenericAPIView):

    def get(self, request):
        '''
        Summary : send response to google Authentication/Authorization server, if response is 200, redirect to
                    Google Permissions page
        :param request:
        :return:  if the status code from google authorization api is 200,
                redirected to Permissions page
        '''

        # https://accounts.google.com/o/oauth2/v2/auth Request for Authentication Token
        url = os.getenv('SOCIAL_AUTH_GOOGLE_URL')
        params = {
            'client_id': os.getenv('SOCIAL_AUTH_GOOGLE_CLIENTID'),
            'response_type': 'code',
            'scope': 'profile',
            'redirect_uri': 'http://localhost:8000/fun/api/google-callback',
            'access_type': 'online',
        }

        response = requests.get(url, params)

        if response.status_code == 200:
            return redirect(response.url)
        return Response(response, status=response.status_code)


class LoginGoogle(GenericAPIView):

    def get(self, request):

        '''
        :Summary : Post redirect to callback URI, send authorization token to receive access token, with this access
                    get user profile information from Google OAuth API.
        :param request: request url consists of the auth_code with the user scopes.
        :return: Http 200 if user_info is recieved, else Response from Google API. Exceptions will raise Http 400
        '''

        try:

            # access_url = 'https://www.googleapis.com/oauth2/v4/token'
            access_url = os.getenv('SOCIAL_AUTH_GOOGLE_GET_TOKEN')
            auth_code = get_auth_code(request)
            params = {
                'client_id': os.getenv('SOCIAL_AUTH_GOOGLE_CLIENTID'),
                'client_secret': os.getenv('SOCIAL_AUTH_GOOGLE_CLIENTSECRET'),
                'code': auth_code,
                'grant_type': "authorization_code",
                'redirect_uri': 'http://localhost:8000/fun/api/google-callback'
            }

            response = requests.post(access_url, params)
            x = json.loads(response.content)
            token = x.get('access_token')

            api_response = get_username(token, os.getenv('SOCIAL_AUTH_GOOGLE_GET_INFO'))

            smd = {
                'success': 'Success',
                'message': 'Successfully signed up and logged in through Google'
            }

            if api_response.status_code == 200:
                data = json.loads(api_response.content)
                username = data.get('name')
                user = User.objects.create_user(username=username)
                user.save()
                return Response(data=smd, status=api_response.status_code)
            else:
                smd['success'] = 'Fail'
                smd['message'] = 'Failed to Sign up with Google'
                return Response(data=smd, status=api_response.status_code)
        except Exception:
            return Response(data=Exception, status=status.HTTP_400_BAD_REQUEST)


class LoginGitHubAuthorization(GenericAPIView):

    def get(self, request, *args, **kwargs):

        auth_url = os.getenv('SOCIAL_AUTH_GITHUB_URL')
        params = {
            'client_id': os.getenv('SOCIAL_AUTH_GITHUB_CLIENTID'),
            'redirect_uri': os.getenv('GITHUB_REDIRECT_URI'),
            # 'scope': 'scope',
        }

        response = requests.get(auth_url, params)

        if response.status_code == 200:
            return redirect(response.url)
        return Response(status=response.status_code)


class LoginGitHub(GenericAPIView):

    def get(self, request, *args, **kwargs):

        # import pdb
        # pdb.set_trace()
        try:
            access_url = os.getenv('SOCIAL_AUTH_GITHUB_GET_TOKEN')
            auth_code = get_auth_code(request)
            params = {
                'client_id': os.getenv('SOCIAL_AUTH_GITHUB_CLIENTID'),
                'client_secret': os.getenv('SOCIAL_AUTH_GITHUB_CLIENTSECRET'),
                'code': auth_code,
                'redirect_uri': os.getenv('GITHUB_REDIRECT_URI'),
            }
            response = requests.post(access_url, params)
            x = response.text
            # x = response.text.strip('&')[0]
            # token = x.lstrip('access_token')
            r = x.lstrip('access_token=')
            token = r.rstrip("&scope=&token_type=bearer")

            headers = {
                "Authorization": f"token {token}"
            }
            api_response = requests.get(os.getenv('SOCIAL_AUTH_GITHUB_GET_INFO'), headers=headers)

            smd = {
                'success': 'Success',
                'message': 'Successfully signed up and logged in through Github',
                'data': []
            }

            if api_response.status_code == 200:
                info = json.loads(api_response.content)
                username = info.get('login')
                user = User.objects.create_user(username=username)
                user.save()
                return Response(data=smd, status=api_response.status_code)
            else:
                smd['success'] = 'FAIL'
                smd['message'] = 'Sign Up and Login Failed'
                return Response(data=smd, status=api_response.status_code)
        except Exception:
            return Response(data=Exception, status=status.HTTP_400_BAD_REQUEST)
