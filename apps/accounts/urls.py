from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True,
                    template_name='accounts/login.html'), name='login'),
    path('home', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios', gestion_usuarios, name='gestion'),
    path('usuarios/add', add_usuario, name='crear_usuario'),
    path('usuarios/edit/<int:id_user>', editar_usuario, name='modificar_usuario'),
]