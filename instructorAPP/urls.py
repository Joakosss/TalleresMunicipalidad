from django.urls import path;
from . import views;
urlpatterns = [
    path('', views.indexInstructor, name='index_instructor'),
    path('postular-taller', views.postularTaller, name='postular_taller'),
    path('mis-talleres', views.misTalleres, name='mis_talleres'),
    
    #Ajax
    
    path('get-participantes/<int:id_taller>', views.participantesTaller, name='participantes_taller'),
    
    
]   