from django.shortcuts import render, redirect
from django.contrib import messages
from apps.pedidos.forms import *
from apps.pedidos.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


@login_required
def gestion_pedidos(request):
	# Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
	usuario = request.user
	return render(request, 'pedidos/gestion.html',
					{'pedidos': Pedido.get_info()})

@login_required
def add_pedido(request):
	usuario = request.user
	if request.method == 'POST':
		form = Pedido_form(request.POST)
		if form.is_valid():
			messages.success(request, 'pedido registrado exitosamente')
			user = form.save(commit=False)
			user.save()
			return redirect('pedidos:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'pedidos/add.html', {'form': form})
	else:
		form = Pedido_form()
		return render(request, 'pedidos/add.html',
					{'form': form})