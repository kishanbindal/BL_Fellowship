from django.views.generic import TemplateView
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/register', views.UserRegistrationView.as_view(), name='register'),
    path('activate/<token>', views.activate, name='activate'),
    path('api/login', views.UserLoginView.as_view(), name='login'),
    path('api/logout', views.UserLogoutView.as_view(), name='logout'),
    path('api/forgotpassword', views.UserForgotPasswordView.as_view(), name='forgot-password'),
    path('reset/<token>', views.reset, name='reset'),
    path('api/uploadimage', views.UploadImage.as_view(), name='upload-image'),
    path('api/google', views.LoginGoogleAuthorization.as_view(), name='google-auth'),
    path('api/google-callback', views.LoginGoogle.as_view(), name='google-callback'),
    path('api/github', views.LoginGitHubAuthorization.as_view(), name='github-auth'),
    path('api/github-callback', views.LoginGitHub.as_view(), name='github-callback'),
    path('api/users', views.GetAllUsers.as_view(), name='get-users'),
    # path('api/', TemplateView.as_view(template_name="login_page.html")),
    # path('api/credentials/<token>', views.UserGetPasswordView.as_view(), name='get-user-credentials')
]
