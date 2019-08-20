from django import forms
from django.forms import ModelForm
from apps.productos.models import *


class Product_form(ModelForm):
    class Meta:
        model = Producto
        fields = ('foto', 'nombre', 'linea', 'etiquetas', 'precio', 'tallas')

    def __init__(self, *args, **kwargs):
            super(Product_form, self).__init__(*args, **kwargs)

            for fieldname in ['nombre', 'etiquetas', 'precio']:
                self.fields[fieldname].widget.attrs['placeholder'] = ''
