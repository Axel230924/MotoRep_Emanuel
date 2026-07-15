from django.db import models

class Categoria (models.Model):
    Nombre = models.CharField(verbose_name='Nombres', max_length=30, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f"{self.Nombre}"