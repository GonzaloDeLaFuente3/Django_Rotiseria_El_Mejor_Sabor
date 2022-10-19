from django.shortcuts import render

# Create your views here.
from apps.cliente.models import Cliente


def altaCliente(request):
    return  render(request, 'cliente/altaCliente.html')

def bajaCliente(request):
    return  render(request, 'cliente/bajaCliente.html')

def modificarCliente(request):
    return  render(request, 'cliente/modificarCliente.html')



def cargarClientes(request):
    return render(request, 'cliente/verClientes.html',
                  {'clientes': Cliente.objects.all()})