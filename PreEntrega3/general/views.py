from django.shortcuts import render
from django.http import HttpResponse
from general.models import Cliente
from general.forms import CargarClienteForm

# Create your views here.
def Home(request):
    return render(request, 'general/home.html')

def Empleados(request):
    return render(request, 'general/carga_empleados.html')

def Clientes(request):

    if request.method == "POST":
        
        miformulario = CargarClienteForm(request.POST)

        if miformulario.is_valid():
            info = miformulario.cleaned_data
            cliente = Cliente(
                dni = info["dni"],
                nombre= info["nombre"],
                apellido= info["apellido"],
                email= info["email"],
                telefono= info["telefono"],
            )
            cliente.save()
            return render(request, "general/home.html")
    else:
        miformulario = CargarClienteForm()

    return render(request, "general/carga_clientes.html", {"miformulario": miformulario})

def Libros(request):
    return render(request, 'general/carga_libros.html')

def Escritores(request):
    return render(request, 'general/carga_escritores.html')

def Generos(request):
    return render(request, 'general/carga_generos.html')


#Views Formularios
def buscar_empleados(request):
    return render(request, 'general/empleados.html')

def buscar_clientes(request):
    return render(request, 'general/clientes.html')

def buscar_libros(request):
    return render(request, 'general/libros.html')

def buscar_escritores(request):
    return render(request, 'general/escritores.html')

def buscar_generos(request):
    return render(request, 'general/generos.html')