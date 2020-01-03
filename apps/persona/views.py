from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import  FormularioPersona
from apps.modelo.models import Rol, Persona

def verPerfil(request):
    lista = Horario.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'principal.html', context)


