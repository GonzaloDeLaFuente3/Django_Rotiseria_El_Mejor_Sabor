from django.contrib import admin

# Register your models here.
from .models import Empleado
class adminEmpleado(admin.ModelAdmin):
    #campos
    list_display = ["cuil", "nombre", "apellido","telefonoFijo","telefonoCelular","domicilio_calle","domicilio_numero","domicilio_departamento", "domicilio_localidad", "fechaIngreso"]
    #campos que se pueden modificar
    list_editable = ["nombre", "apellido","domicilio_localidad", "domicilio_departamento","telefonoFijo","telefonoCelular","domicilio_calle","domicilio_numero"]
    #porque campos se puede buscar
    search_fields = ["cuil", "nombre","apellido"]
    #filtros
    list_filter = ["domicilio_localidad","domicilio_departamento"]

    list_per_page = 10
admin.site.register(Empleado)