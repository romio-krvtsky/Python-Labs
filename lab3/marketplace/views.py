from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from marketplace.models import Product

# Create your views here.


class HomePage(ListView):
    model = Product
    template_name = 'marketplace/home_page.html'
    context_object_name = 'products'


class ViewProduct(DetailView):
    model = Product
    template_name = 'marketplace/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'



def index(request, product_id):
    return HttpResponse(f'product {product_id}')


