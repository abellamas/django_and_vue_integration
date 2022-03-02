from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Alumnos(models.Model):
  
  dni = models.CharField(max_length=8, primary_key=True, unique=True)
  
  apellidos = models.CharField(max_length=50, null=False,blank=False)
  
  nombres = models.CharField(max_length=100, null=False,blank=False)
  
  direccion = models.CharField(max_length=100, null=False,blank=True)
  
  localidad = models.CharField(max_length=50, null=False,blank=True)
  
  telefono = models.CharField(max_length=50,null=False,blank=True)
  
  email = models.EmailField(max_length=254, null=False,blank=True)
  
  fnac = models.DateField(verbose_name="Fecha de Nacimiento",null=False,blank=True)
  
  def __str__(self):
    return f'{self.apellido}, {self.nombres} - {self.dni}'

  class Meta():
    verbose_name = 'Alumno'
    verbose_name_plural = 'Alumnos'
    
class Asignaturas(models.Model):
  id_asignatura = models.CharField(max_length=3, primary_key=True)
  nombre_asignatura = models.CharField(max_length=50, null=False,blank=False)
  cuatrimestre = models.CharField(max_length=4,null=False,blank=False)
  carga_horaria = models.IntegerField(null=False,blank=False)
     
class Calificaciones(models.Model):
  id_asignatura = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)
  id_alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
  calificacion = models.IntegerField(null=False,blank=False)