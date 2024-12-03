from django.urls import path;
from . import views;
urlpatterns = [
    path('', views.indexAdministrador, name='index_admin'),
    path('pago', views.pago, name='pago'),
    path('postulaciones', views.postulaciones, name='postulaciones'),
    path('perfil-admin', views.perfilAdmin, name='perfil_admin'),
    path('materiales', views.Materiales, name='materiales'),
    path('crear-material', views.crearMaterial, name='crear_material'),
    path('solicitudes-materiales', views.solicitudesMateriales, name='solicitudes_materiales'),
    path('salas', views.Salas, name='salas'),
    path('crear-sala', views.CrearSala, name='crear_sala'),
    path('municipalidad', views.Municipalidad, name='municipalidad'),
    path('crear-municipalidad', views.CrearMunicipalidad, name='crear_municipalidad'),
]   