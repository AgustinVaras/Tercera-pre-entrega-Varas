from django.contrib import admin
from general.models import Empleado, Cliente, Autor, Genero, Libro 

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Libro)