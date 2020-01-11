from django.test import RequestFactory, Client
from django.urls import reverse
from Fun import views
from Fun.models import User
import pytest


@pytest.mark.django_db
class TestViews:

    def test_registration_view1(self):

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

    def test_login_view_1(self):

        email = 'asd@gmail.com'
        password = 'password'

        path = reverse('login')
        request = RequestFactory().post(path)
        request.data = {
            'email': email,
            'passowrd': password
        }

        response = views.UserLoginView.post(self, request)
        assert response.status_code == 200
