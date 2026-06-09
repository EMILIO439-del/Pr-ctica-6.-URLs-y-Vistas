from django.urls import path
from .import views

urlpatterns = [path ("form-auto", views.auto)]