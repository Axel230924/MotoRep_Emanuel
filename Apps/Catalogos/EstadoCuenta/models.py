from django.db import models

class EstadoCuenta (models.Model):
    DescripcionEstado = models.CharField(verbose_name='Descripción del Estado', max_length=30, unique=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Estados de Cuenta'

    def __str__(self):
        return f"{self.DescripcionEstado}"