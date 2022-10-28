
from django.shortcuts import render, redirect
from django.template.defaultfilters import upper
from django.urls import reverse
from django.views.generic import ListView
# Create your views here.

from apps.menu.models import Menu


def registrar_menu(request):
    nombre = upper(request.POST['nombreMenu'])
    print(nombre)
    descripcion = request.POST['descripcionMenu']
    tipo_menu = request.POST['tipoMenu']
    precio = request.POST['precioMenu']
    # vigencia = False
    # print(vigencia)
    revisado = request.POST.get('vigente')
    print(revisado)
    if (revisado == None):
        vigencia = False
    else:
        vigencia = True

    tipo_comida = request.POST['tipoComida']
    imagen = request.POST['imagen']


    menu = Menu.objects.create(nombre=nombre,descripcion=descripcion,tipoMenu=tipo_menu,precio=precio,vigencia=vigencia,tipoComida=tipo_comida, imagen=imagen)
    return redirect(reverse("menu:cargar"))

def modificarMenu(request, id):
    return  render(request, 'menu/modificarModal.html', {'menu': Menu.objects.get(id=id)})


def cargarMenu(request):
    return render(request, 'menu/verMenus.html',
                  {'menus': Menu.objects.all()})

def eliminarMenu(request,id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    #redireccion
    return redirect(reverse("menu:cargar"))

def editarMenu(request):
    nombre = upper(request.POST['nombreMenu'])
    print(nombre)
    descripcion = request.POST['descripcionMenu']
    tipo_menu = request.POST['tipoMenu']
    precio = request.POST['precioMenu']
    # vigencia = False
    # print(vigencia)
    revisado = request.POST.get('vigente')

    if (revisado == None):
        vigencia = False
    else:
        vigencia = True

    tipo_comida = request.POST['tipoComida']
    imagen = request.POST['imagen']

    id = request.POST['codigoMenu']

    menu = Menu.objects.get(id=id)
    menu.nombre = nombre
    menu.descripcion = descripcion
    menu.tipoMenu = tipo_menu
    menu.precio = precio
    menu.vigencia = vigencia
    menu.tipoComida = tipo_comida
    menu.imagen=imagen
    print(nombre)
    menu.save()
    return redirect(reverse("menu:cargar"))