from django.db import models

# Create your models here.
from apps.cliente.models import Cliente
from apps.cadete.models import Cadete
from apps.menu.models import Menu

class Pedido(models.Model):
    ESTADO_OPCIONES = [
        (1, 'Pendiente'),
        (2, 'En preparación'),
        (3, 'En camino'),
        (4, 'Entregado'),
        (5, 'Devuelto'),
        (6, 'Cancelado')
    ]
    fechaPedido = models.DateField()
    fecha_hora = models.TimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menu)
    estadoPedido = models.IntegerField(null=False,blank=False, choices=ESTADO_OPCIONES)
    comentario = models.TextField(blank=True)
    envioDomicilio = models.BooleanField(default=False)
    tiempoDemora = models.IntegerField(blank=True)
    cadete = models.ForeignKey(Cadete, on_delete=models.CASCADE, blank=True, null=True)
    total = models.IntegerField()




