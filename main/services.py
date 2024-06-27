from main.models import *

def crear_artista(nombre, apellido, cantante, instrumento):
    artista = Artista(nombre=nombre, apellido=apellido, cantante=cantante, instrumento=instrumento)
    artista.save()
    return artista

def crear_grupo(nombre, fecha_creacion):
    grupo = Grupo(nombre=nombre, fecha_creacion=fecha_creacion)
    grupo.save()

def relacion_artista_grupo(artista, grupo, fecha_ingreso, creacion_registro, agregado_por):
    relacion = ArtistaGrupo(artista=artista, grupo=grupo, fecha_ingreso=fecha_ingreso, creacion_registro=creacion_registro, agregado_por=agregado_por)
    relacion.save()

def agregar_album(titulo, year, grupo_id):
    album = Album(titulo=titulo, year=year, grupo_id=grupo_id)
    album.save()

def obtiene_artista():
    pass

def obtiene_grupo():
    pass

def artista_pertenece_a_grupos():
    pass

def artista_participa_albumes():
    pass

def grupo_albumes():
    pass


'''
TIP: En las funciones en que creamos un objeto, sería una buena práctica para
este ejemplo, retornar el elemento creado, con el fin de obtener los índices para
crear los otros registros.
'''