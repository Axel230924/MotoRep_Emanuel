from django.urls import path
from .views import TipoMovCajaApiView, TipoMovCajaApiViewDetail

urlpatterns = [
        path("", TipoMovCajaApiView.as_view(), name='Para Listar o crear un Tipo de movimiento de caja'),
        path("<int:pk>", TipoMovCajaApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un Tipo de movimiento de caja')
]