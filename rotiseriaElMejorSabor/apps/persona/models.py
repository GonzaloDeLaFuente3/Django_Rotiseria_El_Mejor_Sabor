from django.db import models

# Create your models here.
class Persona(models.Model):
    cuil = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    domicilio_calle = models.CharField(max_length=200)
    domicilio_numero = models.IntegerField()
    domicilio_localidad = models.CharField(max_length=250)

    class Meta:
        abstract = True
