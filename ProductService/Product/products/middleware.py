from typing import Any
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from types import SimpleNamespace

import jwt
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization')
        if token:
            token = token.split(' ')[1]
        if not token:
            return JsonResponse({"detail": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            payload = jwt.decode(token, settings.TOKEN_DECODE_KEY, algorithms=["HS256"])
            user_id = payload.get('user_id')
            user = SimpleNamespace(id=user_id, is_authenticated=True, is_active=True)

            request.user = user
            
            return self.get_response(request)
        except Exception as e:
            return JsonResponse({"detail": "Unauthorized", 'error':str(e)}, status=status.HTTP_401_UNAUTHORIZED)
