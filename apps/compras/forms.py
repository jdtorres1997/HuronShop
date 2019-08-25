
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django_select2.forms import Select2Widget
from apps.compras.models import *
from django import forms 
import re
 
class Compra_form(ModelForm):
    class Meta:
        model = Compra
        fields = ('nombre', 'descripcion', 'estado_compra', 'precio', 'cantidad', 'precio_total')

    def __init__(self, *args, **kwargs):
            super(Compra_form, self).__init__(*args, **kwargs)

            for fieldname in ['nombre', 'descripcion', 'estado_compra', 'precio', 'cantidad', 'precio_total']:
                self.fields[fieldname].widget.attrs['placeholder'] = ''
            
            self.fields['precio_total'].widget.attrs['placeholder'] = '0'
            self.fields['precio'].widget.attrs['placeholder'] = '0'
            self.fields['cantidad'].widget.attrs['placeholder'] = '0'

class Compra_consult_form(ModelForm):
    class Meta:
        model = Compra
        fields = ('nombre', 'descripcion', 'estado_compra')

    def __init__(self, *args, **kwargs):
            super(Compra_consult_form, self).__init__(*args, **kwargs)

            for fieldname in ['nombre', 'descripcion', 'estado_compra']:
                self.fields[fieldname].required = False
                self.fields[fieldname].default = ""
                self.fields[fieldname].widget.attrs['placeholder'] = ''