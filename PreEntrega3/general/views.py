from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'general/home.html')

def Empleados(request):
    return render(request, 'general/empleados.html')

def Clientes(request):
    return render(request, 'general/clientes.html')

def Libros(request):
    return render(request, 'general/libros.html')

def Escritores(request):
    return render(request, 'general/escritores.html')

def Generos(request):
    return render(request, 'general/generos.html')
