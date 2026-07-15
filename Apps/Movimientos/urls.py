from django.urls import path, include

urlpatterns = [
    path('CajaMov/', include ('Apps.Movimientos.CajaMov.urls')),
    path('Compra/', include ('Apps.Movimientos.Compra.urls')),
    path('Factura/', include ('Apps.Movimientos.Factura.urls')),
    path('Producto/', include ('Apps.Movimientos.Producto.urls')),
    path('LoteProducto/', include ('Apps.Movimientos.LoteProducto.urls')),
]