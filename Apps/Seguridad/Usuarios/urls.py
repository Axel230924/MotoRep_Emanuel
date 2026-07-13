from django.urls import path, include
from .views import userCreateView

app_name = 'Usuarios'
urlpatterns = [
      path('api/v1/register/', userCreateView.as_view(), name='Registrar un usuario'),
]