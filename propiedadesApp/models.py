from django.db import models


class Propiedad(models.Model):
    TIPO_CHOICES = [
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
        ('Parcela', 'Parcela'),
        ('Oficina', 'Oficina'),
        ('Terreno', 'Terreno'),
    ]
    OPERACION_CHOICES = [
        ('Venta', 'Venta'),
        ('Arriendo', 'Arriendo'),
    ]

    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    operacion = models.CharField(max_length=20, choices=OPERACION_CHOICES, default='Venta')
    comuna = models.CharField(max_length=80)
    sector = models.CharField(max_length=100, blank=True)
    precio = models.DecimalField(max_digits=14, decimal_places=0)
    dormitorios = models.PositiveIntegerField(default=0)
    banos = models.PositiveIntegerField(default=0)
    superficie = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descripcion = models.TextField(blank=True)
    imagen = models.CharField(max_length=255, blank=True, help_text='Ruta de imagen dentro de static/img/')
    destacada = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)
    actualizada = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-destacada', '-creada']
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    def __str__(self):
        return f'{self.titulo} - {self.comuna}'

    @property
    def precio_formateado(self):
        return f'${self.precio:,.0f}'.replace(',', '.')


class SolicitudVisita(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='solicitudes')
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)
    fecha_preferida = models.DateField(null=True, blank=True)
    mensaje = models.TextField(blank=True)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creada']
        verbose_name = 'Solicitud de visita'
        verbose_name_plural = 'Solicitudes de visita'

    def __str__(self):
        return f'{self.nombre} - {self.propiedad.titulo}'
