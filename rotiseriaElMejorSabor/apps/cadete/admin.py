from django.contrib import admin

# Register your models here.

from apps.cadete.models import Cadete

class adminCadete(admin.ModelAdmin):
    # campos
    list_display = ["cuil", "vigenciaCarnet", "patente", "codigoZona"]
     # campos que se pueden modificar
    list_editable = ["vigenciaCarnet", "patente", "codigoZona"]

    # filtros
    list_filter = ["codigoZona"]

    list_per_page = 10

admin.site.register(Cadete, adminCadete)

