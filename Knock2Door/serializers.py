from rest_framework import serializers
from .models import (
    Rol, Usuario, PersonaNatural, EmpresaInmobiliaria,
    Propiedad, PropiedadPropietario, Visita,
    ContratoOperacion, HistorialEstadoPropiedad
)

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PersonaNaturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaNatural
        fields = '__all__'

class EmpresaInmobiliariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaInmobiliaria
        fields = '__all__'

class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'

class PropiedadPropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropiedadPropietario
        fields = '__all__'

class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__'

class ContratoOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratoOperacion
        fields = '__all__'

class HistorialEstadoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstadoPropiedad
        fields = '__all__'
        