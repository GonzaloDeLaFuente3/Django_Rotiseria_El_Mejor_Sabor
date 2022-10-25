from django.db import models

# Create your models here.
from apps.cliente.models import Cliente


# class Pedido(models.Model):
#     ESTADO_OPCIONES = [
#         ('1', 'Pendiente'),
#         ('2', 'En preparación'),
#         ('3', 'En camino'),
#         ('4', 'Entregado'),
#         ('5', 'Devuelto'),
#         ('6', 'Cancelado')
#     ]
#     fechaPedido = models.DateField()
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     menu = models.ManyToManyField(Plato)
#     estadoPedido = models.IntegerField(null=False,blank=False, choices=ESTADO_OPCIONES)
#     comentario = models.TextField(blank=True)
#     envioDomicilio = models.CharField(max_length=25)
#     tiempoDemora = models.IntegerField()
#     cadete = models.ForeignKey(Cadete, on_delete=models.CASCADE)
#     total = models.IntegerField()




