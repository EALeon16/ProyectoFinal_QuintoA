from django.shortcuts import render, redirect
from django.contrib import messages
from apps.modelo.models import Pelicula, Persona, Sala, Horario

def compraBoleto(request):

   
    
    return render(request,'boleto/adquirir_boleto.html')
