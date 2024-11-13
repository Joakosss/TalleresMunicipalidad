from django import forms
from . import models

def get_regiones():
    regiones = models.Region.objects.all()
    choices = [('', 'Seleccione una región')]  # Opción de placeholder
    choices += [(region.id, region.nombre) for region in regiones]
    return choices

""" def get_comunas(region_id):
    comunas =
 """
def get_genero():
    generos = models.Genero.objects.all()
    choices = [('', 'Seleccione un genero')]  # Opción de placeholder
    choices += [(genero.id, genero.nombre) for genero in generos]
    return choices
    
class regisAdulto1(forms.Form):
    p_nombre = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese primer nombre'
            }
        ),
        label='Primer nombre'
    )
    s_nombre = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese segundo nombre'}),
        label='Segundo nombre'
    )
    p_apellido = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese primer apellido'}),
        label='Primer apellido'
    )
    s_apellido = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese segundo apellido'}),
        label='Segundo apellido'
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Fecha de nacimiento'
    )
    genero = forms.CharField(
        widget=forms.Select(attrs={'class': 'form-control'},choices=get_genero()),
        label='Genero'
    )

class regisAdulto2(forms.Form):
    rut_adulto_mayor = forms.CharField(
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su rut sin puntos ni guion'}),
        label='Rut'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        label='Correo electrónico'
    )
    region = forms.CharField(
        widget=forms.Select(attrs={'class': 'form-control'},choices=get_regiones()),
        label='Región'
    )
    comuna = forms.CharField(
        widget=forms.Select(attrs={'class': 'form-control col-3 col-md-3', 'disabled': 'disabled'},choices=[('', 'Seleccione una comuna')]),
        label='Comuna'
    )
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control col-3 col-md-3', 'placeholder': 'Ingrese su dirección' , 'disabled': 'disabled'}),
        label='Dirección'
    )
"""     certificado_residencia = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='Certificado de residencia'
    ) """

class regisAdulto3(forms.Form):
    contrasenia1=forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}), label='Contraseña')
    contrasenia2=forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita su contraseña'}), label='')
