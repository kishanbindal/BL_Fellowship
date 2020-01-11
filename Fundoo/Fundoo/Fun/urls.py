from django.urls import path, include
from . import views

urlpatterns = [
    path('api/register', views.UserRegistrationView.as_view(), name='register'),
    path('activate/<token>', views.activate, name='activate'),
    path('api/login', views.UserLoginView.as_view(), name='login'),
    path('api/logout', views.UserLogoutView.as_view(), name='logout'),
    path('api/forgotpassword', views.UserForgotPasswordView.as_view(), name='forgot-password'),
    path('reset/<token>', views.reset, name='reset'),
    # path('api/credentials/<token>', views.UserGetPasswordView.as_view(), name='get-user-credentials')
]
