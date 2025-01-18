from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.

class Order (models.Model):
    user = models.ForeignKey (User,null=True, on_delete = models.CASCADE)
    puesto = models.CharField(max_length=40)
    orden = models.CharField(max_length=19, null=True, blank=True)
    dominio = models.CharField(max_length=10)
    chasis = models.CharField(max_length=25)
    marca_vehiculo = models.CharField(max_length=20)
    modelo_vehiculo = models.CharField(max_length=20)
    ano_vehiculo = models.IntegerField()
    operador = models.CharField(max_length=30)
    cuit = models.CharField(max_length=11)
    marca_tacografo = models.CharField(max_length=20)
    modelo_tacografo = models.CharField(max_length=20)
    sn = models.CharField(max_length=26)
    factor_k = models.CharField(max_length=6)
    rodado = models.CharField(max_length=16, null=True, blank=True)
    limite_v = models.CharField(max_length=10, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    ot = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.user} | {self.dominio} | {self.fecha}'

class Marca (models.Model):
    marca_vehiculo = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.marca_vehiculo}'

class Ano (models.Model):
    ano_vehiculo = models.IntegerField()

    def __str__(self):
        return f'{self.ano_vehiculo}'