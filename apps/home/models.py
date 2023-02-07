from datetime import datetime

from apps.authentication.models import Jugador
from django.db import models
from django.utils.translation import gettext_lazy as _

class Base(models.Model):
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    jugador_creador = models.ForeignKey(Jugador, on_delete=models.PROTECT)
    
    class Meta:
        abstract = True
    
class Actividad(Base):
    nombre = models.CharField(max_length=100, blank=False) 
    
    def __str__(self):
        return self.nombre   
    
    class Meta: 
        verbose_name_plural = "Actividades"  
    
class Lugar(Base):
    nombre = models.CharField(max_length=100, blank=False)    
    
    def __str__(self):
        return self.nombre 
    
    class Meta: 
        verbose_name_plural = "Lugares"  

class Equipo(Base):
    nombre = models.CharField(max_length=100, blank=False)
    jugadores = models.ManyToManyField(Jugador, blank=True, related_name='Equipo_jugadores')
    
    def __str__(self):
        return self.nombre   

class Encuentro(Base):
    descripcion = models.CharField(max_length=100, blank=False)
    actividad = models.ForeignKey(Actividad, on_delete=models.PROTECT)
    lugar = models.ForeignKey(Lugar, on_delete=models.PROTECT)
    equipos = models.ManyToManyField(Equipo, blank=True)
    fecha = models.DateField(blank=False)
    hora = models.TimeField(blank=False)
    duracion = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.descripcion   

    class Meta: 
        verbose_name_plural = "Encuentros"
