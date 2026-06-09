from django.shortcuts import render
from django.http import HttpResponse

def productos(request):
    # return HttpResponse("Formulario de productos Emilio torres")
    return render(request, "productos/productos.html")