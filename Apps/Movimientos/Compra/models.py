from django.db import models
from Apps.Catalogos.Proveedor.models import Proveedor
from Apps.Catalogos.CondicionPago.models import CondicionPago
from Apps.Movimientos.Producto.models import DetalleProducto

class Compra(models.Model):
    FechaCompra = models.DateField(verbose_name='Fecha de Compra')
    NumCompra = models.CharField(max_length=20, verbose_name='Número de Compra')
    Total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total de la Compra')
    ProveedorId = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    CondicionPagoId = models.ForeignKey(CondicionPago, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Compras'

    def __str__(self):
        return f"Compra {self.NumCompra} - {self.ProveedorId.Nombre}"
    
class DetalleCompra(models.Model):
    Cantidad = models.IntegerField(verbose_name='Cantidad del Producto')
    PrecioUnitario = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Precio Unitario del Producto')
    Subtotal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Subtotal del Producto')
    CompraId = models.ForeignKey(Compra, on_delete=models.PROTECT)
    DetalleProductoId = models.ForeignKey(DetalleProducto, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Detalles de la Compra'

    def __str__(self):
        return f"Detalle de la Compra {self.DetalleProductoId.ProductoId.Nombre} - {self.DetalleProductoId.MotoId.Modelo} - {self.DetalleProductoId.MarcaId.Nombre} - {self.PrecioUnitario}"
    
class CompraCredito(models.Model):
    Monto = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Monto del Crédito')
    SaldoPendiente = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Saldo Pendiente del Crédito')
    FechaInicio = models.DateField(auto_now_add=True, verbose_name='Fecha de Inicio del Crédito')
    FechaVencimiento = models.DateField(verbose_name='Fecha de Vencimiento del Crédito')
    CompraId = models.ForeignKey(Compra, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Compras de credito'

    def __str__(self):
        return f"Crédito de la Compra {self.CompraId.NumCompra} - {self.FechaVencimiento}"