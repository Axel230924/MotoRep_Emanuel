from django.db import models

class Proveedor (models.Model):
    Nombre = models.CharField(verbose_name='Nombre de proveedor', max_length=30,)
    NumTelefono = models.IntegerField(verbose_name='Número de Teléfono', null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.Nombre}"