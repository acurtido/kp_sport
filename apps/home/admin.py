from django.contrib import admin

from .models import Equipo, Encuentro, Actividad, Lugar

admin.site.register(Equipo)
admin.site.register(Encuentro)
admin.site.register(Actividad)
admin.site.register(Lugar)
