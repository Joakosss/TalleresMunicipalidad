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
    participantes = models.TallerAdultoMayor.objects.filter(taller_id=id_taller).select_related('adulto_mayor')
    lista_participantes = [
        {
            'id': p.id,
            'fecha_inicio': p.fecha_inicio,
            'fecha_fin': p.fecha_fin,
            'adulto_mayor_id': p.adulto_mayor_id,
            'taller_id': p.taller_id,
            'nombre_adulto_mayor': p.adulto_mayor.p_nombre +' '+ p.adulto_mayor.s_nombre +' '+p.adulto_mayor.p_apellido+' ' + p.adulto_mayor.s_apellido    # Asegúrate de que 'nombre' es el campo correcto
        }
        for p in participantes
    ]
    return JsonResponse(lista_participantes, safe=False)