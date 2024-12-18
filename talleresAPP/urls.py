from django.urls import path;
from . import views;
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logear, name='login'),
    path('registro/', views.registro, name='registro'),
    path('talleres/', views.talleres, name='talleres'),
    path('mis-talleres/', views.mis_talleres, name='mis-talleres'),
    path('inscripcion/', views.inscripcion, name='inscripcion'),
    path('perfil/',views.perfil, name='perfil'),
    #boton desconectar
    path('desconectar/', views.desconectar, name='desconectar'),
    #informacion en ajaxs
    path('get_comunas/', views.get_comunas, name='get_comunas'),
    path('datos_taller/<int:idTaller>/', views.datosTaller, name='datos_taller'),
    path('inscribir_taller/<int:idTaller>/', views.inscribir_taller, name='inscribir_taller'),
    
    #Crud Adulto Mayor - User
    path('delete_adulto',views.delete_user, name='delete_adulto'),
]   
