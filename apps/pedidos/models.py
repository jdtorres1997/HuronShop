from django.db import models
from apps.clientes.models import *
from apps.productos.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Pedido(models.Model):

    consecutivo = models.IntegerField(default=0)
    no_pedido = models.CharField(verbose_name="Numero de pedido", max_length=20)
    direccion = models.CharField(verbose_name="Dirección de entrega", max_length=75)
    fecha_entrega = models.DateField(verbose_name="Fecha de entrega")
    cliente = models.ForeignKey(
        Cliente,
        on_delete= models.PROTECT,
        limit_choices_to={'alive': True},
        # Usar para hacer querys con filtro desde el modelo de clientes
        # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name
        related_name="clientes", 
        related_query_name="cliente", 
    )

    #total_compra = models.IntegerField(MinValueValidator(0, "El valor minimo de un producto no puede ser menor a 0"))
    total_compra = models.IntegerField(null=True)

    ESTADO_PEDIDO_CHOICES = [
        ('', ''),
        ('En proceso', 'En proceso'),
        ('Listo', 'Listo'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]
    estado_pedido = models.CharField(
        max_length=10,
        choices=ESTADO_PEDIDO_CHOICES,
        default='',
    )
    ESTADO_PAGO_CHOICES = [
        ('', ''),
        ('No pagado', 'No pagado'),
        ('Pagado', 'Pagado'),
    ]
    estado_pago = models.CharField(
        max_length=10,
        choices=ESTADO_PAGO_CHOICES,
        default='',
    )
    REQUIRED_FIELDS = ['direccion', 'cliente']

    def __str__(self):
        return self.no_pedido
    
    @staticmethod
    def get_info():
        try:
            productos = Pedido.objects.all().order_by('consecutivo')
            return productos
        except Pedido.DoesNotExist:
            return None

class MvtoPedido(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete= models.PROTECT,
        # Usar para hacer querys con filtro desde el modelo de clientes
        # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name
        related_name="productos", 
        related_query_name="producto", 
    )
    pedido = models.ForeignKey(
        Pedido,
        on_delete= models.PROTECT,
        # Usar para hacer querys con filtro desde el modelo de clientes
        # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.related_query_name
        related_name="pedidos", 
        related_query_name="pedido", 
    )
    cantidad = models.IntegerField(default=0)
    costo = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    SIZES_CHOICES = [
        ('', ''),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    ]
    talla = models.CharField(
        max_length=2,
        choices=SIZES_CHOICES,
        default='',
    )
    color = models.CharField(verbose_name="Color", max_length=50, default='')