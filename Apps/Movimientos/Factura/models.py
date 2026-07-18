from django.db import models
from Apps.Catalogos.CondicionPago.models import CondicionPago
from Apps.Catalogos.Cliente.models import Cliente
from Apps.Movimientos.LoteProducto.models import LoteProducto
from Apps.Catalogos.EstadoCuenta.models import EstadoCuenta

class Factura(models.Model):
    Fecha = models.DateField(auto_now_add=True, verbose_name='Fecha de la Factura')
    NumFactura = models.IntegerField(verbose_name='Número de Factura')
    Total = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Total de la Factura')
    CondicionPagoId = models.ForeignKey(CondicionPago, on_delete=models.PROTECT)
    ClienteId = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Facturas'
    
    def __str__(self):  
        return f"Factura {self.NumFactura} - {self.ClienteId.Nombre} - {self.ClienteId.Apellido}"
    
class DetalleFactura(models.Model):
    Cantidad = models.IntegerField(verbose_name='Cantidad del Producto')
    PrecioUnitario = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Precio Unitario del Producto')
    Subtotal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Subtotal del Producto')
    FacturaId = models.ForeignKey(Factura, on_delete=models.PROTECT)
    LoteProductoId = models.ForeignKey(LoteProducto, on_delete=models.PROTECT)
    estado = models.BooleanField(default= True)

    class Meta:
        verbose_name_plural = 'Detalles de la Factura'

    def __str__(self):
        return f"Detalle de la Factura {self.LoteProductoId.DetalleCompraId.DetalleProductoId.ProductoId.Nombre} - {self.LoteProductoId.DetalleCompraId.DetalleProductoId.MotoId.Modelo} -  {self.LoteProductoId.DetalleCompraId.DetalleProductoId.MarcaId.Nombre} - {self.PrecioUnitario}"
    
class FacturaCredito(models.Model):
    FechaInicio = models.DateField(auto_now_add=True, verbose_name='Fecha de Inicio de la Factura')
    FechaVencimiento = models.DateField(verbose_name='Fecha de Vencimiento de la Factura')
    MontoTotal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Monto Total de la Factura')
    SaldoPendiente = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Monto Pendiente de la Factura')
    FacturaId = models.ForeignKey(Factura, on_delete=models.PROTECT)
    EstadoCuentaId = models.ForeignKey(EstadoCuenta, on_delete=models.PROTECT)
    estado = models.BooleanField(default= True)

    class Meta:
        verbose_name_plural = 'Facturas de credito'

    def __str__(self):
        return f"Factura Crédito {self.FacturaId.NumFactura} - {self.FechaVencimiento}"