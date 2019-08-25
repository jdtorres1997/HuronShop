from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.compras.views import *

app_name = 'compras'

urlpatterns = [
    path('', gestion_compras, name='gestion'),
    path('add', add_compra, name='add'),
    path('edit/<int:id_compra>', edit_compra, name='edit'),
    path('detail/<int:id_compra>', detail_compra, name='see'),
    path('consult', consult_compra, name='consult'),
]