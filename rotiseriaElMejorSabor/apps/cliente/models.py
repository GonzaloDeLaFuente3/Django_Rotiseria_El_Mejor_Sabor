
from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
from apps.persona.models import Persona


class Cliente(Persona):
    ZONA_OPCIONES = [
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste')
    ]
    domicilio_barrio = models.CharField(max_length=200)
    domicilio_observacion = models.TextField(blank=True)
    domicilio_zona = models.CharField(max_length=5, choices=ZONA_OPCIONES)
    telefono = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)





