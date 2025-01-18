from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from Orders.models import *
from Users.models import *
from Orders.forms import *
from . import views
import datetime
import random
import string
import csv

# Create your views here.
def nro_orden ():
    
    hora = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # hora = datetime.datetime.now().strftime('m%d_%H-%M-%S')
    letras = ''.join(random.choices(string.ascii_uppercase, k=4))
    return hora + letras


def inicio (request):
    return render(
        request, "index.html"
    )
def orders (request):
    if request.user.is_staff:
        ordenes = Order.objects.all().order_by('-id')        
    else:
        ordenes = Order.objects.filter(user=request.user).order_by('-id')
    return render(
        request, "orders.html",{"ordenes": ordenes}
    )

def new_order (request):
    ano = Ano.objects.all().order_by('-ano_vehiculo')
    marca = Marca.objects.all().order_by('marca_vehiculo')
    if request.method == "POST":
        order = NewOrder(request.POST)

        if order.is_valid():
            datos = order.cleaned_data
            perfil = Profile.objects.get(user=request.user)
            nueva_orden = Order(
                user = request.user,
                puesto = perfil.razon_social,
                orden = nro_orden(),
                dominio = datos["dominio"],
                chasis = datos["chasis"],
                marca_vehiculo = datos["marca_vehiculo"],
                modelo_vehiculo = datos["modelo_vehiculo"],
                ano_vehiculo = datos["ano_vehiculo"],
                operador = datos["operador"],
                cuit = datos["cuit"],
                marca_tacografo = datos["marca_tacografo"],
                modelo_tacografo = datos["modelo_tacografo"],
                sn = datos["sn"],
                factor_k = datos["factor_k"],
                rodado = datos["rodado"],
                limite_v = datos["limite_v"],
                fecha = datos["fecha"],
                ot = datos["ot"]
            )            
            nueva_orden.save()
        else:            
            return render(request,"new-order.html", {'ano':ano,'marca':marca,'order':order})
    return render(request,"new-order.html", {'ano':ano,'marca':marca})

def edit_order (request, id):
    order = Order.objects.get(id=id)
    ano = Ano.objects.all().order_by('-ano_vehiculo')
    marca = Marca.objects.all().order_by('marca_vehiculo')

    if request.method == "POST":
        edited_order = EditOrder(request.POST)
        if edited_order.is_valid():
            datos = edited_order.cleaned_data                       
            
            order.dominio = datos["dominio"]
            order.chasis = datos["chasis"]
            order.marca_vehiculo = datos["marca_vehiculo"]
            order.modelo_vehiculo = datos["modelo_vehiculo"]
            order.ano_vehiculo = datos["ano_vehiculo"]
            order.operador = datos["operador"]
            order.cuit = datos["cuit"]
            order.marca_tacografo = datos["marca_tacografo"]
            order.modelo_tacografo = datos["modelo_tacografo"]
            order.sn = datos["sn"]
            order.factor_k = datos["factor_k"]
            order.rodado = datos["rodado"]
            order.limite_v = datos["limite_v"]
            order.fecha = datos["fecha"]
            order.ot = datos["ot"]
                        
            order.save()
            if request.user.is_staff:
                ordenes = Order.objects.all().order_by('-id')
            else:
                ordenes = Order.objects.filter(user=request.user).order_by('-id')
            return render(
                request, "orders.html",{"ordenes": ordenes}
            )
        else:            
            return render(request,"edit-order.html", {"ano":ano,"marca":marca,"edited_order":edited_order})
    return render(request,"edit-order.html", {"ano":ano,"marca":marca,"order":order})

def print_order (request, id):
    usuario = Profile.objects.get(user=request.user)
    order = Order.objects.get(id=id)
    return render(request,"print-order.html",{"order":order,"usuario":usuario})

def ordenes_csv (request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=ordenesPACs.csv'

    writer = csv.writer(response)

    writer.writerow (['Usuario','Razon Social','Nro Orden Int.','Dominio','Chasis','Marca Vehiculo','Modelo Vehiculo','Año','Operador','CUIT','Marca Tacografo', 'Modelo', 'SN', 'Factor K','Rodado','Limite Vel.','Fecha','Orden Trabajo'])

    # usuarios = User.objects.all()
    
    orden = Order.objects.all()
    perfiles = Profile.objects.all()

    #for u, p in zip(usuarios,perfil):
    for x in orden:
        for p in perfiles:
            if (x.user == p.user):
                writer.writerow([x.user,p.razon_social, x.orden, x.dominio, x.chasis, x.marca_vehiculo, x.modelo_vehiculo, x.ano_vehiculo, x.operador, x.cuit,x.marca_tacografo,x.modelo_tacografo, x.sn,x.factor_k,x.rodado,x.limite_v,x.fecha,x.ot])

    return response

def search_order (request):
    if request.GET["dominio"]:
        patente = request.GET["dominio"]
        alerta = f'No se han encontrado órdenes para la patente "{patente}".'

        if request.user.is_staff:
            ordenes = Order.objects.filter(dominio__icontains=patente).order_by('dominio')
            if ordenes:
                return render (request, "orders.html",{"ordenes": ordenes})
            else:
                ordenes = Order.objects.all().order_by('-id')
                return render (request, "orders.html",{"ordenes": ordenes, "alerta":alerta})

        else:
            ordenes = Order.objects.filter(user=request.user,dominio__icontains=patente).order_by('dominio')
            if ordenes:
                return render (request, "orders.html",{"ordenes": ordenes})
            else:
                ordenes = Order.objects.filter(user=request.user).order_by('-id')
                return render (request, "orders.html",{"ordenes": ordenes, "alerta":alerta})
    else:
        alerta2 = f'Debe ingresar un número de patente'
        if request.user.is_staff:
            ordenes = Order.objects.all().order_by('-id')        
        else:
            ordenes = Order.objects.filter(user=request.user).order_by('-id')
        return render(
            request, "orders.html",{"ordenes": ordenes, "alerta2":alerta2}
    )

def shop (request, id):
    puesto = Profile.objects.get(id=id)
    return render (request,"puesto-detail.html", {"puesto":puesto})

def custom_404(request, exception):
    return render(request, '404.html', status=404)