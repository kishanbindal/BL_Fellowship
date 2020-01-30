import jwt
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, UserLoginSerializer


class UserRegistration(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            # import pdb
            # pdb.set_trace()

            user_name = request.POST.get('username', None)
            user_email = request.data['email']
            user_password = request.data['password']

            if user_name is None:
                raise Exception("Username is required")

            User = get_user_model()
            if User.objects.filter(username=user_name, email=user_email).exists():
                return Response(status=status.HTTP_208_ALREADY_REPORTED)
            else:
                user = User.objects.create_user(username=user_name, email=user_email, password=user_password)
                user.is_active = False
                user.save()
                payload = {
                    'username': user_name,
                    'email': user_email,
                }
                secret = 'secretkey'
                token = jwt.encode(payload, secret, algorithm='HS256').decode('utf-8')

                # send_mail = (subject, message, from_mail, to_email_list[], fail_silently=True)

                mail_subject = 'Account Activation Link'
                # message = f'Thank you for registering. To activate your account please follow the link below. \n{token}'
                from_mail_id = settings.EMAIL_HOST_USER
                to_email_id = [user_email]
                current_site = get_current_site(request)
                message = render_to_string('activation.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'token': token,
                })

                print(current_site)

                send_mail(mail_subject, message, from_mail_id, to_email_id, fail_silently=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def activate(self, token):

    import pdb
    pdb.set_trace()

    decoded_token = jwt.decode(token, 'secretkey', algorithm='HS256')

    email = decoded_token.get('email')
    username = decoded_token.get('username')
    user = User.objects.get(username=username)

    if username is not None:
        user.is_active = True
        redirect('home')
        return HttpResponse('success')

    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


    # decoded_token = jwt.decode(token, 'secretkey', algorithms='HS256')

    # username = decoded_token.get('username')

    # if username is not None:
    #     # username.save()
    #     return HttpResponse('success')


class UserLogin(APIView):

    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            import pdb
            pdb.set_trace()

            # data = request.data
            entry_email = request.data['user_email']
            entry_password = request.data['user_password']
            # username = User.objects.get(email=entry_email).username
            user = auth.authenticate(email=entry_email, password=entry_password)
            print(user)
            # user = User.get.model()
            if user is not None and user != ' ':
                auth.login(request, user)
                user.save()
                # serializer = UserLoginSerializer(user)
                return Response({
                    'user': user,
                    'message': 'successfully logged in',
                    'status': 'UnAuthorized'
                }, status=status.HTTP_200_OK)
            return Response({
                'user': user,
                'message': 'Account is disabled',
                'status': 'UnAuthorized'
            }, status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserLogout(APIView):

    def post(self, request, *args, **kwargs):

        auth.logout(request)

        return Response(status=status.HTTP_200_OK)


class UserForgotPassword(APIView):

    def post(self, request, *args, **kwargs):
        try:

            # import pdb
            # pdb.set_trace()

            username = request.data['username']
            print(username)
            User = get_user_model()
            user = User.objects.get(username=username)
            email = user.email
            print(user)

            if user is not None:

                payload = {
                    'username': username,
                    'email': email
                }
                secret = 'secretkey'
                token = jwt.encode(payload, secret, algorithm='HS256').decode('utf-8')
                from_mail = settings.EMAIL_HOST_USER
                to_email = [email]
                subject = 'Password reset for Forgot Password'
                current_site = get_current_site(request)
                message = render_to_string('forgotpassword.html', {
                    'user': payload,
                    'domain': current_site.domain,
                    'token': token
                })
                # send_mail = (subject, message, from_mail, to_email_list[], fail_silently=True)

                send_mail(subject, message, from_mail, to_email, fail_silently=True)
                return Response('success')
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_302_FOUND)


def verify(self, token):
    import pdb
    pdb.set_trace()

    decoded_token = jwt.decode(token, 'secretkey', algorithm='HS256')

    username = decoded_token.get('username')
    user = User.objects.get(username=username)

    if user is not None:
        return redirect('get-credentials')
    return Response(status=status.HTTP_400_BAD_REQUEST)


class GetForgotCredentials(APIView):
    pass