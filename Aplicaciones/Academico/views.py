""""INTEGRANTES: CRISTIAN PUENTES - T00060458
	     JAYSON SUAREZ    - T00060247"""


"""Creamos la vista"""
from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages


"""creamos la funcion home la cual tendra qie recibir un request para renderisar la plantilla gestionCursos.html """


def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})


"""Creamos la funcion registrarCurso la cual es la que recibira los datos por medio del POST"""


def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    """Igualamos los parametros inicializados con los obtenidos y los redirigimos a la raiz"""
    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')


"""Con esta vista dividimos el trabajo en dos, en esta fraccion solo se efectuaria la busqueda del parametro"""


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


"""En esta segunda parte recibimos lor parametros, los listamos y los guardamos con el uso del metodo .save()"""


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')


"""Hacemos una vista que use el codigo para buscar el parametro, referenciarlo y por ultimo eliminarlo para luego
redireccionar a la raiz """


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')
