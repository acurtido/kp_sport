from django.contrib import admin

from .models import Jugador

# class JugadorAdmin(admin.ModelAdmin):
#      list_display = ['sobrenombre']

admin.site.register(Jugador)
