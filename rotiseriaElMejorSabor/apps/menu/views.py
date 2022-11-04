from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.template.defaultfilters import upper
from django.urls import reverse
from django.views.generic import ListView
from django.contrib import messages
# Create your views here.

from apps.menu.models import Menu

@permission_required('menu.add_menu', login_url="navegacion:login")
def registrar_menu(request):
    nombre = request.POST['nombreMenu']
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
    messages.success(request,"se registro el menu correctamente")
    return redirect(reverse("menu:cargar"))

@permission_required('menu.change_menu', login_url="navegacion:login")
def modificarMenu(request, id):
    return  render(request, 'menu/modificarModal.html', {'menu': Menu.objects.get(id=id)})


@permission_required('menu.view_menu', login_url="navegacion:login")
def cargarMenu(request):
    return render(request, 'menu/verMenus.html',
                  {'menus': Menu.objects.all()})

@permission_required('menu.delete_menu', login_url="navegacion:login")
def eliminarMenu(request,id):
    menu = Menu.objects.get(id=id)
    menu.delete()
    #redireccion
    messages.success(request, "se elimino el menu correctamente")
    return redirect(reverse("menu:cargar"))

@permission_required('menu.change_menu', login_url="navegacion:login")
def editarMenu(request):
    nombre = upper(request.POST['nombreMenu'])
    print(nombre)
    descripcion = request.POST['descripcionMenu']
    tipo_menu = request.POST['tipoMenu']
    precio = request.POST['precioMenu']
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
    messages.success(request, "se modifico el menu correctamente")
    return redirect(reverse("menu:cargar"))