from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.clientes.views import *

app_name = 'clientes'

urlpatterns = [
    path('', gestion_clientes, name='gestion'),
    path('add', add_cliente, name='crear_cliente'),
    path('edit/<int:id_cliente>', editar_cliente, name='modificar_cliente'),
]