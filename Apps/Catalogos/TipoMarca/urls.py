from django.urls import path
from .views import TipoMarcaApiView, TipoMarcaApiViewDetail

urlpatterns = [
        path("", TipoMarcaApiView.as_view(), name='Para Listar o crear un Tipo de marca'),
        path("<int:pk>", TipoMarcaApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un Tipo de marca')
]