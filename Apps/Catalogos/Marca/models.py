from django.db import models
from Apps.Catalogos.TipoMarca.models import TipoMarca

class Marca(models.Model):
    Nombre = models.CharField(max_length=50, verbose_name='Nombre de la Marca', unique=True)
    TipoMarcaId = models.ForeignKey(TipoMarca, on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Marcas'

        def __str__(self):
            return f"{self.Nombre}"