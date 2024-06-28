from main.models import *

def crear_artista(nombre:str, apellido:str, cantante:bool, instrumento:str):
    artista = Artista(nombre=nombre, apellido=apellido, cantante=cantante, instrumento=instrumento)
    artista.save()
    return artista

def crear_grupo(nombre:str, fecha_creacion:str):
    grupo = Grupo(nombre=nombre, fecha_creacion=fecha_creacion)
    grupo.save()
    return grupo

def relacion_artista_grupo(artista_id:int, grupo_id:int, fecha_ingreso:str, agregado_por:str):
    relacion = ArtistaGrupo(artista=artista_id, grupo=grupo_id, fecha_ingreso=fecha_ingreso, agregado_por=agregado_por)
    relacion.save()

def agregar_album(titulo:str, year:int, grupo_id:int):
    album = Album(titulo=titulo, year=year, grupo_id=grupo_id)
    album.save()
    print(album)

def obtiene_artistas(nombre:str):
    artistas = Artista.objects.filter(nombre__contains=nombre) # Contiene
    print(artistas)

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