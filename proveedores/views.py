from django.shortcuts import render
from django.http import HttpResponse

def proveedores(request):
    # return HttpResponse("Formulario de proveedores Emilio torres")
    return render(request, "proveedores/proveedores.html")