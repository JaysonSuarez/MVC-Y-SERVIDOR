""""INTEGRANTES: CRISTIAN PUENTES - T00060458
	     JAYSON SUAREZ    - T00060247"""


"""Creamos el modelo"""
from django.db import models

# Create your models here.
"""Creamos la clase curso en donde se tendran los datos que se utilizaran en el programa"""


class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    """Creamos el metodo str para poder ver los datos del objeto en el servidor"""

    def __str__(self):
        texto = "{0} ({1})"

        return texto.format(self.nombre, self.creditos)
