from django.shortcuts import render, redirect
from django.contrib import messages
from apps.clientes.forms import *
from apps.clientes.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


@login_required
def gestion_clientes(request):
	# Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
	usuario = request.user
	return render(request, 'clientes/gestion.html',
					{'clientes': Cliente.get_info()})
@login_required
def add_cliente(request):
	usuario = request.user
	if request.method == 'POST':
		form = ClienteAddForm(request.POST)
		if form.is_valid():
			messages.success(request, 'Cliente registrado exitosamente')
			user = form.save(commit=False)
			user.save()
			return redirect('clientes:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'clientes/add.html', {'form': form})
	else:
		form = ClienteAddForm()
		return render(request, 'clientes/add.html',
					{'form': form})

@login_required
def editar_cliente(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	usuario = request.user
	if request.method == 'POST':
		form = ClienteEditForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
			messages.success(request, 'Has modificado el cliente exitosamente!')
			return redirect('clientes:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'clientes/edit.html', {'form': form})

	else:
		form = ClienteEditForm(instance=cliente)
		return render(request, 'clientes/edit.html', {'form': form})
	
	return redirect('clientes:gestion')

@login_required
def eliminar_cliente(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	usuario = request.user

	if usuario.is_staff:
		if request.method == 'POST':
			
			cliente.alive = False
			cliente.save()
			messages.success(request, 'Has eliminado el cliente exitosamente!')
			return redirect('clientes:gestion')
		else:
			return render(request, 'clientes/delete.html', {'cliente': cliente})
	else:
		messages.error(request, 'No estas autorizado para realizar esta acción')
		return redirect('clientes:home')

@login_required
def detail_cliente(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	usuario = request.user
	if request.method == 'POST':
		
		#cliente.alive = False
		#cliente.save()
		messages.success(request, 'Has eliminado el cliente exitosamente!')
		return redirect('clientes:gestion')
	else:
		return render(request, 'clientes/detail.html', {'cliente': cliente})

@login_required
def consult_cliente(request):
	template = loader.get_template('clientes/consult.html')
	if(request.method == 'POST'):
		form = ClienteConsultForm(request.POST)
		if form.is_valid():
			clientes = Cliente.objects.filter(first_name__icontains=form.cleaned_data['first_name'],
											last_name__icontains=form.cleaned_data['last_name'],
											cedula__icontains=form.cleaned_data['cedula'],
											direccion__icontains=form.cleaned_data['direccion'])
			context = {
				'clientes': clientes,
				'metodo': request.method,
			}
			return HttpResponse(template.render(context, request))
	else:
		form = ClienteConsultForm()
		
		context = {
			'form' : form,
			'metodo': request.method,
		}
		return HttpResponse(template.render(context, request))