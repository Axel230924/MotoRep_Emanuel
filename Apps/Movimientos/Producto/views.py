from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductoSerializer, DetalleProductoSerializer
from .models import Producto, DetalleProducto
from drf_yasg.utils import swagger_auto_schema

