from django.urls import path;
from . import views;
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logear, name='login'),
    path('registro/', views.registro, name='registro'),
    path('talleres/', views.talleres, name='talleres'),
    path('perfil/',views.perfil, name='perfil'),
    #boton desconectar
    path('desconectar/', views.desconectar, name='desconectar'),
    #informacion en ajaxs
    path('get_comunas/', views.get_comunas, name='get_comunas'),
    
    #Crud Adulto Mayor - User
    path('delete_adulto',views.delete_User, name='delete_adulto'),
]
