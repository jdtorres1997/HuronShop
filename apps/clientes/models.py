from django.db import models

class Cliente(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cedula = models.CharField(max_length=11, unique=True)
    telefono = models.BigIntegerField(default=0)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    alive = models.BooleanField(default=True)

    def __str__(self):
        return self.cedula + ' - ' + self.first_name + ' ' + self.last_name

    @staticmethod
    def get_info():
        try:
            usuarios = Cliente.objects.filter(alive=True).order_by('id')
            return usuarios
        except Cliente.DoesNotExist:
            return None