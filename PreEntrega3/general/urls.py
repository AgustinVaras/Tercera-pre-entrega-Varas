from django.contrib import admin
from django.urls import path
from general.views import Home, Empleados, Clientes, Libros, Escritores, Generos, buscar_empleados, buscar_clientes, buscar_libros, buscar_escritores, buscar_generos


urlpatterns = [
    path('', Home, name='Home'),
    path('carga_empleados/', Empleados, name='Empleados'),
    path('carga_lientes/', Clientes, name='Clientes'),
    path('carga_ibros/', Libros, name='Libros'),
    path('carga_scritores/', Escritores, name='Escritores'),
    path('Generos/', Generos, name='Generos'),
    path('buscar.empleado/', buscar_empleados, name='buscar_empleado'),
    path('buscar.cliente/', buscar_clientes, name='buscar_cliente'),
    path('buscar.libro/', buscar_libros, name='buscar_libro'),
    path('buscar.escritor/', buscar_escritores, name='buscar_escritor'),
    path('buscar.genero', buscar_generos, name='buscar_generos'),
]
