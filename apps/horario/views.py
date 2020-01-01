from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioHorario, FormularioHorario
from apps.modelo.models import Horario, Pelicula, Sala


def agregarHorario(request):
    lista = Pelicula.objects.all()
    listas= Sala.objects.all()
    formulario_horario = FormularioHorario(request.POST)
    if request.method == 'POST':
        if formulario_horario.is_valid():
            datos = formulario_horario.cleaned_data
            horario = Horario()
            horario.hora_pelicula = datos.get('hora_pelicula')
            horario.fecha_pelicua = datos.get('fecha_pelicua')
            horario.pelicula = datos.get('pelicula')
            horario.sala = datos.get('sala')
            horario.save()
            messages.success(request, 'Horario registrado correctamente')
            return redirect('/cartelera')
        else:
            messages.error(request, 'Esta pelicula ya esta registrada')
                 
   
    
    context = {
        'f': formulario_horario,
        'lista': lista,
        'listas': listas
    }
    
    return render(request,'horario/agregar_horario.html', context)



