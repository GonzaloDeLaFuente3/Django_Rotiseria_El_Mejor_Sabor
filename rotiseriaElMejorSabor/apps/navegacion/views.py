from django.shortcuts import render

# Create your views here.
from apps.menu.models import Menu
def ayuda(request):
    return  render(request, 'navegacion/ayuda.html')

def contacto(request):
    return  render(request, 'navegacion/contacto.html')

def sobreNosotros(request):
    return  render(request, 'navegacion/sobreNosotros.html')

def comprar(request, id):
    plato = Menu.objects.get(id=id)
    return  render(request,
                   'navegacion/comprar.html',
                   {'plato':plato})

def configuracion(request):
    return  render(request, 'navegacion/configuracion.html')

def login(request):
    return  render(request, 'navegacion/login.html')

def recuperarContraseña(request):
    return  render(request, 'navegacion/recuperarContraseña.html')
def register(request):
    return  render(request, 'navegacion/register.html')

