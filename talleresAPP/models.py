from django.db import models

# Create your models here.


class Taller(models.Model):
    id_taller = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    horario = models.TimeField
    fecha_inicio= models.DateField
    fecha_fin= models.DateField

class AdultoMayor(models.Model):
    rut_adulto_mayor = models.CharField(max_length=20, primary_key=True)
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20, blank=True, null=True)
    p_apellido = models.CharField(max_length=20)
    s_apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField
    direccion = models.CharField(max_length=40)
    certificado_residencia = models.FileField(upload_to='archivos/', blank=True, null=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)

""" class Instructor(models.Model):
    rut_adulto_mayor = models.CharField(max_length=20, primary_key=True)
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20, blank=True, null=True)
    p_apellido = models.CharField(max_length=20)
    s_apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField
    direccion = models.CharField(max_length=40)
    certificado_residencia = models.FileField(upload_to='archivos/', blank=True, null=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE) """

class Region(models.Model):
    nombre = models.CharField(max_length=30)

class Comuna(models.Model):
    nombre = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Genero(models.Model):
    nombre = models.CharField(max_length=20)