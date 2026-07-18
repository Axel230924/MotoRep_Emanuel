from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ColorProductoSerializers
from .models import ColorProducto
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class ColorProductoApiView (APIView):

    @swagger_auto_schema (responses= {200: ColorProductoSerializers(many=True)})
    def get (self, request):
        colorProduto = ColorProducto.objects.filters (estado=True)
        serializers = ColorProductoSerializers (colorProduto, many=True)
        return Response (serializers.data)
    
    @swagger_auto_schema (request_body= ColorProductoSerializers, responses= {201: ColorProductoSerializers()})
    def post (self, request):
        serializers = ColorProductoSerializers (data = request.data)
        serializers.is_valid(raise_exception= True)
        serializers.save()
        return Response (data= serializers.data, status= status.HTTP_201_CREATED)
    
class ColorProductoApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404(ColorProducto, pk=pk, estado= True)
    
    @swagger_auto_schema (responses= {200: ColorProductoSerializers()})
    def get (self, request, pk):
        colorProducto = self.get_object(pk)
        serializers = ColorProductoSerializers(colorProducto)
        return Response (serializers.data)
    
    @swagger_auto_schema (responses= {200: ColorProductoSerializers()})
    def path (self, request, pk):
        colorProducto = self.get_object (pk)
        serializers = ColorProductoSerializers(colorProducto, data= request.data, partial = True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response (serializers.data)
    
    swagger_auto_schema (responses= {204: "Color de producto eliminado correctamente"})
    def delete (self, request, pk):
        cliente = self.get_object(pk)
        cliente.estado = False
        cliente.save()
        return Response (status = status.HTTP_204_NO_CONTENT)