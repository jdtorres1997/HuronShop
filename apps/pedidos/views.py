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

			#---Guardar mvtos pedido---
			mvtos = json.loads(request.POST['mvtos'])
			#mvtos = request.POST['mvtos']
			total = 0
			for mvto in mvtos:
				try:
					producto = Producto.objects.get(id=mvto['producto_id'])
					cantidad = mvto['cantidad'] if mvto['cantidad'] else 0
					precio = mvto['precio'] if mvto['precio'] else 0
					costo = mvto['costo'] if mvto['costo'] else 0
					talla = mvto['talla'] if mvto['talla'] else ''
					color = mvto['color'] if mvto['color'] else ''
					register_mvto = MvtoPedido.objects.create(pedido=pedido, producto=producto, cantidad=cantidad, precio=precio,
																costo=costo, talla=talla, color=color)
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
	return render(request, 'pedidos/detail.html', {'pedido': pedido, 'mvtos': mvtos})

@login_required
def consult_pedido(request):
	template = loader.get_template('pedidos/consult.html')
	if(request.method == 'POST'):
		form = PedidoConsultForm(request.POST)
		if form.is_valid():
			cliente = form.cleaned_data['cliente'] if form.cleaned_data['cliente'] else ''
			if cliente: 
				cedula_cliente = cliente.cedula
			else:
				cedula_cliente = ''
			print("cedula_cliente", cedula_cliente)
			pedidos = Pedido.objects.filter(direccion__icontains=form.cleaned_data['direccion'],
											cliente__cedula__icontains=cedula_cliente)
			if form.cleaned_data['estado_pedido']:
				pedidos = pedidos.filter(estado_pedido=form.cleaned_data['estado_pedido'])
			if form.cleaned_data['estado_pago']:
				pedidos = pedidos.filter(estado_pago=form.cleaned_data['estado_pago'])
			if form.cleaned_data['fecha_entrega']:
				pedidos = pedidos.filter(fecha_entrega=form.cleaned_data['fecha_entrega'])
			context = {
				'pedidos': pedidos,
				'metodo': request.method,
			}
			return HttpResponse(template.render(context, request))
	else:
		form = PedidoConsultForm()
		
		context = {
			'form' : form,
			'metodo': request.method,
		}
		return HttpResponse(template.render(context, request))

@login_required
def editar_pedido(request, id_pedido):
	pedido = Pedido.objects.get(id=id_pedido)
	if request.method == 'POST':
		form = Pedido_form(request.POST, instance=pedido)
		if form.is_valid():
			pedido = form.save(commit=False)
			pedido.save()
			mvtos = json.loads(request.POST['mvtos'])
			mvtos_deleted = json.loads(request.POST['mvtos_eliminados_pedido'])
			print("---mvtos---", mvtos)
			total = 0
			for mvto in mvtos:
				try:
					producto = Producto.objects.get(id=mvto['producto_id'])
					cantidad = mvto['cantidad'] if mvto['cantidad'] else 0
					precio = mvto['precio'] if mvto['precio'] else 0
					costo = mvto['costo'] if mvto['costo'] else 0
					talla = mvto['talla'] if mvto['talla'] else ''
					color = mvto['color'] if mvto['color'] else ''
					if mvto['id'] == 0:
						register_mvto = MvtoPedido.objects.create(pedido=pedido, producto=producto, cantidad=cantidad, precio=precio,
																costo=costo, talla=talla, color=color)
					elif mvto['id']:
						register_mvto = MvtoPedido.objects.filter(id=mvto['id']).update(pedido=pedido, producto=producto,
																cantidad=cantidad, precio=precio, costo=costo, talla=talla, color=color)
					total += costo
					print("----Guarda mvto---", register_mvto)
				except Exception as e:
					print("Error[almacenando mvto pedido]: ", e)
			for item in mvtos_deleted:
				try:
					pedido_mvto = MvtoPedido.objects.get(id=str(item))
					if pedido_mvto:
						pedido_mvto.delete()
				except Exception as e:
					print("Error[eliminando mvto pedido]: ", e)
			pedido.total_compra = total
			pedido.save()
			messages.success(request, 'Has modificado el pedido exitosamente!')
			return redirect('pedidos:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'pedidos/edit.html', {'form': form})

	else:
		form = Pedido_form(instance=pedido)
		mvtos = list(MvtoPedido.objects.filter(pedido=pedido).order_by('id').values())
		return render(request, 'pedidos/edit.html', {'pedido': pedido, 'form': form, 'mvtos': json.dumps(mvtos), 'productos': Producto.get_array_productos()})
	
	return redirect('pedidos:gestion')