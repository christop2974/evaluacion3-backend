from django.contrib import admin
from .models import Propiedad, SolicitudVisita


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'operacion', 'comuna', 'precio', 'destacada', 'creada')
    list_filter = ('tipo', 'operacion', 'comuna', 'destacada')
    search_fields = ('titulo', 'comuna', 'sector', 'descripcion')
    list_editable = ('destacada',)
    ordering = ('-creada',)


@admin.register(SolicitudVisita)
class SolicitudVisitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'propiedad', 'fecha_preferida', 'creada')
    list_filter = ('fecha_preferida', 'creada')
    search_fields = ('nombre', 'email', 'telefono', 'propiedad__titulo')
    autocomplete_fields = ('propiedad',)
