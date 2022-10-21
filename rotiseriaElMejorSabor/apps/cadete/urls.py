from django.urls import path

from apps.cadete import views
app_name = 'cadete'
urlpatterns = [

    path('login', views.cadete_login, name='login'),
    path('configuracion', views.configuracion_cadete, name='configuracion'),


]