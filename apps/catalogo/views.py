from django.shortcuts import render, redirect
from django.contrib import messages
from apps.productos.models import *

def catalogo(request):
    return render(request, 'catalogo.html',
                    {'products': Producto.get_info()})
