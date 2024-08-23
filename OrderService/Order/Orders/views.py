from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Orders

# Create your views here.

class OrdersView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        orders = Orders.objects.all()
        return Response({'orders':orders}, status=status.HTTP_200_OK)
    
