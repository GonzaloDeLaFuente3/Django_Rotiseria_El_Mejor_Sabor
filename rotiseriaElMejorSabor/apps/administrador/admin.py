from django.contrib import admin

# Register your models here.
from apps.administrador.models import Pedido

class adminPedido(admin.ModelAdmin):
    # campos
    list_display = ["id", "fechaPedido", "cliente", "estadoPedido", "comentario","envioDomicilio", "tiempoDemora", "cadete","total"]
     # campos que se pueden modificar
    list_editable = ["fechaPedido", "cliente", "estadoPedido","envioDomicilio", "tiempoDemora", "cadete","total"]

    # filtros
    list_filter = ["estadoPedido", "envioDomicilio"]

    list_per_page = 20

admin.site.register(Pedido, adminPedido)






