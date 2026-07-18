from django.urls import path
from .views import ClienteApiView, ClienteApiViewDetail

urlpatterns = [
        path("", ClienteApiView.as_view(), name='Para Listar o crear un cliente'),
        path("<int:pk>", ClienteApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un cliente')
]    
