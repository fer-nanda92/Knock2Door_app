from django.shortcuts import render

# Create your views here.

def bienvenida(request):
    return render(request, 'bienvenida.html')

from rest_framework import viewsets
from .models import (
    Rol, Usuario, PersonaNatural, EmpresaInmobiliaria,
    Propiedad, PropiedadPropietario, Visita,
    ContratoOperacion, HistorialEstadoPropiedad
)
from .serializers import (
    RolSerializer, UsuarioSerializer, PersonaNaturalSerializer,
    EmpresaInmobiliariaSerializer, PropiedadSerializer,
    PropiedadPropietarioSerializer, VisitaSerializer,
    ContratoOperacionSerializer, HistorialEstadoPropiedadSerializer
)

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PersonaNaturalViewSet(viewsets.ModelViewSet):
    queryset = PersonaNatural.objects.all()
    serializer_class = PersonaNaturalSerializer

class EmpresaInmobiliariaViewSet(viewsets.ModelViewSet):
    queryset = EmpresaInmobiliaria.objects.all()
    serializer_class = EmpresaInmobiliariaSerializer

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer

class PropiedadPropietarioViewSet(viewsets.ModelViewSet):
    queryset = PropiedadPropietario.objects.all()
    serializer_class = PropiedadPropietarioSerializer

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class ContratoOperacionViewSet(viewsets.ModelViewSet):
    queryset = ContratoOperacion.objects.all()
    serializer_class = ContratoOperacionSerializer

class HistorialEstadoPropiedadViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstadoPropiedad.objects.all()
    serializer_class = HistorialEstadoPropiedadSerializer
