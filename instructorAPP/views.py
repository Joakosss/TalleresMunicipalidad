from django.shortcuts import render
from django.http import JsonResponse
from . import forms
from talleresAPP import models
# Create your views here.

def indexInstructor(request):
    return render(request, 'pages/index-instructor.html')

def postularTaller(request):
    formulario = forms.PostularTaller()
    return render(request, 'pages/postular-taller.html',{'formulario':formulario})

def misTalleres(request):
    talleres = models.Taller.objects.filter(instructor='202002002') # Cambiar por el id del instructor este es ejemplo - request.user.username
    return render(request, 'pages/mis-talleres-instructor.html', {'talleres': talleres})


#Ajax

def participantesTaller(request, id_taller):
    participantes = models.TallerAdultoMayor.objects.filter(taller_id=id_taller).select_related('adultomayor')
    lista_participantes = list(participantes.values())
    return JsonResponse(lista_participantes, safe=False)