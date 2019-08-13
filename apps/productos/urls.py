from django.urls import path

from apps.productos.views import *

app_name = 'productos'

urlpatterns = [
    path('line/add', Add_line, name='add_line'),
    path('line/edit/<int:id>', Edit_line, name='add_line'),
    path('lines/', Manage_lines, name='manage_lines'),
    
]
