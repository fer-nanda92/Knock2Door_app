from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# ==========================================
# 1. ROL Y USUARIOS
# ==========================================

class Rol(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('NATURAL', 'Persona Natural'),
        ('EMPRESA', 'Empresa Inmobiliaria'),
        ('AGENTE', 'Agente Inmobiliario'),
        ('ADMIN', 'Administrador'),
    ]

    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=False)
    contrasena_hash = models.CharField(max_length=128, null=False)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, null=False)
    estado_activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class PersonaNatural(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    rut_dni = models.CharField(max_length=20, unique=True, null=False)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=25, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class EmpresaInmobiliaria(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    rut_empresa = models.CharField(max_length=20, unique=True, null=False)
    razon_social = models.CharField(max_length=150, null=False)
    nombre_fantasia = models.CharField(max_length=150, null=False)
    telefono_contacto = models.CharField(max_length=25, null=False)
    direccion_comercial = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razon_social


# ==========================================
# 2. PROPIEDADES Y PROPIETARIOS
# ==========================================

class Propiedad(models.Model):
    TIPO_INMUEBLE_CHOICES = [
        ('CASA', 'Casa'),
        ('DEPARTAMENTO', 'Departamento'),
        ('TERRENO', 'Terreno'),
        ('OFICINA', 'Oficina'),
        ('BODEGA', 'Bodega'),
    ]

    TIPO_OPERACION_CHOICES = [
        ('VENTA', 'Venta'),
        ('ARRIENDO', 'Arriendo'),
        ('AMBOS', 'Ambos'),
    ]

    ESTADO_PROPIEDAD_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADA', 'Reservada'),
        ('ARRENDADA', 'Arrendada'),
        ('VENDIDA', 'Vendida'),
        ('INACTIVA', 'Inactiva'),
    ]

    agente_asignado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='propiedades_asignadas')
    codigo_interno = models.CharField(max_length=25, unique=True, null=False)
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE_CHOICES, null=False)
    tipo_operacion = models.CharField(max_length=20, choices=TIPO_OPERACION_CHOICES, null=False)
    direccion = models.CharField(max_length=255, null=False)
    comuna_ciudad = models.CharField(max_length=100, null=False)
    precio = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    habitaciones = models.IntegerField(default=0)
    banos = models.IntegerField(default=0)
    superficie_m2 = models.FloatField(null=False)
    es_publica = models.BooleanField(default=True)
    estado_propiedad = models.CharField(max_length=20, choices=ESTADO_PROPIEDAD_CHOICES, default='DISPONIBLE')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo_interno} - {self.direccion}"


class PropiedadPropietario(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    porcentaje_propiedad = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


# ==========================================
# 3. VISITAS Y OPERACIONES
# ==========================================

class Visita(models.Model):
    ESTADO_VISITA_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
        ('REPROGRAMADA', 'Reprogramada'),
    ]

    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    agente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='visitas_agente')
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='visitas_cliente')
    fecha_programada = models.DateTimeField(null=False)
    estado_visita = models.CharField(max_length=20, choices=ESTADO_VISITA_CHOICES, default='PENDIENTE')
    comentarios_agente = models.TextField(max_length=500, null=True, blank=True)
    calificacion_cliente = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class ContratoOperacion(models.Model):
    TIPO_CONTRATO_CHOICES = [
        ('VENTA', 'Venta'),
        ('ARRIENDO', 'Arriendo'),
    ]

    ESTADO_CONTRATO_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('VIGENTE', 'Vigente'),
        ('FINALIZADO', 'Finalizado'),
        ('ANULADO', 'Anulado'),
    ]

    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos_cliente')
    agente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='contratos_agente')
    tipo_contrato = models.CharField(max_length=20, choices=TIPO_CONTRATO_CHOICES, null=False)
    monto_total = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=True, blank=True)
    estado_contrato = models.CharField(max_length=20, choices=ESTADO_CONTRATO_CHOICES, default='BORRADOR')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


# ==========================================
# 4. AUDITORÍA E HISTORIAL
# ==========================================

class HistorialEstadoPropiedad(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    usuario_cambio = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado_anterior = models.CharField(max_length=20, null=False)
    estado_nuevo = models.CharField(max_length=20, null=False)
    fecha_cambio = models.DateTimeField(default=timezone.now)
    motivo = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    
