# -*- encoding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Jugador(AbstractUser):
    def __str__(self):
        return self.username
    
    class Meta: 
        verbose_name_plural = "Jugadores"
    


