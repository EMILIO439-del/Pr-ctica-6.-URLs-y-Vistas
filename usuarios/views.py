from django.shortcuts import render
from django.http import HttpResponse

def usuarios(request):
    # return HttpResponse("Formulario de usuarios Emilio torres")
    return render(request, "usuarios/usuarios.html")
