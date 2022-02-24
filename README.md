# MVC-Y-SERVIDOR
INTEGRANTES: CRISTIAN PUENTES - T00060458
	     JAYSON SUAREZ    - T00060247

La aplicación desarrollada tiene como fin realizar el modelo Cliente-Servidor y
MVC/MVT dandonos una interfaz en un servidor de DJango donde se mostrara el una
interfaz que nos permitira digitar los datos de una materia, teniendo solo 3
parametros principales, los cuales son: Codigo, Nombre y Creditos. Permitiendo
digitar, editar, eliminar y desplegar en pantalla los datos digitados (CRUD).

El programa utiliza la funcionalidad de Django para utilizar el patron MVT por
lo que utilizando plantillas, se puede crear un proyecto que no este desde
cero ahorrandonos codigo ya que nos proporciona los archivos.py para trabajar
y tambien hace uso de un servidor SQL en donde se almacenaran los datos que
son suministrados.

Frameworks, lenguages y programas utilizados: 
Django, SQLite3,ORM, Bootstrap, JavaScript, HTML, Python.

Los archivos trabajados con python y suministrado con la notancion pep8 son los
archivos.py que estan en la carpeta Academico, los demas archivos.py son creados
automaticamente por las plantillas predeterminadas proporcionadas por Django
al igual que el servidor del programa, siendo los archivos que los archivos en
donde se codifico son:

models.py, urls.py, urls.py(plantilla de Django en la carpeta universidad),

gestionCursos.html, gestionCursos.css, base.html, gestionCursos.js,views.py,

edicionCurso.html y admin.py

Comando para que se Ejecute el programa:

python manage.py runserver
