from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render
# # Create your views here.
# def index(request):
#     return HttpResponse('hola mundo')

def administrador(request):
    return  render(request, 'administrador/admin-login.html')