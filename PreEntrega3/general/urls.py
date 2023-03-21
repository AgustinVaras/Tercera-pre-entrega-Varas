from django.contrib import admin
from django.urls import path
from general.views import Home, carga_empleados, carga_clientes, carga_libros, carga_escritores, carga_generos, buscar_empleados, buscar_clientes, buscar_libros, buscar_escritores, buscar_generos


urlpatterns = [
    path('', Home, name='Home'),
    path('carga_empleados/', carga_empleados, name='Empleados'),
    path('carga_clientes/', carga_clientes, name='Clientes'),
    path('carga_libros/', carga_libros, name='Libros'),
    path('carga_escritores/', carga_escritores, name='Escritores'),
    path('carga_generos/', carga_generos, name='Generos'),
    path('buscar.empleado/', buscar_empleados, name='buscar_empleado'),
    path('buscar.cliente/', buscar_clientes, name='buscar_cliente'),
    path('buscar.libro/', buscar_libros, name='buscar_libro'),
    path('buscar.escritor/', buscar_escritores, name='buscar_escritor'),
    path('buscar.genero', buscar_generos, name='buscar_generos'),
]
