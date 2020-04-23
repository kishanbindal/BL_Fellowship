import os
import dotenv
import jwt
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status
from Fundoo.redis_class import Redis
from Fun.models import User


base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = os.path.join(base, '..env')
dotenv.load_dotenv(dotenv_path=env)


class UserCredentialValidation:

    @staticmethod
    def is_empty_register(credentials):

        username = credentials.get('username')
        email = credentials.get('email')
        password = credentials.get('password')

        if (password or email or username) == '' or (password or email or username) == ' ' or password == '':
            raise ValueError("Input Values cannot be Empty")
        elif (password or email or username) is None:
            raise ValueError("Input values cannot be None")
        else:
            return username, email, password

    @staticmethod
    def is_empty_login(credentials):

        email = credentials.get('email')
        password = credentials.get('password')

        if (password or email == '') or (password or email == ' '):
            raise ValueError("Input values cannot be empty!")
        elif password or email is None:
            raise ValueError("Input Value is of None Type!")
        else:
            return email, password


class TokenService:
    '''
    Utility Class For Creating tokens on registration and Login, And for token Decoding.
    '''
    secret = os.getenv('secret')

    def generate_reg_token(self, username, email, *args, **kwargs):
        payload = {
            'username': username,
            'email': email,
        }
        # token = jwt.encode(payload, self.secret, algorithm=os.getenv('algorithm')).decode('utf-8')
        return self.__encode(payload)

    def generate_login_token(self, user_id):
        payload = {
            'id': user_id
        }
        token = jwt.encode(payload, self.secret, algorithm=os.getenv('algorithm')).decode('utf-8')
        return token

    def decode_token(self, token, *args, **kwargs):

        payload = jwt.decode(token, self.secret, algorithms=os.getenv('algorithm'))
        return payload

    def __encode(self, payload):
        return jwt.encode(payload, self.secret, algorithm=os.getenv('algorithm')).decode('utf-8')


class MailServices:

    @staticmethod
    def send_registration_email(username, current_site_url, short_url):  # Add to email at time of production

        # send_mail = (subject, message, from_email, to_email[], fail_silently=True)
        mail_subject = "Account Activation Link"
        message = render_to_string('activate.html', {
            'user': username,
            'domain': current_site_url.domain,
            'token': short_url[2],
        })

        send_mail(mail_subject, message, os.getenv('EMAIL_HOST_USER'), ['kishan.bindal@gmail.com'],
                  fail_silently=True)
        print('mail sent successfully')

    @staticmethod
    def send_forgot_password_email(user, current_site, short_url):  # Add to email at time of production

        subject = f"Receiving this message because you clicked forgot password on {current_site.domain}"
        from_email = os.getenv('EMAIL_HOST_USER')
        to_email = ['kishan.bindal@gmail.com']  # Change to user email at time of production
        message = render_to_string('reset.html', {
            'user': user,
            'domain': current_site.domain,
            'token': short_url[2],
        })
        send_mail(subject, message, from_email, to_email, fail_silently=True)

    @staticmethod
    def send_reminder(user, note):

        subject = f'Reminder for note {note.title}'
        from_email = os.getenv('EMAIL_HOST_USER')
        to_email = ['kishan.bindal@gmail.com']
        message = render_to_string('reminder.html', {
            'user': user,
            'note': note,
        })
        send_mail(subject, message, from_email, to_email, fail_silently=True)


class GoogleLoginServices:

    def __init__(self):

        self.rdb = Redis()
        self.smd = {
            'success': 'Success',
            'message': 'Successfully signed up and logged in through Google',
            'data': []
        }

    def generate_token_at_login(self, user_model, username):

        if user_model.objects.get(username=username) is not None:
            user = user_model.objects.get(username=username)
            key = user.id
            token = TokenService().generate_login_token(key)
            self.smd['message'], self.smd['data'] = 'Successfully Logged in', [token]
            self.rdb.set(key=key, value=token)
            return Response(data=self.smd, status=status.HTTP_200_OK)

        else:
            user = user_model.objects.create_user(username=username)
            user.save()
            user = user_model.objects.get(username=username)
            key = user.id
            token = TokenService().generate_login_token(key)
            self.smd['data'] = [token]
            self.rdb.set(key=key, value=token)
            return Response(self.smd, status=status.HTTP_201_CREATED)


class CollaboratorService:

    @staticmethod
    def get_collaborators(serializer):
        '''
        :return: list of collaborators that can be set to serializer.data['collaborators']
        '''

        collaborators_input = serializer.data.get('collaborators')  # collaborator input has list of emails
        list_of_collaborators = []
        for collaborator_pk in collaborators_input:
            user = User.objects.get(pk=collaborator_pk)
            list_of_collaborators.append(user.id)
        return list_of_collaborators
