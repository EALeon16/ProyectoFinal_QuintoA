from django.db import models

# Create your models here.
class Pelicula(models.Model):
	listaGenero =(
		('A', '"A" - Aptas para todo publico'),
		('B', '"B" - Películas para adolescentes de 12 años en adelante'),
        ('B15', '"B15" - Película no recomendable para menores de 15 años de edad'),
		('C', '"C" - Películas para adultos de 18 años en adelante'),
        ('D', '"D" - Películas para adultos, con sexo explícito'),
		
	)
	listaEstado =(
		('True', 'Si'),
		('False', 'No')
		
	)
	pelicula_id = models.AutoField(primary_key = True)
	nombre_pelicula = models.CharField(max_length=75, unique = True, null=False)
	sinopsis = models.CharField(max_length=50, null=False)
	genero = models.CharField(max_length=15, choices = listaGenero, default= '"A" - Aptas para todo publico', null=False)
	fechaLanzamiento =  models.DateField(auto_now = False, auto_now_add = False, null = False)
	duracion = models.CharField(max_length=25)
	estado = models.BooleanField(null=False, choices = listaEstado, default=True)
	director = models.CharField(max_length=25)
	protagonistas = models.TextField(max_length=50, default='n/a')
	imagen = models.ImageField(upload_to="portadas", null=True)
	

class Persona(models.Model):
	persona_id = models.AutoField(primary_key = True)
	nombres = models.CharField(max_length=75, unique = True, null=False)
	apellidos = models.CharField(max_length=50, null=False)
	fechaNacimiento =  models.DateField(auto_now = False, auto_now_add = False, null = False)
	edad = models.CharField(max_length=25)
	correo = models.EmailField(max_length = 50, null = False)
	rol = models.CharField(max_length=25)

class Sala(models.Model):
	sala_id = models.AutoField(primary_key = True)
	nombre_sala = models.CharField(max_length=75, unique = True, null=False)
	nro_asientos = models.IntegerField(max_length=50, null=False)

class Horario(models.Model):
	horario_id = models.AutoField(primary_key = True)
	hora_pelicula = models.TimeField(null=False)
	fecha_pelicua = models.DateField(auto_now = False, auto_now_add = False, null = False)
	pelicula = models.ForeignKey(
		'Pelicula', 
		on_delete = models.CASCADE,
	)
	sala = models.ForeignKey(
		'Sala', 
		on_delete = models.CASCADE,
	)
	
class Boleto(models.Model):
	listaTipoB = (
		('normal', 'Normal'),
		('especial', 'Especial'),
	)
	boleto_id = models.AutoField(primary_key = True)
	cantidad_asientos = models.IntegerField(max_length=10, null=False)
	precio_total = models.DecimalField(max_digits=10, decimal_places=3, null=False)
	tipo = models.CharField(max_length=30, choices = listaTipoB, null=False, default='Normal')
	persona = models.ForeignKey(
		'Persona', 
		on_delete = models.CASCADE,
	)
	horario = models.ForeignKey(
		'Horario', 
		on_delete = models.CASCADE,
	)
	

   

