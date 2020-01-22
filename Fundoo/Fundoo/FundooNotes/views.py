from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from Fun.models import User
from util.decorators import logged_in
from .models import Note, Label
from .serializers import CreateNoteSerializer
from Fundoo.redis_class import Redis
from services import TokenService

rdb = Redis()


class NoteView(GenericAPIView):

    serializer_class = CreateNoteSerializer

    def post(self, request, *args, **kwargs):
        pass
