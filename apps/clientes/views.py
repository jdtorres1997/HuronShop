from django.shortcuts import render, redirect
from django.contrib import messages
from apps.clientes.forms import *
from apps.clientes.models import *
from django.contrib.auth.decorators import login_required


@login_required
def gestion_clientes(request):
    # Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
    usuario = request.user
    # Validacion para cuando el administrador (is_staff)
    if usuario.is_staff: #--Revisar--
        return render(request, 'clientes/gestion.html',
                        {'clientes': Cliente.get_info()})
    # En caso de que el usuario no sea admin se redirije al home y se muestra mensaje de error
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('/clientes')

@login_required
def add_cliente(request):
    usuario = request.user
    if usuario.is_staff:
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

    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')

@login_required
def editar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    usuario = request.user

    if usuario.is_staff:
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
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('clientes:home')