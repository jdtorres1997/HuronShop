from django.shortcuts import render, redirect
from django.contrib import messages
from apps.accounts.forms import *
from apps.accounts.models import *

# Create your views here.
def home(request):
    usuario = request.user
    if usuario.is_staff:
        return render(request, 'accounts/home_admin.html', {'user': usuario})

def signup(request):
    # Usuario que hizo la peticion a la funcion (usuario que esta en la sesion)
    usuario = request.user
    # Validacion para cuando el administrador (is_staff)
    if usuario.is_staff or True: #--Revisar--
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Usuario registrado exitosamente')
                user = form.save(commit=False)
                user.save()
                return redirect('accounts:registro')
            else:
                messages.error(request, 'Por favor corrige los errores')
                return render(request, 'accounts/signup.html', {'form': form, 'usuarios': User.get_info()})
        else:
            form = SignUpForm()
            return render(request, 'accounts/signup.html',
                        {'form': form, 'usuarios': User.get_info()})
    # En caso de que el usuario no sea admin se redirije al home y se muestra mensaje de error
    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')

def editar_usuario(request, id_user):
    user = User.objects.get(id=id_user)
    usuario = request.user

    if usuario.is_staff:
        if request.method == 'POST':
            return redirect('accounts:registro')

        else:
            return redirect('accounts:registro')

    else:
        messages.error(request, 'No estas autorizado para realizar esta acción')
        return redirect('accounts:home')