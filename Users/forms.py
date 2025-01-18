from dataclasses import fields
from logging import PlaceHolder
from multiprocessing.sharedctypes import Value
from platform import architecture
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class Login_formulario (AuthenticationForm):   
    class Meta:
        model = User
        fields = ['username', 'password']