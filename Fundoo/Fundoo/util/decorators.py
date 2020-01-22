from functools import wraps
from services import TokenService
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response


def logged_in(function=None, redis_db=None):

    @wraps(function)
    def wrapper(request, *args, **kwargs):

        smd = {
            'success': 'Fail',
            'message': 'User not Logged in',
            'data': []
        }

        try:

            token = request.headers.get('token')

            if token is None or token == '':
                raise ValueError("Token not received")

            payload = TokenService().decode_token(token)
            user_id = payload.get('id')
            if redis_db.exists(user_id):
                return function(request, *args, **kwargs)
            return JsonResponse(data=smd, status=status.HTTP_401_UNAUTHORIZED)

        except ValueError:
            return Response(ValueError, status=status.HTTP_400_BAD_REQUEST)

    return wrapper
