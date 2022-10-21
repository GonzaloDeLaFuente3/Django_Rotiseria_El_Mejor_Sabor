from django.db import models

# Create your models here.
from apps.cliente.models import Cliente


class Pedido(models.Model):
    ESTADO_OPCIONES = [
        ('1', 'Pendiente'),
        ('2', 'En preparación'),
        ('3', 'En camino'),
        ('4', 'Entregado'),
        ('5', 'Devuelto'),
        ('6', 'Cancelado')
    ]
    TIPO_ENTREGA = [
        ('1', 'Envío a domicilio'),
        ('2', 'Retiro en el local')
    ]
    fechaPedido = models.DateField()
    horaPedido = models.TimeField()
    menuPedido = models.CharField(max_length=25)
    precioPedido = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    domicilio = models.CharField(max_length=25)
    tipoEntrega = models.IntegerField(null=False, blank=False, choices=TIPO_ENTREGA)
    estadoPedido = models.IntegerField(null=False,blank=False, choices=ESTADO_OPCIONES)
    comentarioCliente = models.TextField(blank=True)





