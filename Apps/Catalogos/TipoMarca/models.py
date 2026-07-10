from django.db import models

class TipoMarca (models.Model):
    Tipo = models.CharField(verbose_name='Tipo', max_length=20, unique=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Tipos de Marca'

    def __str__(self):
        return f"{self.Tipo}"