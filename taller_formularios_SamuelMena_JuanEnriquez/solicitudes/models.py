from django.db import models

# Create your models here.
class Solicitud(models.Model):
    TIPOS = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre = models.CharField(max_length=150)
    documento = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    asunto = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    archivo = models.FileField(upload_to='archivos/', blank=True, null=True)