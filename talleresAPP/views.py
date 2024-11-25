from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout,login as auth_login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from . import models
import json
# Create your views here.

loginURL= 'pages/login.html'

def logear(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        print(usuario, contrasena)
        us = authenticate(request, username=usuario, password=contrasena)
        if us is not None and us.is_active:
            auth_login(request, us)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')
            return render(request, loginURL)
    return render(request, loginURL)

@login_required(login_url="login")
def desconectar(request):
    logout(request)
    return redirect('login')

def registro(request): 
    if request.method == 'POST':
        rut_adulto_mayor = request.POST.get('rut_adulto_mayor')
        p_nombre = request.POST.get('p_nombre')
        s_nombre = request.POST.get('s_nombre')
        p_apellido = request.POST.get('p_apellido')
        s_apellido = request.POST.get('s_apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        comuna = request.POST.get('comuna')
        genero = request.POST.get('genero')
        contrasenia1 = request.POST.get('contrasenia1')
        
        if User.objects.filter(username=rut_adulto_mayor).exists():
            messages.error(request, 'El usuario ya existe')
            return redirect('login')
        try:
           
            user = User.objects.create_user(username=rut_adulto_mayor, password=contrasenia1)
            get_comunas = models.Comuna.objects.get(id=comuna)
            get_genero = models.Genero.objects.get(id=genero)
            adulto = models.AdultoMayor.objects.create(rut_adulto_mayor = rut_adulto_mayor, p_nombre = p_nombre, s_nombre = s_nombre, p_apellido = p_apellido, s_apellido = s_apellido, fecha_nacimiento = fecha_nacimiento, email = email, direccion = direccion, comuna = get_comunas, genero = get_genero, usuario = user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error al registrar el adulto mayor: {str(e)}')
            return render(request, 'pages/registro.html', {'regiones': models.Region.objects.all(), 'generos': models.Genero.objects.all()})
    regiones = models.Region.objects.all()
    generos= models.Genero.objects.all()
    return render(request, 'pages/registro.html', {'regiones': regiones, 'generos': generos})

def index(request):
    #se hace una consulta a talleres con un join a instructor
    lisTalleres = models.Taller.objects.select_related('instructor').all()
    return render(request, 'pages/index.html', {'talleres': lisTalleres})

@login_required(login_url="login")
def talleres(request): 
    #se hace una consulta a talleres con un join a instructor,sala y municipalidad
    lisTalleres = models.Taller.objects.select_related('instructor','sala','municipalidad').all()
    return render(request, 'pages/talleres.html',{'talleres': lisTalleres})

@login_required(login_url="login")
def mis_talleres(request):
    return render(request, 'pages/mis-talleres.html')

@login_required(login_url="login")
def inscripcion(request):
    return render(request, 'pages/inscripcion.html')

@login_required(login_url="login")
def perfil(request):
    if request.method == 'POST':
        adulto               = models.AdultoMayor.objects.get(usuario=request.user)
        adulto.p_nombre      = request.POST.get('p_nombre')
        adulto.s_nombre      = request.POST.get('s_nombre')
        adulto.p_apellido    = request.POST.get('p_apellido')
        adulto.s_apellido    = request.POST.get('s_apellido')
        adulto.email         = request.POST.get('email')
        adulto.direccion     = request.POST.get('direccion')
        adulto.comuna        = models.Comuna.objects.get(id=request.POST.get('comuna'))
        adulto.genero        = models.Genero.objects.get(id=request.POST.get('genero'))
        adulto.save()
        messages.success(request, 'Perfil actualizado correctamente')
        return redirect('perfil')
    adulto = models.AdultoMayor.objects.get(usuario=request.user)
    regiones = models.Region.objects.all()
    comunas= models.Comuna.objects.all()
    generos= models.Genero.objects.all()
    return render(request, 'pages/perfil.html', {'adulto': adulto, 'regiones': regiones, 'generos': generos, 'comunas': comunas}) 

#esto al final AJAXS

def get_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = models.Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)

def delete_user(request):
    user = request.user
    adulto = models.AdultoMayor.objects.get(usuario=user)
    adulto.delete()
    user.delete()
    logout(request)
    return redirect('login')


@login_required
def datosTaller(request, idTaller):
    if request.method == 'GET':
        taller = models.Taller.objects.get(id=idTaller)
        adulto = request.user.username
        #Guarda los datos de taller en un diccionario
        datos = {
            'id' : taller.pk,
            'nombre' : taller.nombre,
            'descripcion' : taller.descripcion,
            'horario' : taller.horario,
            'fechaIni' : taller.fecha_inicio,
            'fechaFin' : taller.fecha_fin,
            'adulto' : adulto
        }
        return JsonResponse(datos)
    
@login_required
def inscribir_taller(request, idTaller):
    if request.method == 'POST':
        # Se obtiene el json enviado por el cliente 
        data = json.loads(request.body)
        print("Datos recibidos : ", data)
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')
        adulto = request.user.username
        taller = idTaller

        # Condición para verificar si el adulto mayor ya está inscrito en el taller
        if models.TallerAdultoMayor.objects.filter(adulto_mayor = adulto, taller=taller).exists():
            return JsonResponse({'error': 'Ya esta inscrito en este taller'}, status=400)

        models.TallerAdultoMayor.objects.create(
            fecha_inicio = fecha_inicio, 
            fecha_fin = fecha_fin, 
            adulto_mayor_id = adulto, 
            taller_id = taller
        )
        return JsonResponse({'mensaje': 'Inscripción realizada correctamente'})
    return JsonResponse({'mensaje': 'Error al inscribirse en el taller'})