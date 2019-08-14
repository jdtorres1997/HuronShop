from django.urls import path

from apps.Lineas.views import *

urlpatterns = [
    path('', Manage_lines, name='manage_lines'),  
    path('add', Add_line, name='add_line'),
    path('edit/<id>', Edit_line, name='edit_line'),
    path('see/<id>', See_line, name='see_line'),
    path('consult', Consult_line, name='consult_line'),
]
