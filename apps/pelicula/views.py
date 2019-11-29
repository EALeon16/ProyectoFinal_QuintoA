from django.shortcuts import render, redirect
from .forms import FormularioPelicula, FormularioPersona
from apps.modelo.models import Pelicula, Persona


def principal(request):
    lista = Pelicula.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'principal.html', context)

def registrarse(request):
    formularioP = FormularioPersona(request.POST)
    return render(request,'persona/registrar_persona.html')

def registrarPelicula(request):
    formulario_pelicula = FormularioPelicula(request.POST, request.FILES)
    if request.method == 'POST':
        if formulario_pelicula.is_valid():
            datos = formulario_pelicula.cleaned_data
            pelicula = Pelicula()
            pelicula.nombre_pelicula = datos.get('nombre_pelicula')
            pelicula.sinopsis = datos.get('sinopsis')
            pelicula.genero = datos.get('genero')
            pelicula.fechaLanzamiento = datos.get('fechaLanzamiento')
            pelicula.duracion = datos.get('duracion')
            pelicula.estado = True
            pelicula.director = datos.get('director')
            pelicula.protagonistas = datos.get('protagonistas')
            pelicula.imagen = datos.get('imagen')
            pelicula.save()
            return redirect(principal)
    context = {
        'f': formulario_pelicula 
    }

    return render(request,'pelicula/registrar_pelicula.html', context)

def editarPelicula(request):
    formulario_pelicula = FormularioPelicula(request.POST) 
    context = {
        'f': formulario_pelicula 
    }

    return render(request,'pelicula/editar_pelicula.html', context)

def verPelicula(request):
    lista = Pelicula.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'pelicula/ver_pelicula.html', context)


