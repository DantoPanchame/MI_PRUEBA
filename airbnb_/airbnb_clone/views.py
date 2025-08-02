from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    if request.user.is_authenticated:
        return render(request, "home.html", {"user": request.user})
    else:
        return HttpResponse("<h1>No estás logueado</h1><br><a href='/usuarios/login/'>Ir a login</a>")

def inicio_registro(request):
    return render(request, 'usuarios/inicio_registro.html')