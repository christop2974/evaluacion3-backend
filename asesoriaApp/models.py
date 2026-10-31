from django.db import models


class Consejo(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Consejo'
        verbose_name_plural = 'Consejos'

    def __str__(self):
        return self.titulo
