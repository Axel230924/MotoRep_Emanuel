from django.db import models

class Cliente (models.Model):
    Nombre = models.CharField(verbose_name='Nombres', max_length=30,)
    Apellido = models.CharField(verbose_name='Apellidos', max_length=30,)
    NumCedula = models.CharField(verbose_name='Número de Cédula', max_length=20, unique=True, null=True, blank=True)
    NumTelefono = models.IntegerField(verbose_name='Número de Teléfono', null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.Nombre} - {self.Apellido}"