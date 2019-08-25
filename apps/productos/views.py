from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.contrib import messages
from apps.productos.forms import *
from apps.productos.models import *
from apps.Lineas.models import *
from django.contrib.auth.decorators import login_required


@login_required
def Add_product(request):
	if(request.method == 'POST'):
		form = Product_form(request.POST, request.FILES)
		if form.is_valid():
			productos = form.save()
			productos.save()
			return redirect('/productos')
		else:
			messages.error(request, 'Por favor corrige los errores')
			context = {
			'form': form,
			}
			template = loader.get_template('add_product.html')
			return HttpResponse(template.render(context, request))
	else:
		
		form = Product_form()
		template = loader.get_template('add_product.html')
		context = {
			'form': form,
		}
		return HttpResponse(template.render(context, request))


@login_required
def Manage_products(request):
	
	return render(request, 'gestion_product.html',
					{'products': Producto.get_info()})

@login_required
def Edit_product(request, id):
	producto = Producto.objects.get(id=id)
	if request.method == 'POST':
		form = Product_form(request.POST, request.FILES, instance=producto)
		print(form.fields['tallas'])
		if form.is_valid():
			form.save()
			return redirect('/productos')
		else:
			messages.error(request, 'Por favor corrige los errores')
			context = {
			'form': form,
			}
			template = loader.get_template('edit_product.html')
			return HttpResponse(template.render(context, request))
	else:
		form = Product_form(instance=producto)
		template = loader.get_template('edit_product.html')
		context = {
			'form': form,
			'producto': producto,
		}
		return HttpResponse(template.render(context, request))

@login_required
def See_product(request, id):
	producto = Producto.objects.get(id=id)
	if request.method == 'GET':
		template = loader.get_template('see_product.html')
		tallas = str(producto.tallas).split(',')
		context = {
			'producto': producto,
			'tallas': tallas,
		}
		return HttpResponse(template.render(context, request))

@login_required
def Consult_product(request):
	
	if(request.method == 'POST'):
		form = Product_form(request.POST)
		form.fields['nombre'].required = False
		form.fields['linea'].required = False
		form.fields['precio'].required = False
		form.fields['tallas'].required = False
		if form.is_valid():

			nombre_linea = "" if not form.cleaned_data['linea'] else form.cleaned_data['linea']
			
			productos = Producto.objects.filter(
				nombre__icontains=form.cleaned_data['nombre'],
				linea__name__icontains = nombre_linea,
				etiquetas__icontains=form.cleaned_data['etiquetas'] ,
				)
			busqueda = Producto.objects.none()
			if form.cleaned_data['tallas'] :
				for t in form.cleaned_data['tallas']:
					busqueda_por_tallas = Producto.objects.filter(
						tallas__icontains =  t
					)
					busqueda = busqueda.union(busqueda_por_tallas)

			productos = productos & busqueda
			
			template = loader.get_template('consult_product.html')
			context = {
				'products': productos,
				'metodo': request.method,
			}
			return HttpResponse(template.render(context, request))
	else:
		form = Product_form()
		form.fields['nombre'].required = False
		form.fields['linea'].required = False
		form.fields['precio'].required = False
		form.fields['tallas'].required = False
		template = loader.get_template('consult_product.html')
		context = {
			'form' : form,
			'metodo': request.method,
		}
		return HttpResponse(template.render(context, request))
