from core.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)    
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
"""
Views for the user API.
"""
from rest_framework import generics
from core.models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.



class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


""" User all or user id"""

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserListCreateAPIView(generics.ListCreateAPIView):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication] 
    serializer_class = UserSerializer
    def get_queryset(self):
        print("@@@@@@@@@@@@@@@@@@@@@")
        """
        This view should return a list of users
        for the currently authenticated user.
        """
        print(self.request.user.is_staff)
        if self.request.user.is_staff == False:
            print("1"*50)
            user_data= self.request.user.id
            print(user_data)
            data = User.objects.filter(id=user_data)
            print(data)
            return data
        else:
            print("2"*50)
            data = User.objects.all()
            return data
        

class UserRetrtieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    print("%%%%%%%%%%%%%%%")
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializer
    def get_queryset(self):
        print("ididididid")
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        print(self.request.user.is_staff)
        if self.request.user.is_staff == False:

            user_data= self.request.user.id
            data = User.objects.filter(id= user_data)
            return data
        else:
            data = User.objects.all()
            return data