from django.urls import path
from .import views

urlpatterns = [path("form-camion", views.camion)]
