from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import *


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo', 'state', 'description', 'price', ]

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Error! Price must be positive')

        return price


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', ]
