from django.forms import ModelForm
from .models import Asistencia

class AsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'