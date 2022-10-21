from django.shortcuts import render

# Create your views here.
def altaEmpleado(request):
    return render(request,'empleado/altaEmpleado.html')

def modificarCadete(request):
    return  render(request, 'empleado/modificarCadete.html')

def verEmpleados(request):
    return  render(request, 'empleado/verEmpleados.html')