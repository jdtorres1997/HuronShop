from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import json
from apps.productos.forms import *
from apps.productos.models import *

def Add_line(request):
	if(request.method == 'POST'):
		form = Line_form(request.POST)
		if form.is_valid():
			linea = form.save()
			linea.save()
			return  redirect('/productos/lines/')
	else:
		form = Line_form()
		template = loader.get_template('Addline.html')
		context = {
			'form' : form,
		}
		return HttpResponse(template.render(context, request))


def Manage_lines(request):
	lineas = Linea.objects.order_by('id')
	template = loader.get_template('manage_lines.html')
	context = {
		'lineas': lineas,
	}
	return HttpResponse(template.render(context, request))


def Edit_line(request, ide):
	linea = Linea.objects.get(id=ide)
	if request.method == 'POST':
		lineas = Linea.objects.get(id=ide)
		template = loader.get_template('edit_line.html')
		context = {
			'linea': linea,
		}
		return HttpResponse(template.render(context, request))
	else:
		form = Line_form(instance=linea)
		lineas = Linea.objects.get(id=ide)
		template = loader.get_template('edit_line.html')
		context = {
			'form': form,
			'linea': linea,
		}
		return HttpResponse(template.render(context, request))