from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_asistencia, name='form_asistencia'),
    path('confirmacion/', views.confirmacion, name='confirmacion_asistencia'),
]