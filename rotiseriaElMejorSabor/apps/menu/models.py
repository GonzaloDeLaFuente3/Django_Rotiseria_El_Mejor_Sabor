from django.db import models

# Create your models here.
class Menu(models.Model):
    TIPO_MENU = [
        (1, 'Entrada'),
        (2, 'Plato principal'),
        (3 , 'Postre')
    ]
    TIPO_COMIDA = [
        (1, 'Normal'),
        (2, 'Vegetariano'),
        (3, 'Celiaco'),
        (4, 'Diabetico')
    ]
    nombre = models.CharField(max_length=400, unique=True)
    descripcion = models.TextField(blank=True)
    tipoMenu = models.IntegerField(null=False,blank=False, choices=TIPO_MENU)
    precio = models.DecimalField(max_digits=7 , decimal_places=2)
    vigencia = models.BooleanField(default=False)
    tipoComida = models.IntegerField(null=False,blank=False, choices=TIPO_COMIDA)