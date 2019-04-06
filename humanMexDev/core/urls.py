from django.urls import path

#Importar vistas del Path
from . import views

urlpatterns = [
    #Path del nucleo
    path('', views.home, name="home")
]