from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo', 'state', 'description', 'price', ]


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', ]
