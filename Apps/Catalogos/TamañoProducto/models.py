from django.db import models

class TamañoProducto (models.Model):
    Tamaño = models.CharField(verbose_name='Tamaño', max_length=30, unique=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Tamaños de Producto'

    def __str__(self):
        return f"{self.Tamaño}"