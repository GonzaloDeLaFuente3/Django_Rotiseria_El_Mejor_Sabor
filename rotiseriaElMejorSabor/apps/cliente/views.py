from django.shortcuts import render

# Create your views here.
def altaCliente(request):
    return  render(request, 'cliente/altaCliente.html')

def bajaCliente(request):
    return  render(request, 'cliente/bajaCliente.html')

def modificarCliente(request):
    return  render(request, 'cliente/modificarCliente.html')

def verClientes(request):
    return  render(request, 'cliente/verClientes.html')