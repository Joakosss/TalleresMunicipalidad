from django.urls import path;
from . import views;
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registro/', views.registroAdulto.as_view(), name='registro'),
    path('talleres/', views.talleres, name='talleres'),
]
