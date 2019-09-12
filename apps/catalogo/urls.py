from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.catalogo.views import *

app_name = 'catalogo'

urlpatterns = [
    path('login', catalogo(), name='catalogo'),
]