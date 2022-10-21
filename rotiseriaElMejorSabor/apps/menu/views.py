
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
# Create your views here.

from apps.menu.models import Menu


def registrar_menu(request):
    nombre = request.POST['nombreMenu']
    descripcion = request.POST['descripcionMenu']
    tipo_menu = request.POST['tipoMenu']
    precio = request.POST['precioMenu']
    if (request.POST['vigente'] == "True"):
        vigencia = True
    else:
        vigencia = False
    tipo_comida = request.POST['tipoComida']


    menu = Menu.objects.create(nombre=nombre,descripcion=descripcion,tipoMenu=tipo_menu,precio=precio,vigencia=vigencia,tipoComida=tipo_comida)
    return redirect(reverse("menu:cargar"))

def bajaMenu(request):
    return  render(request, 'menu/bajaMenu.html')
def modificarMenu(request):
    return  render(request, 'menu/modificarMenu.html')


def cargarMenu(request):
    return render(request, 'menu/verMenus.html',
                  {'menus': Menu.objects.all()})

def eliminarMenu(request,id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    #redireccion
    return redirect(reverse("menu:cargar"))