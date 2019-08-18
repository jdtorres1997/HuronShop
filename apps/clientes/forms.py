from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django_select2.forms import Select2Widget
from apps.clientes.models import *
from django import forms 
import re

class ClienteAddForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('first_name', 'last_name', 'cedula', 'email', 'telefono', 'direccion')

    def __init__(self, *args, **kwargs):
        super(ClienteAddForm, self).__init__(*args, **kwargs)

        for fieldname in ['first_name', 'last_name', 'cedula', 'email', 'telefono', 'direccion']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = ''

    def clean(self):
        nombre = self.cleaned_data['first_name']
        apellido = self.cleaned_data['last_name']
        cedula = self.cleaned_data['cedula']
        correo = self.cleaned_data['email']
        telefono = self.cleaned_data['telefono']
        direccion = self.cleaned_data['direccion']

        regex_nombre = re.compile('^[a-zA-ZÀ,\s]{3,20}$', re.IGNORECASE)
        regex_cedula = re.compile('^[0-9]{8,11}$')
        regex_email = re.compile('^(([^<>()\[\],;:\s@"]+(\.[^<>()\[\],;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')

        c = Cliente.objects.filter(cedula=cedula).count()
        
        if not regex_nombre.match(nombre):
            self.add_error('first_name','Nombre debe ser mayor a 3 caracteres y a-z')

        if not regex_nombre.match(apellido):
            self.add_error('last_name','Apellido debe ser mayor a 3 caracteres y a-z')

        if not regex_email.match(correo):
            self.add_error('email','Correo inválido')

        if len(str(telefono)) < 7 or len(str(telefono)) > 11: 
            self.add_error('telefono','Teléfono deber ser entre 7 y 11 números')

        if not c == 0:
            self.add_error('cedula', 'Cedula ya registrada')
        else:
            if not regex_cedula.match(cedula):
                self.add_error('cedula','Cédula debe ser numérica entre 8 y 11 números')

        if not len(direccion) > 3:
            self.add_error('direccion','Dirección deber ser entre 3 y 50 caracteres')

        return self.cleaned_data

class ClienteEditForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('first_name', 'last_name', 'email', 'telefono', 'direccion')

    def __init__(self, *args, **kwargs):
        super(ClienteEditForm, self).__init__(*args, **kwargs)

        for fieldname in ['first_name', 'last_name', 'email', 'telefono', 'direccion']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = ''

    def clean(self):
        nombre = self.cleaned_data['first_name']
        apellido = self.cleaned_data['last_name']
        correo = self.cleaned_data['email']
        telefono = self.cleaned_data['telefono']
        direccion = self.cleaned_data['direccion']

        regex_nombre = re.compile('^[a-zA-ZÀ,\s]{3,20}$', re.IGNORECASE)
        regex_email = re.compile('^(([^<>()\[\],;:\s@"]+(\.[^<>()\[\],;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
        
        if not regex_nombre.match(nombre):
            self.add_error('first_name','Nombre debe ser mayor a 3 caracteres y a-z')

        if not regex_nombre.match(apellido):
            self.add_error('last_name','Apellido debe ser mayor a 3 caracteres y a-z')

        if not regex_email.match(correo):
            self.add_error('email','Correo inválido')

        if len(str(telefono)) < 7 or len(str(telefono)) > 11: 
            self.add_error('telefono','Teléfono deber ser entre 7 y 11 números')

        if not len(direccion) > 3:
            self.add_error('direccion','Dirección deber ser entre 3 y 50 caracteres')

        return self.cleaned_data