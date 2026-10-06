from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RolViewSet, UsuarioViewSet, PersonaNaturalViewSet,
    EmpresaInmobiliariaViewSet, PropiedadViewSet,
    PropiedadPropietarioViewSet, VisitaViewSet,
    ContratoOperacionViewSet, HistorialEstadoPropiedadViewSet
)

router = DefaultRouter()
router.register(r'roles', RolViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'personas-naturales', PersonaNaturalViewSet)
router.register(r'empresas-inmobiliarias', EmpresaInmobiliariaViewSet)
router.register(r'propiedades', PropiedadViewSet)
router.register(r'propiedad-propietarios', PropiedadPropietarioViewSet)
router.register(r'visitas', VisitaViewSet)
router.register(r'contratos', ContratoOperacionViewSet)
router.register(r'historiales', HistorialEstadoPropiedadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
