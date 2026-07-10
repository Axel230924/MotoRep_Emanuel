from django.db import models

class Caja (models.Model):
    NumCaja = models.IntegerField(verbose_name='Número de Caja', unique=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Cajas'

    def __str__(self):
        return f"{self.NumCaja}"