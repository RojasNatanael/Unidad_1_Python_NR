from django.db import models

# Create your models here.
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    consumo_maximo = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="dispositivos")

    def __str__(self):
        return self.nombre


class Medicion(models.Model):
    consumo = models.FloatField()
    fecha = models.DateTimeField()
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="mediciones")
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="mediciones")

    def __str__(self):
        return f"Medición {self.id} - {self.dispositivo.nombre} ({self.fecha})"


class Alerta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    medicion = models.ForeignKey(Medicion, on_delete=models.CASCADE, related_name="alertas")

    def __str__(self):
        return self.titulo
