from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
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
    login_url = reverse_lazy('login')


class MyProfile(ListView):
    model = Product
    template_name = 'marketplace/my_profile.html'
    context_object_name = 'products'


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'marketplace/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'marketplace/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutUser(LogoutView):
    template_name = 'registration/logged_out.html'
    next_page = 'home'



