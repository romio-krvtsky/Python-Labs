from django import forms
from .models import *


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo', 'state', 'description', 'price', 'owner']
