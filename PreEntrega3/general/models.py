from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Persona():
    dni = models.IntegerField(unique=True, null=False, blank=False,)
    nombre = models.CharField(max_length=25, null=False, blank=False)
    apellido = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido}"
    
class Empleado(models.Model, Persona):
    id = models.AutoField(primary_key=True)
    nacimiento = models.DateField(null=False , blank=False ,help_text="Fecha de Nacimiento")
    genero = models.CharField(
        max_length=1, 
        choices=[
        ('M', 'Masculino'),
        ('F', 'Femenino')
        ], 
        help_text="M: Masculino, F: Femenino"
    )

    def __str__(self) -> str:
        return f"{self.id} - {super().__str__()}" 
    
class Cliente(models.Model, Persona):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=120, null=False, blank=False, unique=True)
    telefono = PhoneNumberField(blank=True, region="AR")

    def __str__(self) -> str:
        return f"{self.id} - {super().__str__()}"


class autores(models.Model, Persona):
    nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    muerte = models.DateField('Fallecido', null=True, blank=True)

    def __str__(self) -> str:
        return super().__str__()


class generos(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el nombre del género (ej: Ciencia Ficción, Poesía, Fantasía, etc)")

    def __str__(self) -> str:
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, unique=True)
    autor = models.ForeignKey(autores, on_delete=models.CASCADE)
    genero = models.ManyToManyField(generos, help_text="Seleccione un genero para el libro")
    resumen = models.TextField(max_length=1000, help_text="Ingrese un breve resumen del libro")

    def __str__(self) -> str:
        return self.titulo



