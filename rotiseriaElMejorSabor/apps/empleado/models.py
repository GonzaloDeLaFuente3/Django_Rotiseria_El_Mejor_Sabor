from django.db import models

# Create your models here.
from apps.persona.models import Persona


class Empleado(Persona):
    telefonoFijo = models.IntegerField(null=True)
    fechaNacimiento = models.DateField()
    telefonoCelular = models.IntegerField()
    domicilio_departamento = models.CharField(max_length=300)
    fechaIngreso = models.DateField()

    class Meta:
        abstract = True

