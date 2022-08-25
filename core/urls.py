"""
URL mappings for the user API.
"""
from django.urls import path

# from user import views

from core.views import *





urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token'),
    path('customer_info_view/', UserListCreateAPIView.as_view(), name="customer_info_view"),
    path('customer_info_detail_view/<int:pk>/', UserRetrtieveUpdateDestroyAPIView.as_view(), name="customer_info_detail_view"),
    
]