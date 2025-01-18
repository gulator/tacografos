from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from Users.models import *
from Orders.models import *
from Users.forms import *
from . import views

# Create your views here.

def perfil (request):
    usuario = request.user
    pais = Pais.objects.all().order_by("pais")
    provincia = Provincia.objects.all()
    profile = Profile.objects.get(user=usuario)
    
    print({"profile":profile})
    return render(request,"perfil.html",{"pais":pais, "provincia":provincia,"profile":profile})

def login_request(request):
    
    if request.user.is_authenticated:
        if request.user.is_staff:
            ordenes = Order.objects.all().order_by('orden')
        else:
            ordenes = Order.objects.filter(user=request.user).order_by('orden')
            return render(request, 'orders.html', {"ordenes":ordenes})
    else:
        if request.method == "POST":

            formulario = Login_formulario(request, data=request.POST)

            if formulario.is_valid():
                usuario = formulario.cleaned_data.get("username")
                contrasenia = formulario.cleaned_data.get("password")

                user = authenticate(username=usuario, password=contrasenia)

                if user is not None:
                    login(request, user)
                    if request.user.is_staff:
                        ordenes = Order.objects.all().order_by('-id')
                    else:
                        ordenes = Order.objects.filter(user=request.user).order_by('-id')
                    return render(request, 'orders.html',{"ordenes":ordenes})
                else:
                    return render(
                        request, "index.html", {"mensaje": "Error. Formulario erroneo."}
                    )

            else:
                formulario = Login_formulario()
                return render(
                    request,
                    "index.html",
                    {
                        "formulario": formulario,
                        "mensaje": "Error. Datos de ingreso incorrectos",
                    },
                )

        formulario = Login_formulario()
        
        return render(request, "index.html", {"formulario": formulario})
    
def logout_user (request):
    logout(request)

    return redirect("login_request")

def puestos (request):
    perfiles = Profile.objects.all()
    tipo_usuario = User.objects.all()
    non_superuser_users = tipo_usuario.filter(is_superuser=False)
    usuarios = perfiles.filter(user__in=non_superuser_users).order_by('provincia', 'localidad')


    return render (request, "puestos.html", {"usuarios":usuarios})