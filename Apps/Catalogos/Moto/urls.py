from django.urls import path
from .views import MotoApiView, MotoApiViewDetail

urlpatterns = [
        path("", MotoApiView.as_view(), name='Para Listar o crear una Moto'),
        path("<int:pk>", MotoApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar una Moto')
]