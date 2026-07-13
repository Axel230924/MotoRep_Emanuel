from django.urls import path
from .views import CajaApiView
from .views import CajaApiViewDetail

app_name = 'Caja'

urlpatterns = [
    path("", CajaApiView.as_view(), name='Para Listar o crear una caja'),
    path("<int:pk>/", CajaApiViewDetail.as_view(), name='Para obtener, actualizar o eliminar una caja'),
]