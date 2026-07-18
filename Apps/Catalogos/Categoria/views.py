from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import CategoriaSerializers
from .models import Categoria

from drf_yasg.utils import swagger_auto_schema

class CategoriaApiView(APIView):

    @swagger_auto_schema (responses= {200: CategoriaSerializers (many = True)})
    def get (self, request):
        categoria = Categoria.objects.filter (estado = True)
        serializers = CategoriaSerializers(categoria, many= True)
        return Response (serializers.data)
    
    @swagger_auto_schema (request_body=CategoriaSerializers, responses={201: CategoriaSerializers()})
    def post(self, request):

        serializer = CategoriaSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
    
class CategoriaApiViewDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404 (Categoria, pk=pk, estado = True)
    
    @swagger_auto_schema (responses= {200: CategoriaSerializers})
    def get (self, request, pk):

        categoria = self.get_object (pk)
        serializers = CategoriaSerializers (categoria)
        return Response (serializers.data)
            
    @swagger_auto_schema (responses={200: CategoriaSerializers})
    def patch (self, request, pk):

        categoria = self.get_object (pk)
        serializer = CategoriaSerializers(categoria, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    @swagger_auto_schema (responses={204: 'Categoria eliminado correctamente'})
    def delete(self, request, pk):
            
        categoria = self.get_object(pk)
        categoria.estado = False
        categoria.save()
        return Response(status=status.HTTP_204_NO_CONTENT)