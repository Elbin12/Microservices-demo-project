from django.shortcuts import render
from .models import Products
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
import json
from .serializers import ProductSerializer
# Create your views here.


class ProductsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response({'products':serializer.data}, status=status.HTTP_200_OK)