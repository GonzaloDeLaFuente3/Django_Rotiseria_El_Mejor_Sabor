from django.urls import path

from apps.menu import views
app_name = 'menu'
urlpatterns = [
    path('alta', views.altaMenu, name='alta'),
    path('baja', views.bajaMenu, name='baja'),
    path('modificar', views.modificarMenu, name='modificar'),
    path('ver/', views.cargarMenu, name='cargar'),
    path('eliminar/<int:id>', views.eliminarMenu, name='eliminar')
]