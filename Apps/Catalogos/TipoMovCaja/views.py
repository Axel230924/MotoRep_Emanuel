from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import TipoMovCaja
from .serializers import TipoMovCajaSerializers

from drf_yasg.utils import swagger_auto_schema

class TipoMovCajaApiView(APIView):
    
    @swagger_auto_schema (responses={200: TipoMovCajaSerializers(many = True)})
    def get(self, request):     

        tipoMovCaja = TipoMovCaja.objects.filter (estado = True)
        serializers = TipoMovCajaSerializers(tipoMovCaja, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=TipoMovCajaSerializers, responses={201: TipoMovCajaSerializers()})
    def post(self, request):

        serializer = TipoMovCajaSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class TipoMovCajaApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (TipoMovCaja, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: TipoMovCajaSerializers()})
    def get(self, request, pk):

        tipoMovCaja = self.get_object (pk)
        serializer = TipoMovCajaSerializers(tipoMovCaja)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: TipoMovCajaSerializers()})
    def patch (self, request, pk):

        tipoMovCaja = self.get_object (pk)
        serializer = TipoMovCajaSerializers(tipoMovCaja, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Tipo de movimiento de caja eliminado correctamente'})
    def delete(self, request, pk):
        
        tipoMovCaja = self.get_object(pk)
        tipoMovCaja.estado = False
        tipoMovCaja.save()
        return Response(status=status.HTTP_204_NO_CONTENT)