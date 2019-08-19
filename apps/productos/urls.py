from django.urls import path

from apps.productos.views import *

app_name = 'productos'

urlpatterns = [
    path('', Manage_products, name='manage'),
    path('add', Add_product, name='add'),
    path('see/<id>', See_product, name='see'),  
    path('edit/<id>', Edit_product, name='edit'),
    path('consult/', Consult_product, name='consult'),

    
]
