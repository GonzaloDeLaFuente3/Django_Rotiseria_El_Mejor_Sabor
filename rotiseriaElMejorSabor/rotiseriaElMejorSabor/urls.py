"""rotiseriaElMejorSabor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrador/', include('apps.administrador.urls',namespace='administrador')),
    path('index/', include('apps.index.urls')),
    path('menu/', include('apps.menu.urls',namespace='menu')),
    path('cliente/', include('apps.cliente.urls',namespace='cliente')),
    path('navegacion/', include('apps.navegacion.urls')),
    path('empleado/', include('apps.empleado.urls')),
    path('cadete/', include('apps.cadete.urls')),
    path('accounts/', include('django.contrib.auth.urls')),


]
