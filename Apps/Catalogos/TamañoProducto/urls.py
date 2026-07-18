from django.urls import path
from .views import TamañoProductoApiView, TamañoProductoApiViewDetail

urlpatterns = [
        path("", TamañoProductoApiView.as_view(), name='Para Listar o crear un Tamaño de producto'),
        path("<int:pk>", TamañoProductoApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un Tamaño de producto')
]