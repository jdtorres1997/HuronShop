from django.shortcuts import render, redirect
from django.contrib import messages
from apps.pedidos.forms import *
from apps.pedidos.models import *
from apps.productos.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Max
import json


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
			pedido = form.save(commit=False)
			#---Agregar consecutivo de venta---
			max = Pedido.objects.all().aggregate(Max('consecutivo'))
			if max['consecutivo__max'] is not None:
				pedido.consecutivo = max["consecutivo__max"] + 1
			else:
				pedido.consecutivo = 1
			pedido.no_pedido = "PED-" + str(pedido.consecutivo).zfill(5)

			pedido.save()
			mvtos = json.loads(request.POST['mvtos'])
			#mvtos = request.POST['mvtos']
			total = 0
			for mvto in mvtos:
				try:
					producto = Producto.objects.get(id=mvto['producto'])
					cantidad = mvto['cantidad'] if mvto['cantidad'] else 0
					precio = mvto['precio'] if mvto['precio'] else 0
					costo = mvto['costo'] if mvto['costo'] else 0
					register_mvto = MvtoPedido.objects.create(pedido=pedido, producto=producto, cantidad=cantidad, precio=precio,
																costo=costo)
					total += costo
					print("----Guarda mvto---", register_mvto)
				except Exception as e:
					print("Error[almacenando mvto pedido]: ", e)
			pedido.total_compra = total
			pedido.save()
			#print("----request---", mvtos)
			#print("----request---", mvtos[0])
			return redirect('pedidos:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'pedidos/add.html', {'form': form})
	else:
		form = Pedido_form()
		
		return render(request, 'pedidos/add.html',
					{'form': form, 'productos': Producto.get_array_productos()})

@login_required
def detail_pedido(request, id_pedido):
	pedido = Pedido.objects.get(id=id_pedido)
	mvtos = MvtoPedido.objects.filter(pedido=pedido).order_by('id')
	print("--mvtos--", mvtos)
	return render(request, 'pedidos/detail.html', {'pedido': pedido, 'mvtos': mvtos})