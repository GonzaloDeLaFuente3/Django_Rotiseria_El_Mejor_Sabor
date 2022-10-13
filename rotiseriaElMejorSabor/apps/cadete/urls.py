from django.urls import path

from apps.cadete import views
apps_name = 'cadete'
urlpatterns = {

    path('cadete-login.html', views.cadete_login, name='cadete-login'),
    path('configuracion-cadete.html', views.configuracion_cadete, name='configuracion-cadete'),


}