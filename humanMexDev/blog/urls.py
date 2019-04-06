from django.urls import path

#Importar vistas del Path
from . import views

urlpatterns = [
    #Path del nucleo
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category")
]