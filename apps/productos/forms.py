from django import forms
from django.forms import ModelForm
from apps.productos.models import *

class Product_form(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'