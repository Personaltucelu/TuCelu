from django.db import models
from django.utils import timezone

# Create your models here.
class Celular(models.Model):
    marca = models.ForeignKey('appcelu.marca', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    Color = models.CharField(max_length=150)
    precio = models.CharField(max_length=15)
    fecha_publicacion = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre



