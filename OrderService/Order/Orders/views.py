from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Orders
from .serializers import OrderSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

import grpc
from . import products_pb2
from . import products_pb2_grpc

import jwt
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings



# Create your views here.

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class OrdersView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        orders = Orders.objects.filter(user_id=request.user.id)
        serializer = OrderSerializer(orders, many=True)
        return Response({'orders':serializer.data}, status=status.HTTP_200_OK)
    
class CreateOrder(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user_id = request.user.id
        product_id = request.data['product_id']

        channel = grpc.insecure_channel('127.0.0.1:8002')
        stub = products_pb2_grpc.ProductServiceStub(channel)

        product_response = stub.GetProductPrice(products_pb2.ProductRequest(product_id = int(product_id)))
        print(product_response,'lll')

        price = product_response.price

        Orders.objects.create(user_id = user_id, product_id = product_id, total_amount = price)

        return Response('Order created', status=status.HTTP_201_CREATED)

        
