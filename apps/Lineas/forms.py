from django import forms
from django.forms import ModelForm
from .models import *


class Line_form(ModelForm):
    class Meta:
        model = Linea
        fields = ('name', 'description', 'active')

    def __init__(self, *args, **kwargs):
            super(Line_form, self).__init__(*args, **kwargs)

            for fieldname in ['name', 'description']:
                self.fields[fieldname].widget.attrs['placeholder'] = ''
