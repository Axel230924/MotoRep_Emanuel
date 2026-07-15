from django.urls import path, include

urlpatterns = [
    path('Caja/', include ('Apps.Catalogos.Caja.urls')),
    path('Categoria/', include ('Apps.Catalogos.Categoria.urls')),
    path('Cliente/', include ('Apps.Catalogos.Cliente.urls')),
    path('ColorProducto/', include ('Apps.Catalogos.ColorProducto.urls')),
    path('CondicionPago/', include ('Apps.Catalogos.CondicionPago.urls')),
    path('Empleado/', include ('Apps.Catalogos.Empleado.urls')),
    path('EstadoCuenta/', include ('Apps.Catalogos.EstadoCuenta.urls')),
    path('MetodoPago/', include ('Apps.Catalogos.MetodoPago.urls')),
    path('Proveedor/', include ('Apps.Catalogos.Proveedor.urls')),
    path('TamañoProducto/', include ('Apps.Catalogos.TamañoProducto.urls')),
    path('TipoMarca/', include ('Apps.Catalogos.TipoMarca.urls')),
    path('TipoMovCaja/', include ('Apps.Catalogos.TipoMovCaja.urls')),
    path('Moto/', include ('Apps.Catalogos.Moto.urls')),
    path('Marca/', include ('Apps.Catalogos.Marca.urls'))   
]