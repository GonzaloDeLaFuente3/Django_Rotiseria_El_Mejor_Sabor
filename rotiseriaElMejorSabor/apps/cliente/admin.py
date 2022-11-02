from django.contrib import admin

# Register your models here.
from .models import Cliente
class adminCliente(admin.ModelAdmin):
    #campos
    list_display = ["cuil", "nombre", "apellido","domicilio_localidad", "domicilio_barrio", "domicilio_observacion","domicilio_zona","telefono","domicilio_calle","domicilio_numero", "usuario"]
    #campos que se pueden modificar
    list_editable = ["nombre", "apellido","domicilio_localidad", "domicilio_barrio","domicilio_zona","telefono","domicilio_calle","domicilio_numero"]
    #porque campos se puede buscar
    search_fields = ["cuil", "nombre","apellido"]
    #filtros
    list_filter = ["domicilio_localidad","domicilio_zona","domicilio_barrio"]

    list_per_page = 10
admin.site.register(Cliente, adminCliente)

