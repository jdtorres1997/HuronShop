from django.shortcuts import render, redirect
from django.contrib import messages
from apps.compras.forms import *
from apps.compras.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Max


@login_required
def gestion_compras(request):
	return render(request, 'gestion.html',
					{'compras': Compra.get_info()})

 
@login_required
def add_compra(request):
	if request.method == 'POST':
		form = Compra_form(request.POST)
		if form.is_valid():
			messages.success(request, 'pedido registrado exitosamente')
			pedido = form.save(commit=False)
			pedido.save()
			print("----request---", request.POST)
			return redirect('compras:gestion')
		else:
			messages.error(request, 'Por favor corrige los errores')
			return render(request, 'add.html', {'form': form})
	else:
		form = Compra_form()
		return render(request, 'add.html',
					{'form': form})

@login_required
def edit_compra(request, id_compra):
	compra = Compra.objects.get(id=id_compra)
	if request.method == 'POST':
		form = Compra_form(request.POST, instance=compra)
		if form.is_valid():
			form.save()
			return redirect('/compras')
		else:
			messages.error(request, 'Por favor corrige los errores')
			context = {
			'form': form,
			}
			template = loader.get_template('edit.html')
			return HttpResponse(template.render(context, request))
	else:
		form = Compra_form(instance=compra)
		template = loader.get_template('edit.html')
		context = {
			'form': form,
			'compra': compra,
		}
		return HttpResponse(template.render(context, request))


@login_required
def detail_compra(request, id_compra):
	Compras = Compra.objects.get(id=id_compra)
	if request.method == 'GET':
		template = loader.get_template('see.html')
		context = {
			'compra': Compras,
		}
		return HttpResponse(template.render(context, request))

@login_required
def consult_compra(request):
	
	if(request.method == 'POST'):
		form = Compra_consult_form(request.POST)
		
		if form.is_valid():
			compras = Compra.objects.filter(
				nombre__icontains=form.cleaned_data['nombre'],
				descripcion__icontains=form.cleaned_data['descripcion'],
				estado_compra__icontains=form.cleaned_data['estado_compra'],
				)
			template = loader.get_template('consult.html')
			context = {
				'compras': compras,
				'metodo': request.method,
			}
			return HttpResponse(template.render(context, request))
		else:
			messages.error(request, 'Por favor corrige los errores')
			context = {
			'form': form,
			}
			template = loader.get_template('edit.html')
			return HttpResponse(template.render(context, request))

	else:
		form = Compra_consult_form()

		template = loader.get_template('consult.html')
		context = {
			'form' : form,
			'metodo': request.method,
		}
		return HttpResponse(template.render(context, request))
