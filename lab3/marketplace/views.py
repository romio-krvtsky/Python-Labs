from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from marketplace.forms import AddProductForm, RegistrationForm
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


class PostProduct(LoginRequiredMixin, CreateView):
    form_class = AddProductForm
    template_name = 'marketplace/post_product.html'
    login_url = reverse_lazy('home')


class MyProfile(ListView):
    model = Product
    template_name = 'marketplace/my_profile.html'
    context_object_name = 'products'


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'marketplace/register.html'
    success_url = reverse_lazy('login')

