from django import forms
from . import models

def get_regiones():
    regiones = models.Region.objects.all()
    choices = [('', 'Seleccione una región')]  # Opción de placeholder
    choices += [(region.id, region.nombre) for region in regiones]
    return choices

class regisAdulto2(forms.Form):
    p_nombre = forms.CharField(
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese primer nombre'}),
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

class regisAdulto1(forms.Form):
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
        max_length=40,
        widget=forms.Select(attrs={'class': 'form-control'},choices=get_regiones()),
        label='Región'
    )
    comuna = forms.CharField(
        max_length=40,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Comuna'
    )
    direccion = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
        label='Dirección'
    )
"""     certificado_residencia = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='Certificado de residencia'
    ) """

class regisAdulto3(forms.Form):
    contrasenia1=forms.CharField(max_length=40)
    contrasenia2=forms.CharField(max_length=40)
    
    
"""     comuna = forms.ForeignKey('Comuna', on_delete=forms.CASCADE)
    genero = forms.ForeignKey('Genero', on_delete=forms.CASCADE)
    usuario = forms.ForeignKey('Usuario', on_delete=forms.CASCADE) """