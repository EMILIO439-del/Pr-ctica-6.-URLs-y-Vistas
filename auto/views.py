from django.shortcuts import render
from django.http import HttpResponse

def auto(request):
    # return HttpResponse("Formulario de auto Emilio torres")
    return render(request, "auto/auto.html")        