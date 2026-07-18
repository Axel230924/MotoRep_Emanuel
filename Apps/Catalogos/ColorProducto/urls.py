from django.urls import path
from .views import ColorProductoApiView, ColorProductoApiViewDetail

urlpatterns = [
        path("", ColorProductoApiView.as_view(), name='Para Listar o crear un Color de producto'),
        path("<int:pk>", ColorProductoApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un Color de producto')
]