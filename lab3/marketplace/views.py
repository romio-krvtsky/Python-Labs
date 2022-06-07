import asyncio
import logging
from asgiref.sync import sync_to_async
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from marketplace.forms import AddProductForm, RegistrationForm
from marketplace.models import Product

logger = logging.getLogger('main')


# Create your views here.

@sync_to_async
def get_my_products(self):
    return Product.objects.filter(owner=self.request.user)


class HomePage(ListView):
    logger.info('Home Page')
    model = Product
    template_name = 'marketplace/home_page.html'
    context_object_name = 'products'


class PostProduct(LoginRequiredMixin, CreateView):
    logger.info('Posting Product')
    form_class = AddProductForm
    template_name = 'marketplace/post_product.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostProduct, self).form_valid(form)


class ViewProduct(DetailView):
    logger.info('Product Info')
    model = Product
    template_name = 'marketplace/product.html'
    context_object_name = 'product'


class EditProduct(UpdateView):
    logger.info('Product Update')
    model = Product
    fields = ['name', 'photo', 'state', 'description', 'price']
    template_name = 'marketplace/edit_product.html'
    context_object_name = 'product'


class DeleteProduct(DeleteView):
    logger.info('Product delete')
    model = Product
    template_name = 'marketplace/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('my_profile')


class MyProfile(LoginRequiredMixin, ListView):
    logger.info('My Profile')
    model = Product
    template_name = 'marketplace/my_profile.html'
    context_object_name = 'products'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return asyncio.run(get_my_products(self))


class RegisterUser(CreateView):
    logger.info('Registration')
    form_class = RegistrationForm
    template_name = 'marketplace/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    logger.info('Login')
    form_class = AuthenticationForm
    template_name = 'marketplace/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutUser(LogoutView):
    logger.info('Logout')
    template_name = 'registration/logged_out.html'
    next_page = 'home'
