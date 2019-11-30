from django.shortcuts import render, redirect
from .forms import FormularioPelicula, FormularioPersona, FormularioEditarPelicula
from apps.modelo.models import Pelicula, Persona


def principal(request):
    lista = Pelicula.objects.filter(proyeccion = 'si')
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
            pelicula.genero = datos.get('genero')
            pelicula.sinopsis = datos.get('sinopsis')
            pelicula.clasificacion = datos.get('clasificacion')
            pelicula.fechaLanzamiento = datos.get('fechaLanzamiento')
            pelicula.duracion = datos.get('duracion')
            pelicula.proyeccion = datos.get('proyeccion')
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
    nombre = request.GET['nombre_pelicula']
    pelicula = Pelicula.objects.get(nombre_pelicula = nombre)
    if request.method == 'POST':
        formulario_editar = FormularioEditarPelicula(request.POST)
        if formulario_editar.is_valid():
            datos = formulario_editar.cleaned_data
            pelicula.proyeccion = datos.get('proyeccion')
            pelicula.save()
            return redirect(verPelicula)
    else:
        formulario_editar = FormularioEditarPelicula(instance = pelicula)
    context = {
        'f': formulario_editar 
    }

    return render(request,'pelicula/editar_pelicula.html', context)

def verPelicula(request):
    lista = Pelicula.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'pelicula/ver_pelicula.html', context)

def verSala(request):
    lista = Pelicula.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'salas/ver_salas.html', context)

def agregarSala(request):
    lista = Pelicula.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request,'salas/agregar_sala.html', context)


