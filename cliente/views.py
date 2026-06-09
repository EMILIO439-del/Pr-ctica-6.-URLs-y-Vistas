from django.shortcuts import render
from django.http import HttpResponse

def cliente(request):
    # return HttpResponse("Formulario de cliente Emilio torres")
    return render(request, "cliente/cliente.html")