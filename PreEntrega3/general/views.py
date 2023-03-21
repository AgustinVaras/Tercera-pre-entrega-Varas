from django.shortcuts import render
from django.http import HttpResponse
from general.models import Cliente, Empleado, Libro, Autor, Genero
from general.forms import CargarClienteForm, CargarEmpleadoForm, CargarAutorForm, CargarLibroForm, CargarGeneroForm

# Create your views here.
def Home(request):
    return render(request, 'general/home.html')

def carga_empleados(request):
    if request.method == "POST":
        
        miformulario = CargarEmpleadoForm(request.POST)

        if miformulario.is_valid():
            info = miformulario.cleaned_data
            empleado = Empleado(
                dni = info["dni"],
                nombre= info["nombre"],
                apellido= info["apellido"],
                nacimiento= info["nacimiento"],
                genero= info["genero"],
            )
            empleado.save()
            return render(request, "general/home.html")
    else:
        miformulario = CargarEmpleadoForm()

    return render(request, "general/carga_empleados.html", {"miformulario": miformulario})

def carga_clientes(request):

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

def carga_libros(request):
    if request.method == "POST":
        
        miformulario = CargarLibroForm(request.POST)

        if miformulario.is_valid():
            info = miformulario.cleaned_data
            libro = Libro(
                titulo = info["titulo"],
                autor= info["autor"],
                genero= info["genero"],
                resumen= info["resumen"]
            )
            libro.save()
            return render(request, "general/home.html")
    else:
        miformulario = CargarLibroForm()

    return render(request, "general/carga_libros.html", {"miformulario": miformulario})

def carga_escritores(request):
    if request.method == "POST":
        
        miformulario = CargarAutorForm(request.POST)

        if miformulario.is_valid():
            info = miformulario.cleaned_data
            autor = Autor(
                nombre = info["nombre"],
                apellido= info["apellido"],
                nacimiento= info["nacimiento"],
                muerte= info["muerte"]
            )
            autor.save()
            return render(request, "general/home.html")
    else:
        miformulario = CargarAutorForm()

    return render(request, "general/carga_escritores.html", {"miformulario": miformulario})

def carga_generos(request):
    if request.method == "POST":
        
        miformulario = CargarGeneroForm(request.POST)

        if miformulario.is_valid():
            info = miformulario.cleaned_data
            genero = Genero(
                nombre = info["nombre"]
            )
            genero.save()
            return render(request, "general/home.html")
    else:
        miformulario = CargarGeneroForm()

    return render(request, "general/carga_generos.html", {"miformulario": miformulario})


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