from django.shortcuts import render
from .models import Products
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

# Create your views here.


class ProductsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        products = Products.objects.all()
        return Response(products, status=status.HTTP_200_OK)