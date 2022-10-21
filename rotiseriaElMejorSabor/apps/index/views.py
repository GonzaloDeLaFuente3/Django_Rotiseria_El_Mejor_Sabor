from django.shortcuts import render

# Create your views here.
from apps.menu.models import Menu
def index(request):
    return render(request, 'index/index.html',
                  {'menus': Menu.objects.all()})