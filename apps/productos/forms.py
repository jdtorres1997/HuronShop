from django import forms
from django.forms import ModelForm
from .models import *

class Line_form(ModelForm):
    class Meta:
        model = Linea
        fields = '__all__'