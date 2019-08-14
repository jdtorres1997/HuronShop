from django.urls import path

from apps.Lineas.views import *

urlpatterns = [
    path('line/add', Add_line, name='add_line'),
    path('line/edit/<id>', Edit_line, name='edit_line'),
    path('line/see/<id>', See_line, name='see_line'),
    path('line/consult/', Consult_line, name='consult_line'),
    path('lines/', Manage_lines, name='manage_lines'), 
]
