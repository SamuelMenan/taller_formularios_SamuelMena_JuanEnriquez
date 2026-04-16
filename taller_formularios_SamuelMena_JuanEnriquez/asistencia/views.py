from django.http import HttpResponse


def formulario_asistencia(request):
    return HttpResponse("Formulario de asistencia")


def confirmacion(request):
    return HttpResponse("Asistencia registrada correctamente")