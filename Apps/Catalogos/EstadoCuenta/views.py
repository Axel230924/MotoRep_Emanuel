from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import EstadoCuenta
from .serializers import EstadoCuentaSerializers

from drf_yasg.utils import swagger_auto_schema

class EstadoCuentaApiView(APIView):
    
    @swagger_auto_schema (responses={200: EstadoCuentaSerializers(many = True)})
    def get(self, request):     

        estadoCuenta = EstadoCuenta.objects.filter (estado = True)
        serializers = EstadoCuentaSerializers(estadoCuenta, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=EstadoCuentaSerializers, responses={201: EstadoCuentaSerializers()})
    def post(self, request):

        serializer = EstadoCuentaSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class EstadoCuentaApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (EstadoCuenta, pk=pk, estado= True)   
    
    @swagger_auto_schema (responses={200: EstadoCuentaSerializers()})
    def get(self, request, pk):

        estadoCuenta = self.get_object (pk)
        serializer = EstadoCuentaSerializers(estadoCuenta)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: EstadoCuentaSerializers()})
    def patch (self, request, pk):

        estadoCuenta = self.get_object (pk)
        serializer = EstadoCuentaSerializers(estadoCuenta, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Estado de cuenta eliminado correctamente'})
    def delete(self, request, pk):
        
        estadoCuenta = self.get_object(pk)
        estadoCuenta.estado = False
        estadoCuenta.save()
        return Response(status=status.HTTP_204_NO_CONTENT)