from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.Lineas.models import *

"""
class Productos(models.Model):

    foto = models.ImageField(
        upload_to='media', verbose_name="Imagenes de Muestra:")
    name = models.CharField("Nombre del producto:",max_length=75)
    linea = models.ForeignKey(
        Linea,
        on_delete= models.PROTECT,
        limit_choices_to={'active': True},
        # Usar para hacer querys con filtrso desde el modelo de lineas hasta este modelo mas info 
        # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name
        related_name="lineas", 
        related_query_name="linea", 
        to_field='name'
    )
    #etiquetas = models.



    cedula = models.CharField(verbose_name="Cédula", max_length=11, unique=True)



    telefono = models.CharField(verbose_name="Teléfono", max_length=11)
    cedula = models.CharField(verbose_name="Cédula", max_length=11, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'cedula', 'email', 'is_active', 'telefono']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.cedula + ' - ' + self.get_full_name()
    
    @staticmethod
    def get_info():
        try:
            usuarios = Productos.objects.all().order_by('id')
            return usuarios
        except Productos.DoesNotExist:
            return None
"""