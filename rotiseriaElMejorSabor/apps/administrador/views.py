from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render
# # Create your views here.
# def index(request):
#     return HttpResponse('hola mundo')

def admin_login(request):
    return  render(request, 'administrador/admin-login.html')

def administrador_configuracion(request):
    return  render(request, 'administrador/configuracion-admin.html')

def pedido(request):
    return  render(request, 'administrador/pedido.html')

def estadisticas(request):
    return  render(request, 'administrador/estadisticas.html')

def historial_pedidos(request):
    return  render(request, 'administrador/historial-pedidos.html')