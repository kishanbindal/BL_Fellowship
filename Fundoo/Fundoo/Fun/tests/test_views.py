from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, Client
from django.urls import reverse
from rest_framework.test import force_authenticate
from Fun import views
from Fun.models import User
import pytest
import mock


@pytest.mark.django_db
class TestRegistrationView:

    def test_registration_success(self):

        username = 'kishan'
        email = 'kishan.bindal@gmail.com'
        password = '123'
        confirm_password = '123'

        path = reverse('register')
        request = RequestFactory().post(path)
        request.data = {
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
        }
        response = views.UserRegistrationView.post(self, request)
        assert response.status_code == 201

    def test_registration_view2(self):
        username = 'kishan'
        email = 'kishan.bindal@gmail.com'
        password = '123'
        confirm_password = '0'

        path = reverse('register')
        request = RequestFactory().post(path)
        request.data = {
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
        }
        response = views.UserRegistrationView.post(self, request)
        assert response.status_code == 400

    def test_registration_view3(self):
        username = ''
        email = 'kishan.bindal@gmail.com'
        password = '123'
        confirm_password = '0'

        path = reverse('register')
        request = RequestFactory().post(path)
        request.data = {
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
        }
        response = views.UserRegistrationView.post(self, request)
        assert response.status_code == 400


@pytest.mark.django_db
class TestLoginView:

    # def test_login_functionality(self):
    #
    #     email = 'kishan.bindal@gmail.com'
    #     password = '123'
    #
    #     user = User.objects.create_user(username='kishanbindal', email=email, password=password,
    #                                     confirm_password=password, is_active=True)
    #     user.save()
    #     user.save()
    #     client = Client()
    #     response = client.post(reverse('login'))
    #     assert response.status_code == 200

    def test_login_view_pass(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password,
                                        confirm_password=password, is_active=True)
        user.save()

        path = reverse('login')
        request = RequestFactory().post(path)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.data = {
            'email': email,
            'password': password
        }
        mock.Mock(request)

        response = views.UserLoginView.post(self, request)
        assert response.status_code == 200

    def test_login_view_invalid_password(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password,
                                        confirm_password=password, is_active=True)
        user.save()

        path = reverse('login')
        request = RequestFactory().post(path)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.data = {
            'email': email,
            'password': '12345'
        }
        mock.Mock(request)

        response = views.UserLoginView.post(self, request)
        assert response.status_code == 404

    def test_login_view_invalid_serializer(self):

        email = 'kishan.bindal@gmail.com'
        password = '123'

        user = User.objects.create_user(username='kishanbindal', email=email, password=password,
                                        confirm_password=password, is_active=True)
        user.save()

        path = reverse('login')
        request = RequestFactory().post(path)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        request.data = {
            'email': '12345',
            'password': '12345'
        }
        mock.Mock(request)

        response = views.UserLoginView.post(self, request)
        assert response.status_code == 400


@pytest.mark.django_db
# @mock.patch('Fun.views.UserRegistrationView.post')
class TestForgotPasswordView:

    def test_forgot_password_pass_case(self):

        username = 'asd'
        email = 'asd@gmail.com'
        password = '123'

        user = User.objects.create_user(username=username, email=email, password=password, confirm_password=password)
        user.save()

        path = reverse('forgot-password')
        request = RequestFactory().post(path)
        request.data = {
            'email': email
        }
        response = views.UserForgotPasswordView.post(self, request)
        assert response.status_code == 202

    def test_forgot_password_invalidemail(self):
        username = 'asd'
        email = 'asd@gmail.com'
        password = '123'

        user = User.objects.create_user(username=username, email=email, password=password, confirm_password=password)
        user.save()

        path = reverse('forgot-password')
        request = RequestFactory().post(path)
        request.data = {
            'email': None,
        }
        response = views.UserForgotPasswordView.post(self, request)
        assert response.status_code == 400

    def test_forgot_password_invalid_serializer(self):
        username = 'asd'
        email = 'asd@gmail.com'
        password = '123'

        user = User.objects.create_user(username=username, email=email, password=password,
                                        confirm_password=password)
        user.save()

        path = reverse('forgot-password')
        request = RequestFactory().post(path)
        request.data = {
            'password': None,
        }
        response = views.UserForgotPasswordView.post(self, request)
        assert response.status_code == 404
