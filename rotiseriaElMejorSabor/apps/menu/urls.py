from django.urls import path
from django.views.generic import TemplateView

from apps.menu import views
app_name = 'menu'
urlpatterns = [
    # TemplateView.as_view(template_name='base/home.html')
    path('alta/', TemplateView.as_view(template_name='menu/altaMenu.html'), name='alta'),
    path('modificar/', views.modificarMenu, name='modificar'),
    path('ver/', views.cargarMenu, name='cargar'),
    path('eliminar/<int:id>', views.eliminarMenu, name='eliminar'),
    path('registrar', views.registrar_menu, name='registrar_menu')
]