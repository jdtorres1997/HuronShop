from django import forms
from django.forms import ModelForm
from apps.pedidos.models import *

class Pedido_form(ModelForm):
    class Meta:
        model = Pedido
        fields = ('cliente', 'direccion', 'fecha_entrega', 'estado_pedido', 'estado_pago')

    def __init__(self, *args, **kwargs):
        super(Pedido_form, self).__init__(*args, **kwargs)

        for fieldname in ['cliente', 'direccion', 'fecha_entrega', 'estado_pedido', 'estado_pago']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = ''
        #self.fields['fecha_entrega'].input_formats='%d/%m/%Y'

    def clean(self):
        pass
        #print("-----fecha-----", self.cleaned_data['fecha_entrega'])

class PedidoConsultForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ('cliente', 'direccion', 'fecha_entrega', 'estado_pedido', 'estado_pago')

    def __init__(self, *args, **kwargs):
        super(PedidoConsultForm, self).__init__(*args, **kwargs)

        for fieldname in ['cliente', 'direccion', 'fecha_entrega', 'estado_pedido', 'estado_pago']:
            self.fields[fieldname].required = False
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs['placeholder'] = ''