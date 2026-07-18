from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Marca
from .serializers import MarcaSerializers

from drf_yasg.utils import swagger_auto_schema

class MarcaApiView(APIView):
    
    @swagger_auto_schema (responses={200: MarcaSerializers(many = True)})
    def get(self, request):     

        marca = Marca.objects.filter (estado = True)
        serializers = MarcaSerializers(marca, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=MarcaSerializers, responses={201: MarcaSerializers()})
    def post(self, request):

        serializer = MarcaSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class MarcaApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (Marca, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: MarcaSerializers()})
    def get(self, request, pk):

        marca = self.get_object (pk)
        serializer = MarcaSerializers(marca)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: MarcaSerializers()})
    def patch (self, request, pk):

        marca = self.get_object (pk)
        serializer = MarcaSerializers(marca, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Marca eliminado correctamente'})
    def delete(self, request, pk):
        
        marca = self.get_object(pk)
        marca.estado = False
        marca.save()
        return Response(status=status.HTTP_204_NO_CONTENT)