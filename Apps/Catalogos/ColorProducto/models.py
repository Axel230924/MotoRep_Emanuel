from django.db import models

class ColorProducto (models.Model):
    Color = models.CharField(verbose_name='Colores', max_length=20,)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Colores de Producto'

    def __str__(self):
        return f"{self.Color}"