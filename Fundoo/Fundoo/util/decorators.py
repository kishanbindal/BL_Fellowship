from functools import wraps
from services import TokenService
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from Fundoo import redis_class

rdb = redis_class.Redis()


def logged_in(function=None):

    @wraps(function)
    def wrapper(request, id=None, *args, **kwargs):

        smd = {
            'success': 'Fail',
            'message': 'User not Logged in',
            'data': []
        }

        try:
            # token = request.META.get('HTTP_TOKEN')
            token = request.headers.get('token')

            if token is None or token == '':
                raise ValueError("Token not received")

            payload = TokenService().decode_token(token)
            user_id = payload.get('id')
            if rdb.exists(user_id):
                return function(request, id, *args, **kwargs)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            return JsonResponse(smd, status=status.HTTP_401_UNAUTHORIZED)

    return wrapper
