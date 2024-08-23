

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('create/', views.CreateOrder.as_view(), name='create')
]
