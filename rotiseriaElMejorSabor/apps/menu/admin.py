from django.contrib import admin

# Register your models here.
from .models import Menu
class adminMenu(admin.ModelAdmin):
    #campos
    list_display = ["id","nombre","descripcion","tipoMenu","precio", "vigencia","tipoComida","imagen"]
    #campos que se pueden modificar
    list_editable = ["nombre","tipoMenu","precio", "vigencia","tipoComida"]
    #porque campos se puede buscar
    search_fields = ["nombre"]
    #filtros
    list_filter = ["tipoMenu", "vigencia","tipoComida"]

    list_per_page = 10

admin.site.register(Menu,adminMenu)
