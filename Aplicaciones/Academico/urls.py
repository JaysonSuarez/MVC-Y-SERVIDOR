""""INTEGRANTES: CRISTIAN PUENTES - T00060458
	     JAYSON SUAREZ    - T00060247"""


"""Creamos las rutas a utilizar en el programa"""
from django.urls import path
from . import views

"""Con urlpatterns nos encargamos de definir las vistas"""
urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso)
]
