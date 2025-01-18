from django.db import models
import datetime
import os
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField

# Create your models here.


class Profile (models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    agente = models.CharField(max_length=5)
    responsable = models.CharField(max_length=40)
    razon_social = models.CharField(max_length=60)
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=60)
    provincia = models.CharField(max_length=60)
    pais = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    tel1 = models.IntegerField()
    tel2 = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'Usuario: {self.usuario} | agente: {self.agente}'

class Pais (models.Model):
    pais = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.pais}'

class Provincia (models.Model):
    provincia = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.provincia}'
