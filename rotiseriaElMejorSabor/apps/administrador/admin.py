from django.contrib import admin

# Register your models here.
from apps.administrador.models import Pedido

class adminPedido(admin.ModelAdmin):
    # campos
    list_display = ["id", "fechaPedido", "cliente", "estadoPedido", "comentario","envioDomicilio", "tiempoDemora", "cadete","total"]
    # # campos que se pueden modificar
    # list_editable = ["nombre", "tipoMenu", "precio", "vigencia", "tipoComida"]
    # # porque campos se puede buscar
    # search_fields = ["nombre"]
    # # filtros
    # list_filter = ["tipoMenu", "vigencia", "tipoComida"]

    list_per_page = 10

admin.site.register(Pedido, adminPedido)






