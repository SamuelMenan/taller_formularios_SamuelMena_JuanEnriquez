from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_solicitud, name='form_solicitud'),
    path('confirmacion/', views.confirmacion, name='confirmacion_solicitud'),
]