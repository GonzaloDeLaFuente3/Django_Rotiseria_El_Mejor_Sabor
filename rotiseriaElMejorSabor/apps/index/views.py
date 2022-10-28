from django.shortcuts import render

# Create your views here.
from apps.menu.models import Menu
def index(request):
    platos = Menu.objects.all()
    return render(request, 'index/index.html',
                  {'platos':platos})

