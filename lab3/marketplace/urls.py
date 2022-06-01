from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('product/<int:pk>/', ViewProduct.as_view(), name='product'),
    path('post_product', PostProduct.as_view(), name='sell'),
    path('register/', RegisterUser.as_view(), name='register')


]
