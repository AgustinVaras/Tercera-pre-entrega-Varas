from django.contrib import admin
from django.urls import path
from general.views import Home, Empleados, Clientes, Libros, Escritores, Generos


urlpatterns = [
    path('', Home, name='Home'),
    path('Empleados/', Empleados, name='Empleados'),
    path('Clientes/', Clientes, name='Clientes'),
    path('Libros/', Libros, name='Libros'),
    path('Escritores/', Escritores, name='Escritores'),
    path('Generos/', Generos, name='Generos'),
]
