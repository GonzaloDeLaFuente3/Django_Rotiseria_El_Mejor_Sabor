from django.urls import path

from apps.navegacion import views
app_name = 'navegacion'
urlpatterns = [
    path('ayuda', views.ayuda, name='ayuda'),
    path('contacto', views.contacto, name='contacto'),
    path('sobre_nosotros', views.sobreNosotros, name='sobre_nosotros'),
    path('comprar', views.comprar, name='comprar'),
    path('configuracion', views.configuracion, name='configuracion'),
    path('login', views.login, name='login'),
    path('recuperar_contraseña.html', views.recuperarContraseña, name='recuperar_contraseña'),
    path('register', views.register, name='register'),

]