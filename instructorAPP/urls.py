from django.urls import path;
from . import views;
urlpatterns = [
    path('', views.indexInstructor, name='index_instructor'),
]   