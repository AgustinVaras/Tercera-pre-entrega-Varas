from django import forms 
from phonenumber_field.formfields import PhoneNumberField

class CargarClienteForm(forms.Form):
    dni = forms.IntegerField()
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=120)
    telefono = PhoneNumberField(region="AR")
