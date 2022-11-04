from django.urls import path
from django.views.generic import TemplateView

from apps.cliente import views
app_name = 'cliente'
urlpatterns = [
    # TemplateView.as_view(template_name='base/home.html')
    path('alta/', TemplateView.as_view(template_name='cliente/altaCliente.html'), name='alta'),
    path('registrar/', views.altaCliente, name='registrar_cliente_admin'),
    path('ver/', views.cargarClientes, name='cargar'),
    path('eliminar/<str:cuil>', views.eliminarCliente, name='eliminar'),
    path('modificar/<str:cuil>', views.modificarCliente, name='modificar'),
    path('editar/', views.editarCliente, name='editar'),
    #cliente desde la parte del index
    path('registrar_cliente/', TemplateView.as_view(template_name='cliente/registrarClienteIndex.html'), name='registrar_cliente'),
    path('registrarse_como_cliente/', views.registrar_cliente_desde_index, name='registrarse_como_cliente'),

]