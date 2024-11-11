from django.shortcuts import render
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
        us = authenticate(request, username=usuario, password=contrasena)
        if us is not None and us.is_active:
            auth_login(request, us)
            return render(request, 'pages/index.html')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')
            return render(request, loginURL)
    return render(request, 'pages/login.html')






""" def desconectar(request):
    logout(request)
    return render(request, 'loginURL') """

class registroAdulto(SessionWizardView):
    template_name = 'pages/register.html'
    form_list = [forms.regisAdulto1, forms.regisAdulto2, forms.regisAdulto3]
    
    def done(self, form_list, **kwargs):
        # Aquí puedes procesar los datos de los formularios
        form_data = [form.cleaned_data for form in form_list]
        
        #aqui accedemos alos datos de los formularios
        # Combina los datos de los formularios en un solo diccionario
        user_data = {**form_data[0], **form_data[1], **form_data[2]}
        print (user_data)
        return render(self.request, 'pages/login.html')





def index(request):
    #se hace una consulta a talleres con un join a instructor
    lisTalleres = models.Taller.objects.select_related('instructor').all()
    return render(request, 'pages/index.html', {'talleres': lisTalleres})

def talleres(request): 
    #se hace una consulta a talleres con un join a instructor,sala y municipalidad
    lisTalleres = models.Taller.objects.select_related('instructor','sala','municipalidad').all()
    return render(request, 'pages/talleres.html',{'talleres': lisTalleres})








#esto al final AJAXS

def get_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = models.Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
    return JsonResponse(list(comunas), safe=False)