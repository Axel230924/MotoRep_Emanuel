from django.db import models
from Apps.Catalogos.Empleado.models import Empleado
from Apps.Catalogos.Caja.models import Caja
from Apps.Catalogos.TipoMovCaja.models import TipoMovCaja
from Apps.Catalogos.MetodoPago.models import MetodoPago
from Apps.Movimientos.Compra.models import Compra, CompraCredito
from Apps.Movimientos.Factura.models import Factura, FacturaCredito

class TurnoCaja(models.Model):
    FechaApertura = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Apertura de la caja')
    FechaCierre = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Cierre de la caja')
    MontoInicial = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Monto Inicial de la caja')
    MontoFinal = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Monto Final de la caja')
    Egresos = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Egresos de la caja')
    DinDigital = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Dinero Digital de la caja')
    DinEfectivo = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Dinero en Efectivo de la caja')
    EmpleadoId = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    CajaId = models.ForeignKey(Caja, on_delete=models.PROTECT)
    estado = models.BooleanField(default= True)

    class Meta:
        verbose_name_plural = 'Turnos de la Caja'

    def __str__(self):
        return f"{self.CajaId.NumCaja} - {self.EmpleadoId.Nombre} - {self.EmpleadoId.Apellido} - {self.FechaApertura}"
    
class MovimientoCaja(models.Model):
    FechaMovimiento = models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Movimiento de la caja')
    MontoTotal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Monto del Movimiento de la caja')
    Descripcion = models.TextField(verbose_name='Descripción del Movimiento de la caja', null= True, blank= True)
    TipoMovCajaId = models.ForeignKey(TipoMovCaja, on_delete=models.PROTECT)
    TurnoCajaId = models.ForeignKey(TurnoCaja, on_delete=models.PROTECT)
    CompraId = models.ForeignKey(Compra, on_delete=models.PROTECT, null=True, blank=True)
    CompraCreditoId = models.ForeignKey(CompraCredito, on_delete=models.PROTECT, null=True, blank=True)
    FacturaId = models.ForeignKey(Factura, on_delete=models.PROTECT, null=True, blank=True)
    FacturaCreditoId = models.ForeignKey(FacturaCredito, on_delete=models.PROTECT, null=True, blank=True)
    estado = models.BooleanField(default= True)

    class Meta:
        verbose_name_plural = 'Movimientos de la caja'

    def __str__(self):
        return f"{self.TipoMovCajaId.Nombre} - {self.FechaMovimiento}"
    
class DetallePagoMov(models.Model):
    Monto = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Monto del Pago del Movimiento de la caja')
    MetodoPagoId = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    MovimientoCajaId = models.ForeignKey(MovimientoCaja, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Detalles de pago'

    def __str__(self):
        return f"{self.MetodoPagoId.Nombre}"