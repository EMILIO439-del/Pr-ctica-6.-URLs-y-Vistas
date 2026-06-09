from django.shortcuts import render
from django.http import HttpResponse

def empleados(request):
    # return HttpResponse("Formulario de empleados Emilio torres")
    return render(request, "empleados/empleados.html")