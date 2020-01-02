from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register', views.UserRegistration.as_view(), name='register')

]
