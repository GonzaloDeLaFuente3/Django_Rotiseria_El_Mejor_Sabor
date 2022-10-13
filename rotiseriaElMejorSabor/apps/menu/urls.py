from django.urls import path

from apps.menu import views
apps_name = 'menu'
urlpatterns = [
    path('altaMenu.html', views.altaMenu, name='altaMenu'),
    path('bajaMenu.html', views.bajaMenu, name='bajaMenu'),
    path('modificarMenu.html', views.modificarMenu, name='modificarMenu'),
    path('verMenus.html', views.verMenus, name='verMenus'),
]