from django.db import models

class Linea(models.Model):
    name = models.CharField("Nombre de la linea:",max_length=75, unique=True)
    description = models.TextField(verbose_name="Descripción de la linea:",blank=True)
    active = models.BooleanField(
        default=True,
        help_text=(
            'Desiga si la Linea se encuentra activa en el sistema'
        ),
    )

    class meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + '.'

    @staticmethod
    def get_info():
        try:
            lineas = Linea.objects.all().order_by('id')
            return lineas
        except Linea.DoesNotExist:
            return None

Linea._meta.get_field('name').help_text = "El nombre de la linea no puede estar vacio ni sobre pasar el limite de 75 carcteres"
Linea._meta.get_field('name').blank = False