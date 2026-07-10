from django.db import models

class MetodoPago (models.Model):
    Metodo = models.CharField(verbose_name='Método', max_length=50, unique=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Métodos de Pago'

    def __str__(self):
        return f"{self.Metodo}"