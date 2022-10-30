from django.db import models

# Create your models here.
class Persona(models.Model):
    cuil = models.CharField(max_length=11, unique=True, primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    domicilio_localidad = models.CharField(max_length=250)
    domicilio_calle = models.CharField(max_length=250)
    domicilio_numero= models.IntegerField()

    class Meta:
        abstract = True
    def nombre_completo(self):
        return "{} {}.".format(self.apellido, self.nombre)

    def __str__(self):
        return self.nombre_completo()