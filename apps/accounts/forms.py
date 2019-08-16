from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_select2.forms import Select2Widget
from apps.accounts.models import *
from django import forms
import re

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'cedula', 'username', 'email', 'password1', 'password2',
                  'telefono')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['first_name', 'last_name', 'cedula', 'username', 'email', 'password1', 'password2',
                  'telefono']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = ''

    def clean(self):
        nombre = self.cleaned_data['first_name']
        apellido = self.cleaned_data['last_name']
        cedula = self.cleaned_data['cedula']
        correo = self.cleaned_data['email']
        telefono = self.cleaned_data['telefono']
        username = self.cleaned_data['username']

        regex_nombre = re.compile('^[a-zA-ZÀ,\s]{3,20}$', re.IGNORECASE)
        regex_cedula = re.compile('^[0-9]{8,11}$')
        regex_email = re.compile('^(([^<>()\[\],;:\s@"]+(\.[^<>()\[\],;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
        regex_telefono = re.compile('^[0-9]{7,11}$')

        u = User.objects.filter(username=username).count()

        c = User.objects.filter(cedula=cedula).count()

        if not regex_nombre.match(nombre):
            self.add_error('first_name','Nombre debe ser mayor a 3 caracteres y a-z')

        if not regex_nombre.match(apellido):
            self.add_error('last_name','Apellido debe ser mayor a 3 caracteres y a-z')

        if not regex_email.match(correo):
            self.add_error('email','Correo inválido')

        if not regex_telefono.match(telefono):
            self.add_error('telefono','Teléfono deber ser entre 7 y 11 números')

        if not u == 0:
            self.add_error('username', 'Nombre de usuario no disponible')

        if not c == 0:
            self.add_error('cedula', 'Cedula ya registrada')
        else:
            if not regex_cedula.match(cedula):
                self.add_error('cedula','Cédula debe ser numérica entre 8 y 11 números')


        return self.cleaned_data

class EditarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'telefono', 'is_active')

    def clean(self):
        nombre = self.cleaned_data['first_name']
        apellido = self.cleaned_data['last_name']
        correo = self.cleaned_data['email']
        telefono = self.cleaned_data['telefono']

        regex_nombre = re.compile('^[a-zA-ZÀ,\s]{3,20}$', re.IGNORECASE)
        regex_email = re.compile('^(([^<>()\[\],;:\s@"]+(\.[^<>()\[\],;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
        regex_telefono = re.compile('^[0-9]{7,11}$')

        if not regex_nombre.match(nombre):
            self.add_error('first_name','Nombre debe ser mayor a 3 caracteres y a-z')

        if not regex_nombre.match(apellido):
            self.add_error('last_name','Apellido debe ser mayor a 3 caracteres y a-z')

        if not regex_email.match(correo):
            self.add_error('email','Correo inválido')

        if not regex_telefono.match(telefono):
            self.add_error('telefono','Teléfono deber ser entre 7 y 11 números')

        return self.cleaned_data