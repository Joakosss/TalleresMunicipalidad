from django import forms



class CrearMaterial(forms.Form):
    nombre = forms.CharField(label='Nombre Taller', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre del material'}))
    especificacion = forms.CharField(label='Descripcion del taller', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese nombre del material'}))
    stock = forms.IntegerField(label='Stock',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese stock del material'}))
    precio = forms.IntegerField(label='Precio',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese precio del material'}))  

class CrearSala(forms.Form):
    nombre = forms.CharField(label='Nombre sala', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre de la sala'}))
    especificacion = forms.CharField(label='Descripcion de la sala', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese nombre de la sala'}))
class CrearMunicipalidad(forms.Form):
    nombre = forms.CharField(label='Nombre municipalidad', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre de la municipalidad'}))

