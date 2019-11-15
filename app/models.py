"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Catedratico (models.Model):
    id_Catedratico = models.IntegerField (primary_key = True)
    nombre = models.CharField (max_length = 50)
    apellido = models.CharField (max_length = 50)
    telefono = models.IntegerField ()
    direccion = models.CharField (max_length = 100)

class Carrera (models.Model):
    id_Carrera = models.IntegerField (primary_key = True)
    nombre = models.CharField (max_length = 50)

class Curso(models.Model):
    id_Curso = models.IntegerField(primary_key = True)
    nombre = models.CharField (max_length = 50)
    horario = models.CharField (max_length = 50)
    catedratico = models.ForeignKey (Catedratico, on_delete=models.CASCADE)
    carrera = models.ForeignKey (Carrera, on_delete= models.CASCADE)

class Estudiante(models.Model):
    carnet = models.IntegerField (primary_key = True)
    nombre = models.CharField (max_length = 50)
    apellido = models.CharField (max_length = 50)
    direccion = models.CharField (max_length = 100)
    telefono = models.IntegerField ()
    carrera = models.ForeignKey (Carrera, on_delete = models.CASCADE)

class CursoLibre (models.Model):
    id_CursoLibre = models.IntegerField(primary_key = True)
    nombre = models.CharField (max_length = 50)
    horario = models.CharField (max_length = 50)
    catedratico = models.ForeignKey (Catedratico, on_delete=models.CASCADE)

class AsignacionCurso (models.Model):
    id_asignacion = models.AutoField (primary_key = True)
    estudiante = models.ForeignKey (Estudiante, on_delete = models.CASCADE)
    curso = models.ForeignKey (Curso, on_delete=models.CASCADE)

class AsignacionCursoLibre (models.Model):
    id_asignacionlibre = models.AutoField (primary_key = True)
    estudiante = models.ForeignKey (Estudiante, on_delete = models.CASCADE)
    cursolibre = models.ForeignKey (CursoLibre, on_delete=models.CASCADE)

class Login (models.Model):
    id_login = models.IntegerField (primary_key= True)
    id_estudiante = models.ForeignKey (Estudiante,on_delete=models.CASCADE, null=True)
    id_catedratico = models.ForeignKey (Catedratico,on_delete=models.CASCADE, null=True)
    contrasenia = models.CharField (max_length = 30)

class Formulario (models.Model):
    id_form = models.AutoField (primary_key = True)
    nombre = models.CharField (max_length = 50)
    email = models.EmailField ()
    mensaje = models.CharField (max_length = 350)

class Publicacion(models.Model):
    id_publicacion=models.AutoField (primary_key=True)
    titulo=models.CharField (max_length = 50)
    nombre_prof=models.CharField (max_length = 50)
    descripcion=models.CharField (max_length = 350)

