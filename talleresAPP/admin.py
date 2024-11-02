from django.contrib import admin
from .models import Perfil, Usuario, AdultoMayor, Instructor, Region, Comuna, Genero, Municipalidad, Sala, Taller, TallerAdultoMayor, ValorizacionTaller, Bono, Pago, FuncionarioMunicipal, PropuestaTaller, Material, SolicitudMaterial

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Usuario)
admin.site.register(AdultoMayor)
admin.site.register(Instructor)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Genero)
admin.site.register(Municipalidad)
admin.site.register(Sala)
admin.site.register(Taller)
admin.site.register(TallerAdultoMayor)
admin.site.register(ValorizacionTaller)
admin.site.register(Bono)
admin.site.register(Pago)
admin.site.register(FuncionarioMunicipal)
admin.site.register(PropuestaTaller)
admin.site.register(Material)
admin.site.register(SolicitudMaterial)
