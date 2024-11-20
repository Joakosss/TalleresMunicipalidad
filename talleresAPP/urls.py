from django.urls import path;
from . import views;
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.logear, name='login'),
    path('registro/', views.registroAdulto.as_view(), name='registro'),
    path('talleres/', views.talleres, name='talleres'),
    path('mis-talleres/', views.mis_talleres, name='mis-talleres'),
    
    #boton desconectar
    path('desconectar/', views.desconectar, name='desconectar'),
    #informacion en ajaxs
    path('get_comunas/', views.get_comunas, name='get_comunas'),
]
