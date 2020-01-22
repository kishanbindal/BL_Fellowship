from django.urls import path, include
from . import views


urlpatterns = [
    path('api/notes', views.NoteView.as_view(), name='Notes')
]
