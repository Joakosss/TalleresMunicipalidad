from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, logout,login as auth_login
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from formtools.wizard.views import SessionWizardView
from . import models, forms
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
    regiones = models.Region.objects.all()
    comuna = models.Comuna.objects.all()
    genero= models.Genero.objects.all()
    return render(request, 'pages/registro.html')

class registroAdulto(SessionWizardView):
    template_name = 'pages/register.html'
    form_list = [forms.regisAdulto1, forms.regisAdulto2, forms.regisAdulto3]
    
    def done(self, form_list, **kwargs):
        # Aquí puedes procesar los datos de los formularios
        form_data = [form.cleaned_data for form in form_list]
        
        #aqui accedemos alos datos de los formularios
        # Combina los datos de los formularios en un solo diccionario
        user_data = {**form_data[0], **form_data[1], **form_data[2]}
        
        if User.objects.filter(username=user_data['rut_adulto_mayor']).exists():
            messages.error(self.request, 'El usuario ya existe')
            return redirect('login')

        # Crea un nuevo usuario
        try:
           
            user = User.objects.create_user(username=user_data['rut_adulto_mayor'], password=user_data['contrasenia1'])
            
            get_comunas = models.Comuna.objects.get(id=user_data['comuna'])
            get_genero = models.Genero.objects.get(id=user_data['genero'])
            
            adulto = models.AdultoMayor.objects.create(rut_adulto_mayor = user_data['rut_adulto_mayor'], p_nombre = user_data['p_nombre'], s_nombre = user_data['s_nombre'], p_apellido = user_data['p_apellido'], s_apellido = user_data['s_apellido'], fecha_nacimiento = user_data['fecha_nacimiento'], email = user_data['email'], direccion = user_data['direccion'], comuna = get_comunas, genero = get_genero, usuario = user)
            messages.success(self.request, 'Usuario registrado correctamente')
            return redirect('login')
        except Exception as e:
            messages.error(self.request, f'Error al registrar el adulto mayor: {str(e)}')
            return render(self.request, self.template_name, {'form_list': form_list})





def index(request):
    #se hace una consulta a talleres con un join a instructor
    lisTalleres = models.Taller.objects.select_related('instructor').all()
    return render(request, 'pages/index.html', {'talleres': lisTalleres})

@login_required(login_url="login")
def talleres(request): 
    #se hace una consulta a talleres con un join a instructor,sala y municipalidad
    lisTalleres = models.Taller.objects.select_related('instructor','sala','municipalidad').all()
    return render(request, 'pages/talleres.html',{'talleres': lisTalleres})








#esto al final AJAXS

def get_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = models.Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)