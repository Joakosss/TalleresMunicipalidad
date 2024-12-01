from django.urls import path;
from . import views;
urlpatterns = [
    path('', views.indexAdministrador, name='index_admin'),
    path('pago', views.pago, name='pago'),
    path('postulaciones', views.postulaciones, name='postulaciones'),
    path('perfil-admin', views.perfilAdmin, name='perfil_admin'),
]   