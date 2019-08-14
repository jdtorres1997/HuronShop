from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import json
from apps.Lineas.forms import *
from apps.Lineas.models import *

def Add_line(request):
	if(request.method == 'POST'):
		form = Line_form(request.POST)
		if form.is_valid():
			linea = form.save()
			linea.save()
			return  redirect('/lines/')
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


def Edit_line(request, id):
	linea = Linea.objects.get(id=id)
	if request.method == 'POST':
		form = Line_form(request.POST, instance=linea)
		if form.is_valid():
			form.save()
			return redirect('/lines/')
	else:
		form = Line_form(instance=linea)
		template = loader.get_template('edit_line.html')
		context = {
			'form': form,
			'linea': linea,
		}
		return HttpResponse(template.render(context, request))

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