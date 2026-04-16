from django.shortcuts import redirect, render

from .forms import SolicitudForm


def formulario_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('confirmacion_solicitud')
    else:
        form = SolicitudForm()

    return render(request, 'formulario.html', {'form': form})


def confirmacion(request):
    return render(request, 'confirmacion.html')