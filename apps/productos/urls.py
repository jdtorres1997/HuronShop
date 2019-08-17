from django.urls import path

from apps.productos.views import *

urlpatterns = [
    path('', Add_product, name='manage_products'),  

    
]
