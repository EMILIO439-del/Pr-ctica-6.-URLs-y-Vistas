from django.shortcuts import render
from django.http import HttpResponse

def camion(request):
    # return HttpResponse("Formulario de camion Emilio torres")
    return render(request, "camion/camion.html")