from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import json
from apps.productos.forms import *
from apps.productos.models import *
from django.contrib.auth.decorators import login_required


@login_required
def Add_product(request):
	if(request.method == 'POST'):
		form = Product_form(request.POST)
		if form.is_valid():
			lineas = form.save()
			lineas.save()
			return redirect('/lineas')
	else:
		form = Product_form()
		template = loader.get_template('add_product.html')
		context = {
			'form': form,
		}
		return HttpResponse(template.render(context, request))
"""
@login_required
def Manage_lines(request):
	return render(request, 'add_product.html',
					{'lineas': Productos.get_info()})
@login_required
def Edit_line(request, id):
	linea = Linea.objects.get(id=id)
	if request.method == 'POST':
		form = Line_form(request.POST, instance=linea)
		if form.is_valid():
			form.save()
			return redirect('/lineas')
	else:
		form = Line_form(instance=linea)
		template = loader.get_template('edit_line.html')
		context = {
			'form': form,
			'linea': linea,
		}
		return HttpResponse(template.render(context, request))

@login_required
def See_line(request, id):
	linea = Linea.objects.get(id=id)
	if request.method == 'GET':
		form = Line_form(instance=linea)
		template = loader.get_template('see_line.html')
		form.fields['name'].widget.attrs['disabled'] = 'disabled'
		form.fields['description'].widget.attrs['disabled'] = 'disabled'
		context = {
			'form': form,
			'linea': linea,
		}
		return HttpResponse(template.render(context, request))

@login_required
def Consult_line(request):
	if(request.method == 'POST'):
		form = Line_form(request.POST)
		form.fields['name'].required = False
		if form.is_valid():
			lineas = Linea.objects.filter(name__icontains=form.cleaned_data['name'] ,description__icontains=form.cleaned_data['description'])
			template = loader.get_template('consult_line.html')
			context = {
				'lineas': lineas,
				'metodo': request.method,
			}
			return HttpResponse(template.render(context, request))
	else:
		form = Line_form()
		template = loader.get_template('consult_line.html')
		form.fields['name'].required = False
		context = {
			'form' : form,
			'metodo': request.method,
		}
		return HttpResponse(template.render(context, request))
        """
