from django.db import models

# Create your models here.

# hay que revisar pq existe un foreing key pero de 1 a 1 oneToOneField
class Perfil(models.Model):
    descripcion = models.CharField(max_length=40)

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=40)
    contrasenia = models.CharField(max_length=40)
    perfil = models.ForeignKey('Perfil', on_delete=models.CASCADE)



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
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Instructor(models.Model):
    rut_instructor = models.CharField(max_length=20, primary_key=True)
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20, blank=True, null=True)
    p_apellido = models.CharField(max_length=20)
    s_apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField
    direccion = models.CharField(max_length=40)
    valor_hora= models.IntegerField
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class Region(models.Model):
    nombre = models.CharField(max_length=30)

class Comuna(models.Model):
    nombre = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class Genero(models.Model):
    nombre = models.CharField(max_length=20)


class Municipalidad(models.Model):
    nombre = models.CharField(max_length=40)

class Sala(models.Model):
    nombre = models.CharField(max_length=30)
    especificaciones = models.CharField(max_length=30)

class Taller(models.Model):
    id_taller = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    horario = models.TimeField
    fecha_inicio= models.DateField
    fecha_fin= models.DateField
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    municipalidad = models.ForeignKey('Municipalidad', on_delete=models.CASCADE)


class TallerAdultoMayor(models.Model):
    fecha_inicio = models.DateField
    fecha_fin = models.DateField
    adulto_mayor = models.ForeignKey('AdultoMayor', on_delete=models.CASCADE)
    taller = models.ForeignKey('Taller', on_delete=models.CASCADE)

class ValorizacionTaller(models.Model):
    taller_adulto_mayor = models.ForeignKey('TallerAdultoMayor', on_delete=models.CASCADE)
    valoracion = models.IntegerField

class Bono(models.Model):
    valorizacion_taller = models.ForeignKey('ValorizacionTaller', on_delete=models.CASCADE)
    fecha_bono = models.DateField
    estado_bono = models.BooleanField    
    """ Aqui hay que revisar que mierda, en estado bono como lo vamos a dejar, si es un booleano o un string,"""

class Pago(models.Model):
    bono = models.ForeignKey('Bono', on_delete=models.CASCADE)
    fecha_pago = models.DateField
    monto = models.IntegerField
    estado_pago = models.CharField(max_length=20)
    taller = models.ForeignKey('Taller', on_delete=models.CASCADE)

class FuncionarioMunicipal(models.Model):
    rut_funcionario = models.CharField(max_length=20, primary_key=True)
    p_nombre = models.CharField(max_length=20)
    s_nombre = models.CharField(max_length=20, blank=True, null=True)
    p_apellido = models.CharField(max_length=20)
    s_apellido = models.CharField(max_length=20)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    municipalidad = models.ForeignKey('Municipalidad', on_delete=models.CASCADE)

class PropuestaTaller(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
    horario = models.TimeField
    fecha_inicio= models.DateField
    fecha_fin= models.DateField
    estadoSolicitud =models.BooleanField
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    municipalidad = models.ForeignKey('Municipalidad', on_delete=models.CASCADE)

class Material(models.Model):
    nombre = models.CharField(max_length=30)
    especificacion = models.CharField(max_length=40)
    stock = models.IntegerField
    precio = models.IntegerField

class SolicitudMaterial(models.Model):
    cantidad = models.IntegerField
    fecha_solicitud = models.DateField
    estado_solicitud = models.BooleanField
    materiales = models.ForeignKey('Materiales', on_delete=models.CASCADE)
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    taller = models.ForeignKey('Taller', on_delete=models.CASCADE)