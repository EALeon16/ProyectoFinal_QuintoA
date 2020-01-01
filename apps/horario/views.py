from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioHorario, FormularioHorario
from apps.modelo.models import Horario, Pelicula, Sala


def agregarHorario(request):
    
    """lista = Pelicula.objects.all()
    
listas = Sala.objects.all()
    formulario_horario = FormularioHorario(request.POST)
    if request.method == 'POST':
        if formulario_horario.is_valid():
            datosH = formulario_horario.cleaned_data
            horario = Horario()
            horario.hora_pelicula = datosH.get('hora_pelicula')
            horario.fecha_pelicua = datosH.get('fecha_pelicua')
            horario.sala_id = datosH.get('sala')
            horario.sala_id = datosH.get('sala')
            horario.save()
            messages.success(request, 'Horario registrado correctamente')
            return redirect(verPelicula)
        else:
            messages.error(request, 'Esta pelicula ya esta registrada')
               

    fecha = []
    context = {
        'lista' : lista,
        'listas': listas,
    }
    
    return render(request,'horario/agregar_horario.html')"""



