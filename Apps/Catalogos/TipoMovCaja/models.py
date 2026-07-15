from django.db import models

class TipoMovCaja (models.Model):
    TipoMov = models.CharField(verbose_name='Tipo de Movimiento', max_length=30, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Tipos de Movimiento en Caja'

    def __str__(self):
        return f"{self.TipoMov}"