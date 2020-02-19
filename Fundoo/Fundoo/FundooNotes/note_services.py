from services import TokenService
from rest_framework.response import Response


class GenerateId:

    @staticmethod
    def generate_id(request):
        token = request.headers.get('token')
        user_id = TokenService().decode_token(token).get('id')
        return user_id
