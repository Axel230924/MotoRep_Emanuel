from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import TipoMarca
from .serializers import TipoMarcaSerializers

from drf_yasg.utils import swagger_auto_schema

class TipoMarcaApiView(APIView):
    
    @swagger_auto_schema (responses={200: TipoMarcaSerializers(many = True)})
    def get(self, request):     

        tipoMarca = TipoMarca.objects.filter (estado = True)
        serializers = TipoMarcaSerializers(tipoMarca, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=TipoMarcaSerializers, responses={201: TipoMarcaSerializers()})
    def post(self, request):

        serializer = TipoMarcaSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class TipoMarcaApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (TipoMarca, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: TipoMarcaSerializers()})
    def get(self, request, pk):

        tipoMarca = self.get_object (pk)
        serializer = TipoMarcaSerializers(tipoMarca)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: TipoMarcaSerializers()})
    def patch (self, request, pk):

        tipoMarca = self.get_object (pk)
        serializer = TipoMarcaSerializers(tipoMarca, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Tipo de marca eliminado correctamente'})
    def delete(self, request, pk):
        
        tipoMarca = self.get_object(pk)
        tipoMarca.estado = False
        tipoMarca.save()
        return Response(status=status.HTTP_204_NO_CONTENT)