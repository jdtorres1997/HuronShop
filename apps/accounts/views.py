from django.shortcuts import render, redirect
from django.contrib import messages
from apps.accounts.forms import *
from apps.accounts.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    usuario = request.user
    if usuario.is_staff:
        return render(request, 'accounts/home_admin.html', {'user': usuario})
    else:
        return render(request, 'accounts/home_users.html', {'user': usuario})

@login_required
def gestion_usuarios(request):
    # Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
    usuario = request.user
    # Validacion para cuando el administrador (is_staff)
    if usuario.is_staff: #--Revisar--
        return render(request, 'accounts/gestion.html',
                        {'usuarios': User.get_info()})
    # En caso de que el usuario no sea admin se redirije al home y se muestra mensaje de error
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')

@login_required
def editar_usuario(request, id_user):
    user = User.objects.get(id=id_user)
    usuario = request.user

    if usuario.is_staff:
        if request.method == 'POST':
            form = EditarUsuario(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Has modificado el usuario exitosamente!')
                return redirect('accounts:gestion')
            else:
                messages.error(request, 'Por favor corrige los errores')
                return render(request, 'accounts/edit_user.html', {'form': form})

        else:
            form = EditarUsuario(instance=user)
            return render(request, 'accounts/edit_user.html', {'form': form})
        
        return redirect('accounts:gestion')
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')

@login_required
def add_usuario(request):
    usuario = request.user
    if usuario.is_staff:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Usuario registrado exitosamente')
                user = form.save(commit=False)
                user.save()
                return redirect('accounts:gestion')
            else:
                messages.error(request, 'Por favor corrige los errores')
                return render(request, 'accounts/add.html', {'form': form})
        else:
            form = SignUpForm()
            return render(request, 'accounts/add.html',
                        {'form': form})

    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')