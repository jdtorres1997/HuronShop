from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telefono = models.CharField(max_length=11)
    cedula = models.CharField(max_length=11, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'cedula', 'email', 'is_active', 'telefono']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.cedula + ' - ' + self.get_full_name()
