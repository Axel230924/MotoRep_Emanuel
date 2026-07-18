from django.urls import path
from .views import EstadoCuentaApiView, EstadoCuentaApiViewDetail

urlpatterns = [
        path("", EstadoCuentaApiView.as_view(), name='Para Listar o crear un Estado de cuenta'),
        path("<int:pk>", EstadoCuentaApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un Estado de cuenta')
]