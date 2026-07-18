from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Proveedor
from .serializers import ProveedorSerializers

from drf_yasg.utils import swagger_auto_schema

class ProveedorApiView(APIView):
    
    @swagger_auto_schema (responses={200: ProveedorSerializers(many = True)})
    def get(self, request):     

        proveedor = Proveedor.objects.filter (estado = True)
        serializers = ProveedorSerializers(proveedor, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=ProveedorSerializers, responses={201: ProveedorSerializers()})
    def post(self, request):

        serializer = ProveedorSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class ProveedorApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (Proveedor, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: ProveedorSerializers()})
    def get(self, request, pk):

        proveedor = self.get_object (pk)
        serializer = ProveedorSerializers(proveedor)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: ProveedorSerializers()})
    def patch (self, request, pk):

        proveedor = self.get_object (pk)
        serializer = ProveedorSerializers(proveedor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Proveedor eliminado correctamente'})
    def delete(self, request, pk):
        
        proveedor = self.get_object(pk)
        proveedor.estado = False
        proveedor.save()
        return Response(status=status.HTTP_204_NO_CONTENT)