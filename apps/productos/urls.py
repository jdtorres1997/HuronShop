from django.urls import path

from apps.productos.views import *

urlpatterns = [
    path('', Manage_products, name='manage_products'),
    path('add', Add_product, name='add_product'),  

    
]
