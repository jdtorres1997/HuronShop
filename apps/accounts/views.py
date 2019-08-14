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
        '''
        if request.method == 'POST':
            form = EditarEmpleado(request.POST, instance=user)
            form_empleado = FormEmpleado(request.POST, instance=empleado)
            form_empleado_extra = EditarEmpleadoExtra(request.POST, instance=user)
            if form.is_valid() and form_empleado.is_valid() and form_empleado_extra.is_valid():
                form.save()
                form_empleado.save()
                form_empleado_extra.save()
                messages.success(request, 'Has modificado el empleado exitosamente!')
                return redirect('accounts:registro')
            else:
                messages.error(request, 'Por favor corrige los errores')
                return render(request, 'accounts/editar_empleado.html', {'form': form, 'form_empleado': form_empleado,
                                                                         'form_empleado_extra': form_empleado_extra})

        else:
            form = EditarEmpleado(instance=user)
            form_empleado = FormEmpleado(instance=empleado)
            form_empleado_extra = EditarEmpleadoExtra(instance=user)
            return render(request, 'accounts/editar_empleado.html', {'form': form, 'form_empleado': form_empleado,
                                                                     'form_empleado_extra': form_empleado_extra})
        '''
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