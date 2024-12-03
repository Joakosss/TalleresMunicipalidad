from django.shortcuts import render
from . import forms

# Create your views here.
def indexAdministrador(request):
    return render(request, 'pages/index-admin.html')

def pago(request):
    return render(request, 'pages/pago.html')

def postulaciones(request):
    return render(request, 'pages/postulaciones.html')

def perfilAdmin(request):
    return render(request, 'pages/perfil-admin.html')

def Materiales(request):
    return render(request, 'pages/materiales.html')

def crearMaterial(request):
    formulario = forms.CrearMaterial()
    return render(request, 'pages/crear-material.html',{'formulario':formulario})

def solicitudesMateriales(request):
    return render(request, 'pages/solicitudes-materiales.html')

def Salas(request):
    return render(request, 'pages/salas.html')

def CrearSala(request):
    formulario = forms.CrearSala()
    return render(request, 'pages/crearSala.html',{'formulario':formulario})

def Municipalidad(request):
    return render(request, 'pages/municipalidades.html')
def CrearMunicipalidad(request):
    formulario = forms.CrearMunicipalidad()
    return render(request, 'pages/crear-municipalidad.html',{'formulario':formulario})