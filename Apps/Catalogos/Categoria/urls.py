from django.urls import path
from .views import CategoriaApiView, CategoriaApiViewDetail

app_name = 'Categoria'

urlpatterns = [
        path("", CategoriaApiView.as_view(), name='Para Listar o crear una categoria'),
        path("<int:pk>", CategoriaApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar una categporia')
]