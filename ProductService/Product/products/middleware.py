from typing import Any
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('HI')
        token = request.headers.get('Authorization')
        if token:
            token = token.split(' ')[1]
        if not token:
            return JsonResponse({"detail": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        print('working', token)
        validate_url = 'http://127.0.0.1:8000/validate_token/'
        headers= {'Authorization':token}
        response = requests.post(validate_url, headers=headers)

        if response.status_code != 200:
            return JsonResponse({"detail": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return self.get_response(request)
