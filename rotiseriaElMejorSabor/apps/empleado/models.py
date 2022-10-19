from django.db import models

# Create your models here.
from apps.persona.models import Persona


# class Empleado(Persona):
#     telefonoFijo = models.IntegerField(null=True)
#     telefonoCelular = models.IntegerField()
#     domicilio_departamento = models.CharField(max_length=300)
#     fechaNacimiento = models.DateField()
#     fechaIngreso = models.DateField()
#
# class Cadete(Empleado):
#     vigenciaCarnet = models.DateField()
#     patente = models.CharField(max_length=7, unique=True)
#     codigoZona = models.IntegerField(max_length=1)
#     correoElectronico
#     contraseña = models.CharField(max_length=200)
# password1 = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False)
