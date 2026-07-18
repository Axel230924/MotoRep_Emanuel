from django.urls import path
from .views import MarcaApiView, MarcaApiViewDetail

urlpatterns = [
        path("", MarcaApiView.as_view(), name='Para Listar o crear una Marca'),
        path("<int:pk>", MarcaApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar una Marca')
]