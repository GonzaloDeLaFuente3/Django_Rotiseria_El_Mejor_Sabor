from django.shortcuts import render

# Create your views here.
def altaMenu(request):
    return  render(request, 'menu/altaMenu.html')

def bajaMenu(request):
    return  render(request, 'menu/bajaMenu.html')
def modificarMenu(request):
    return  render(request, 'menu/modificarMenu.html')
def verMenus(request):
    return  render(request, 'menu/verMenus.html')