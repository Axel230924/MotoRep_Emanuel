from django.db import models

class Empleado (models.Model):
    Nombre = models.CharField(verbose_name='Nombres', max_length=30,)
    Apellido = models.CharField(verbose_name='Apellidos', max_length=30,)
    NumCedula = models.CharField(verbose_name='Número de Cédula', max_length=20, unique=True)
    NumTelefono = models.IntegerField(verbose_name='Número de Teléfono',)
    Direccion = models.CharField(verbose_name='Dirección', max_length=100,)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f"{self.Nombre} - {self.Apellido}"