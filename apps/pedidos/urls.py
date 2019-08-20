from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.pedidos.views import *

app_name = 'pedidos'

urlpatterns = [
    path('', gestion_pedidos, name='gestion'),
    path('add', add_pedido, name='crear_pedido'),
    #path('edit/<int:id_pedido>', editar_pedido, name='modificar_pedido'),
    #path('delete/<int:id_pedido>', eliminar_pedido, name='eliminar_pedido'),
    path('detail/<int:id_pedido>', detail_pedido, name='detalle_pedido'),
    #path('consult', consult_pedido, name='consultar_pedido'),
]