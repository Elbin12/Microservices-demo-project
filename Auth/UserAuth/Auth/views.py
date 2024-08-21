from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import aauthenticate, login, logout
from .serializers import UserSerializer
from rest_framework import status, permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

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
        

class Login(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        print(request.data)
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        login(request, user)
        refresh = RefreshToken.for_user(user)
        refresh["first_name"] = str(user.first_name)
        content = {
            'isAdmin': user.is_superuser,
            'access_token' : str(refresh.access_token),
            'refresh_token' : str(refresh)
        }

        response = Response(content, status=status.HTTP_200_OK)

        return response 
    
class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        print(request.data)

        logout(request)
        try:
            refresh_token = request.data["refresh_token"]
            print(refresh_token,'token')
            token = RefreshToken(refresh_token)
            print('hi')
            token.blacklist()
            print('ji')
            response = Response(status=status.HTTP_205_RESET_CONTENT)
            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class Home(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        data = {'user': request.user.username,'first_name': request.user.first_name, 'email': request.user.email}
        return Response(data, status=status.HTTP_200_OK)