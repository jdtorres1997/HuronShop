from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telefono = models.CharField(verbose_name="Teléfono", max_length=11)
    cedula = models.CharField(verbose_name="Cédula", max_length=11, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'cedula', 'email', 'is_active', 'telefono']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.cedula + ' - ' + self.get_full_name()
    
    @staticmethod
    def get_info():
        try:
            usuarios = User.objects.all().order_by('id')
            return usuarios
        except User.DoesNotExist:
            return None

User._meta.get_field('username').verbose_name = 'Nombre de usuario'
User._meta.get_field('first_name').verbose_name = 'Nombres'
User._meta.get_field('email').verbose_name = 'Correo electrónico'
User._meta.get_field('last_name').verbose_name = 'Apellidos'
User._meta.get_field('password').verbose_name = 'Contraseña'
#User._meta.get_field('password2').verbose_name = 'Verificar contraseña'