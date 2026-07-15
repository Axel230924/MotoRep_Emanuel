from django.db import models

class TamañoProducto (models.Model):
    Tamaño = models.CharField(verbose_name='Tamaño del producto', max_length=30, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Tamaño de Producto'

    def __str__(self):
        return f"{self.Tamaño}"