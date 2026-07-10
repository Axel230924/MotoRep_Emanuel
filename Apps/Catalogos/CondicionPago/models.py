from django.db import models

class CondicionPago (models.Model):
    Condicion = models.CharField(verbose_name='Condición', max_length=20, unique=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Condiciones de Pago'

    def __str__(self):
        return f"{self.Condicion}"