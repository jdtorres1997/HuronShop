from django.db import models

class Cliente(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cedula = models.CharField(max_length=11, unique=True)
    telefono = models.IntegerField(default=0)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.cedula + ' - ' + self.first_name + ' ' + self.last_name