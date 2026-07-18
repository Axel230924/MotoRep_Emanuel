from django.urls import path
from .views import CondicionPagoApiView, CondicionPagoApiViewDetail
urlpatterns = [
           path("", CondicionPagoApiView.as_view(), name='Para Listar o crear una Condicion de pago'),
        path("<int:pk>", CondicionPagoApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar una Condicion de pago') 
]