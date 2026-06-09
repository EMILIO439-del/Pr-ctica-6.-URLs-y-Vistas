from django.shortcuts import render
from django.http import HttpResponse

def moto(request):
    # return HttpResponse("Formulario de moto Emilio torres")
    return render(request, "moto/moto.html")