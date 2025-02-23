"""tacografos URL Configuration

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
from django.urls import path, include
from Orders import views
from Orders.views import inicio
from Users import views as users_views
from django.conf import settings #para imagenes
from django.conf.urls.static import static #para imagenes
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',users_views.login_request, name='login_request'),
    path('Orders/', include('Orders.urls')),
    path('Users/', include('Users.urls')),
    
    #path('Users/', include('Users.urls'))
]
handler404 = 'Orders.views.custom_404'
