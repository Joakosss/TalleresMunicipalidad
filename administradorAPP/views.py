from django.shortcuts import render

# Create your views here.
def indexAdministrador(request):
    return render(request, 'pages/index-admin.html')

def pago(request):
    return render(request, 'pages/pago.html')

def postulaciones(request):
    return render(request, 'pages/postulaciones.html')

def perfilAdmin(request):
    return render(request, 'pages/perfil-admin.html')