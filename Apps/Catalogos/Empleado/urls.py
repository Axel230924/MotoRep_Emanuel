from django.urls import path
from .views import EmpleadoApiView, EmpleadoApiViewDetail

urlpatterns = [
        path("", EmpleadoApiView.as_view(), name='Para Listar o crear un Empleado'),
        path("<int:pk>", EmpleadoApiViewDetail.as_view(), name = 'Obtener, actualizar o eliminar un Empleado')    
]