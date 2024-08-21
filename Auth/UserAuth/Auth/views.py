from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import status

# Create your views here.


class Signup(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data received'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)