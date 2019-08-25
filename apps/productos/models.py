from django.db import models
from apps.Lineas.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

class Producto(models.Model):

    foto = models.ImageField(upload_to = "productos/",null=True, blank=True)
    nombre = models.CharField("Nombre del producto:",max_length=75)
    linea = models.ForeignKey(
        Linea,
        on_delete= models.PROTECT,
        limit_choices_to={'active': True},
        # Usar para hacer querys con filtrso desde el modelo de lineas hasta este modelo mas info 
        # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name
        related_name="lineas", 
        related_query_name="linea", 
    )
    etiquetas = models.TextField(
        verbose_name="Etiquetas relacionadas con el producto",      
        help_text="Añade aqui las etiquetas que estan relacionadas con tu producto",
        blank=True,
        )

    precio = models.IntegerField(
            MinValueValidator(0, "El valor minimo de un producto no puede ser menor a 0"),

    )
    
    extraPueno = 'XS'
    pequeno = 'S'
    mediano = 'M'
    grande = 'L'
    SIZES_CHOICES = [
        (extraPueno, 'XS'),
        (pequeno, 'S'),
        (mediano, 'M'),
        (grande, 'L'),
    ]

    tallas = MultiSelectField(
        choices=SIZES_CHOICES,
        max_choices=4,
        max_length=50
    )
   
    REQUIRED_FIELDS = ['nombre', 'linea', 'precio', 'tallas']

    def __str__(self):
        return self.nombre + ' - ' + str(self.linea)
    
    @staticmethod
    def get_info():
        try:
            productos = Producto.objects.all().order_by('id')
            return productos
        except Producto.DoesNotExist:
            return None
    
    @staticmethod
    def get_array_productos():
        try:
            productos = list(Producto.objects.all().order_by('id').values())
            return productos
        except Producto.DoesNotExist:
            return None

Producto._meta.get_field('tallas').help_text = "Selecciona todas las opciones de tallas en las cuales este producto estara disponible"
Producto._meta.get_field('precio').help_text = "Define un valor de venta para este producto"
Producto._meta.get_field('precio').verbose_name= "precio"
Producto._meta.get_field('linea').verbose_name= "linea relacionada con el producto"



            