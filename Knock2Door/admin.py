from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import (
    Rol, Usuario, PersonaNatural, EmpresaInmobiliaria,
    Propiedad, PropiedadPropietario, Visita,
    ContratoOperacion, HistorialEstadoPropiedad
)

admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(PersonaNatural)
admin.site.register(EmpresaInmobiliaria)
admin.site.register(Propiedad)
admin.site.register(PropiedadPropietario)
admin.site.register(Visita)
admin.site.register(ContratoOperacion)
admin.site.register(HistorialEstadoPropiedad)


