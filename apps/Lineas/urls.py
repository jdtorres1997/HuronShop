from django.urls import path

from apps.Lineas.views import *

app_name = 'lineas'

urlpatterns = [
    path('', Manage_lines, name='manage'),  
    path('add', Add_line, name='add'),
    path('edit/<id>', Edit_line, name='edit'),
    path('see/<id>', See_line, name='see'),
    path('consult', Consult_line, name='consult'),
]
