from django.urls import path

from apps.empleado import views
app_name = 'empleado'
urlpatterns = [

    path('alta/', views.registrar_empleado, name='alta'),
    path('ver/', views.cargarEmpleados, name='ver'),
    path('modificarEmpleado/<str:cuil>', views.modificarEmpleado, name='modificarEmpleado'),
    path('editar/', views.editarEmpleado, name='editar'),
    path('eliminar/<str:cuil>', views.eliminarEmpleado, name='eliminar'),

    path('guardar_cadete/', views.registrar_Cadete, name='registrar_Cadete'),
    path('guardar_empleado/', views.registrar_empleado_comun, name='registrar_empleado_comun'),



]