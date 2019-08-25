from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Compra(models.Model):
    nombre = models.CharField("Nombre del producto a comprar:",max_length=75, unique=True)
    descripcion = models.TextField(verbose_name="Motivo de compra:",blank=True)
    ESTADO_COMPRA_CHOICES = [
        ('En proceso', 'En proceso'),
        ('Pago', 'Pago'),
    ]
    estado_compra = models.CharField(
        max_length=10,
        choices=ESTADO_COMPRA_CHOICES,
        default='',
    )
    precio = models.IntegerField(
            MinValueValidator(0, "El valor minimo de una compra no puede ser menor a 0"),
            default= 0,
    )
    cantidad = models.IntegerField(
            MinValueValidator(0, "Debes comprar al menos un producto"),
            default= 0,

    )
    precio_total = models.IntegerField(
            MinValueValidator(0, "El valor minimo de una compra no puede ser menor a 0"),
            default= 0,
    )
    REQUIRED_FIELDS = ['nombre', 'precio', 'cantidad']
    class meta:
        ordering = ["id"]

    def __str__(self):
        return self.nombre

    @staticmethod
    def get_info():
        try:
            compras = Compra.objects.all().order_by('id')
            return compras
        except Compra.DoesNotExist:
            return None

Compra._meta.get_field('nombre').help_text = "El nombre de la linea no puede estar vacio ni sobre pasar el limite de 75 carcteres"
Compra._meta.get_field('precio').help_text = "Ingrsa el precio individual de cada producto"
Compra._meta.get_field('precio').verbose_name = "Precio individual del producto:"
Compra._meta.get_field('cantidad').verbose_name= "Cantidad a comprar:"
Compra._meta.get_field('precio_total').verbose_name= "Precio total de la compra:"
