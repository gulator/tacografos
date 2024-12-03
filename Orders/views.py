from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from . import views

# Create your views here.

def inicio (request):
    return render(
        request, "index.html"
    )