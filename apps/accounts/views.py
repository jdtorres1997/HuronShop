from django.shortcuts import render

# Create your views here.
def home(request):
    usuario = request.user
    if usuario.is_staff:
        return render(request, 'accounts/home_admin.html', {'user': usuario})