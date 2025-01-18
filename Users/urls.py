from django.urls import path
from . import views


urlpatterns = [
    path('perfil', views.perfil, name='perfil'),
    path('logout', views.logout_user, name='Logout'),
    path('puestos', views.puestos, name="puestos")
    ]