from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from marketplace.forms import AddProductForm
from marketplace.models import Product


# Create your views here.


class HomePage(ListView):
    model = Product
    template_name = 'marketplace/home_page.html'
    context_object_name = 'products'


class ViewProduct(DetailView):
    model = Product
    template_name = 'marketplace/product.html'
    context_object_name = 'product'


class PostProduct(CreateView):
    form_class = AddProductForm
    template_name = 'marketplace/post_product.html'



