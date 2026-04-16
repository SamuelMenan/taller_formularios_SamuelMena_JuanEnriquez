from django.shortcuts import render

# Create your views here.
def crear_xxx(request):
    if request.method == 'POST':
        form = Formulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')
    else:
        form = Formulario()

    return render(request, 'template.html', {'form': form})