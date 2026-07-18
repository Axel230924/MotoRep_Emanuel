from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import TamañoProducto
from .serializers import TamañoProductoSerializers

from drf_yasg.utils import swagger_auto_schema

class TamañoProductoApiView(APIView):
    
    @swagger_auto_schema (responses={200: TamañoProductoSerializers(many = True)})
    def get(self, request):     

        tamañoProducto = TamañoProducto.objects.filter (estado = True)
        serializers = TamañoProductoSerializers(tamañoProducto, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=TamañoProductoSerializers, responses={201: TamañoProductoSerializers()})
    def post(self, request):

        serializer = TamañoProductoSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class TamañoProductoApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (TamañoProducto, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: TamañoProductoSerializers()})
    def get(self, request, pk):

        tamañoProducto = self.get_object (pk)
        serializer = TamañoProductoSerializers(tamañoProducto)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: TamañoProductoSerializers()})
    def patch (self, request, pk):

        tamañoProducto = self.get_object (pk)
        serializer = TamañoProductoSerializers(tamañoProducto, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Tamaño de producto eliminado correctamente'})
    def delete(self, request, pk):
        
        tamañoProducto = self.get_object(pk)
        tamañoProducto.estado = False
        tamañoProducto.save()
        return Response(status=status.HTTP_204_NO_CONTENT)