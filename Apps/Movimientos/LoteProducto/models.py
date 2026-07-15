from django.db import models
from Apps.Movimientos.Compra.models import DetalleCompra

class LoteProducto(models.Model):
    Cantidad = models.IntegerField (verbose_name='Cantidad del Lote')
    PrecioUnitario = models.DecimalField (max_digits=7, decimal_places=2, verbose_name='Precio Unitario del producto')
    PrecioVenta = models.DecimalField (max_digits=7, decimal_places=2, verbose_name='Precio de Venta del producto')
    FechaRegistro = models.DateField (auto_now_add=True, verbose_name='Fecha de Registro del Lote')
    DetalleCompraId = models.ForeignKey (DetalleCompra, on_delete=models.PROTECT)
    estado = models.BooleanField (default= True)

    class Meta:
        verbose_name_plural = 'Lotes de productos'
    
    def __str__(self):
        return f"{self.DetalleCompraId.DetalleProductoId.ProductoId.Nombre} - {self.DetalleCompraId.DetalleProductoId.MotoId.Modelo} - {self.DetalleCompraId.DetalleProductoId.MarcaId.Nombre}"