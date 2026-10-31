from django.contrib import admin
from .models import Consejo


@admin.register(Consejo)
class ConsejoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo', 'creado')
    list_filter = ('activo',)
    search_fields = ('titulo', 'descripcion')
