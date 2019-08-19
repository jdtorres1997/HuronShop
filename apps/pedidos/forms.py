from django import forms
from django.forms import ModelForm
from apps.pedidos.models import *

class Pedido_form(ModelForm):
    class Meta:
        model = Pedido
        fields = ('cliente', 'direccion', 'fecha_entrega', 'estado_pedido', 'estado_pago')