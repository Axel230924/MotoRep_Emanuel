from django.urls import path
from .views import ProveedorApiView, ProveedorApiViewDetail

urlpatterns = [
        path("", ProveedorApiView.as_view(), name='Para Listar o crear un Proveedor'),
        path("<int:pk>", ProveedorApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un Proveedor')
]