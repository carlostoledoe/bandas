from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cantante = models.BooleanField(default=False)
    instrumento = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    artista = models.ManyToManyField(Artista, related_name='grupos', through='ArtistaGrupo')
    def __str__(self) -> str:
        return f'{self.nombre}'

class Album(models.Model):
    titulo = models.CharField(max_length=50)
    year = models.IntegerField()
    grupo = models.ForeignKey(Grupo, related_name='albumes', on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.titulo} {self.year} {self.grupo}'

class ArtistaGrupo(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    # artista_id int
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    # grupo_id int
    fecha_ingreso = models.DateField()
    creacion_registro = models.DateField(auto_now_add=True)
    agregado_por = models.CharField(max_length=50)
