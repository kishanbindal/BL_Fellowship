from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('api/login', views.UserLogin.as_view(), name='login'),
    path('api/register', views.UserRegistration.as_view(), name='register'),
    path('api/logout', views.UserLogout.as_view(), name='logout'),
    path('activate/<token>', views.activate, name='activate'),
    path('api/api/forgotpassword', views.UserForgotPassword.as_view(), name='forgot-password'),,
    path('verify/<token>', views.activate, name='activate'),
]
