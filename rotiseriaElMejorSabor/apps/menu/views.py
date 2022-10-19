
from django.shortcuts import render, redirect
from django.views.generic import ListView
# Create your views here.


from apps.menu.models import Menu


def altaMenu(request):
    return  render(request, 'menu/altaMenu.html')

def bajaMenu(request):
    return  render(request, 'menu/bajaMenu.html')
def modificarMenu(request):
    return  render(request, 'menu/modificarMenu.html')


def cargarMenu(request):
    return render(request, 'menu/verMenus.html',
                  {'menus': Menu.objects.all()})

def eliminarMenu(request, id ):
    # menu = Menu.objects.get(id=id)
    # menu.delete()
    #redireccion


    return  redirect('/verMenu.html')