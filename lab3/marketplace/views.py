from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from marketplace.models import Product


class ProductsPage(ListView):
    model = Product
    template_name = 'marketplace/home_page.html'
    context_object_name = 'products'


