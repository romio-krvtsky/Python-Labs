from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', ProductsPage.as_view(), name='home'),
    # path('about/', , name='about'),
    # path('my_profile/', , name='my_profile'),
    # path('sell/', , name='add_product'),
    # path('product/<int:product_id>/', show_product, name='product')

]
