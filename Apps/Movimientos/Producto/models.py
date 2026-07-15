from django.db import models
from Apps.Catalogos.Marca.models import Marca
from Apps.Catalogos.Moto.models import Moto
from Apps.Catalogos.ColorProducto.models import ColorProducto
from Apps.Catalogos.TamañoProducto.models import TamañoProducto
from Apps.Catalogos.Categoria.models import Categoria

class Producto(models.Model):
    Nombre = models.CharField(max_length=30, verbose_name='Nombre del Producto')
    Codigo = models.CharField(max_length=30, verbose_name='Codigo del Producto')
    CategoriaId = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.Nombre
    
class DetalleProducto(models.Model):
    ProductoId = models.ForeignKey(Producto, on_delete=models.PROTECT)
    MarcaId = models.ForeignKey(Marca, on_delete=models.PROTECT, verbose_name='Marca del Producto')
    MotoId = models.ForeignKey(Moto, on_delete=models.PROTECT, verbose_name='Moto del Producto')
    ColorProductoId = models.ForeignKey(ColorProducto, on_delete=models.PROTECT, null = True, blank = True)
    TamañoProductoId = models.ForeignKey(TamañoProducto, on_delete=models.PROTECT, null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Detalle de los productos'

    def __str__(self):
        return f"{self.ProductoId.Nombre} - {self.MarcaId.Nombre} - {self.MotoId.Modelo}"
    