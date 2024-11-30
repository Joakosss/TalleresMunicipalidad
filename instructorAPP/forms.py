from django import forms
from talleresAPP import models as talleresAPP_models

def getMunicipalidades():
    return talleresAPP_models.Municipalidad.objects.all()

class PostularTaller(forms.Form):
    nombre = forms.CharField(label='Nombre Taller', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre del Taller'}))
    descripcion = forms.CharField(label='Descripcion del taller', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese nombre del Taller'}))
    horarioInicio = forms.TimeField(label='Horario inicio taller',widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'Ingrese horario del Taller'}))
    horarioFin = forms.TimeField(label='Horario fin taller',widget=forms.TimeInput(attrs={'class':'form-control','placeholder':'Ingrese horario del Taller'}))
    municipalidad = forms.ModelChoiceField(queryset=getMunicipalidades(), label='Municipalidad', widget=forms.Select(attrs={'class':'form-control'}))
    
"""  estadoSolicitud =forms.BooleanField()
    instructor = forms.ModelChoiceField(queryset=talleresAPP_models.Instructor.objects.all())
""" 