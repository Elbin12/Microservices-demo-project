from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('home/', views.Home.as_view(), name='home'),
    path('validate_token/', views.ValidateToken.as_view(), name='validate_token')
]
