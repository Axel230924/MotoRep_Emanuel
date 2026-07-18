from django.urls import path
from .views import MetodoPagoApiView, MetodoPagoApiViewDetail

urlpatterns = [
        path("", MetodoPagoApiView.as_view(), name='Para Listar o crear un Metodo de pago'),
        path("<int:pk>", MetodoPagoApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un Metodo de pago')
]