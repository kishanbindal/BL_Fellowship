import os
import dotenv
import jwt
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django_short_url.views import get_surl
from django.template.loader import render_to_string


base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = os.path.join(base, '.env')
dotenv.load_dotenv(dotenv_path=env)


class UserCredentialValidation:

    @staticmethod
    def is_empty_register(credentials):
        import pdb
        pdb.set_trace()

        username = credentials.get('username')
        email = credentials.get('email')
        password = credentials.get('password')

        if (password or email or username) == '' or (password or email or username) == ' ':
            raise ValueError("Input Values cannot be Empty")
        elif (password or email or username) is None:
            raise ValueError("Input values cannot be None")
        else:
            return username, email, password

    @staticmethod
    def is_empty_login(**credentials):

        email = credentials.get('email')
        password = credentials.get('password')

        if (password or email == '') or (password or email == ' '):
            raise ValueError("Input values cannot be empty!")
        elif password or email is None:
            raise ValueError("Input Value is of None Type!")
        else:
            return email, password


class UserRegistrationService:
    pass


class TokenService:

    secret = os.getenv('secret')

    def generate_token(self, username, email):
        payload = {
            'username': username,
            'email': email,
        }
        token = jwt.encode(payload, self.secret, algorithm=os.getenv('algorithm')).decode('utf-8')
        return token

    def decode_token(self, token):

        payload = jwt.decode(token, self.secret, algorithm=os.getenv('algorithm'))
        return payload


class MailServices:

    @staticmethod
    def send_registration_email(username, current_site_url, short_url):

        mail_subject = "Account Activation Link"
        message = render_to_string('activate.html', {
            'user': username,
            'domain': current_site_url.domain,
            'token': short_url[2],
        })
        send_mail(mail_subject, message, os.getenv('EMAIL_HOST_USER'), ['kishan.bindal@gmail.com'],
                  fail_silently=True)
        print('mail sent successfully')
