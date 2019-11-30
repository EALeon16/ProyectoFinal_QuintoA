from django import forms 
from apps.modelo.models import Pelicula, Persona, Sala
class FormularioPelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ["nombre_pelicula", "genero","sinopsis", "clasificacion", "proyeccion","fechaLanzamiento","duracion","director","protagonistas","imagen"]

class FormularioEditarPelicula(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ["proyeccion"]

class FormularioPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["nombres", "apellidos", "fechaNacimiento", "edad","correo"]

class FormularioSala(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ["nombre_sala", "nro_asientos"]

        





