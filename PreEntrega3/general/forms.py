from django import forms 
from phonenumber_field.formfields import PhoneNumberField
from general.models import Autor, Genero

class CargarClienteForm(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=120)
    telefono = PhoneNumberField(region="AR")

class CargarEmpleadoForm(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    nacimiento = forms.DateField()
    genero = forms.ChoiceField(
        choices=[
        ('M', 'Masculino'),
        ('F', 'Femenino')
        ], help_text="M: Masculino, F: Femenino"
    ) 

class CargarAutorForm(forms.Form):
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    nacimiento = forms.DateField()
    muerte = forms.DateField(required=False)

    
class CargarLibroForm(forms.Form):
    titulo = forms.CharField(max_length=50,)
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), empty_label="Vacio")
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(),empty_label="Vacio")
    resumen = forms.CharField(max_length=1000,widget=forms.Textarea)   



class CargarGeneroForm(forms.Form):
    nombre = forms.CharField(max_length=100, help_text="Ingrese el nombre del género (ej: Ciencia Ficción, Poesía, Fantasía, etc)")