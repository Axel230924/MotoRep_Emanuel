from django.db import models
from Apps.Catalogos.Marca.models import Marca

class Moto(models.Model):
    Modelo = models.CharField(max_length=30, verbose_name='Modelo de la Moto')
    Año = models.IntegerField(verbose_name='Año de Fabricación')
    MarcaId = models.ForeignKey(Marca, on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Modelo} - {self.MarcaId.Nombre}"