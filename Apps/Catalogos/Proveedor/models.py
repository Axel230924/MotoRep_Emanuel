from django.db import models

class Proveedor (models.Model):
    Nombre = models.CharField(verbose_name='Nombres', max_length=30,)
    NumTelefono = models.IntegerField(verbose_name='Número de Teléfono', null=True, blank=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.Nombre}"