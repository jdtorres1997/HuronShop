from django.db import models

class Linea(models.Model):
    name = models.CharField("Nombre de la linea:",max_length=75)
    description = models.TextField(verbose_name="Descripción de la linea:",blank=True)

    class meta:
        ordering = ["name"]

    def __str__(self):
        return self.name + ' - ' + self.desription