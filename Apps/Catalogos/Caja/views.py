from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Caja
from .serializers import CajaSerializer

from drf_yasg.utils import swagger_auto_schema

class CajaApiView(APIView):
    
    #Obtenemos todas las cajas activas
    @swagger_auto_schema (responses={200: CajaSerializer(many = True)})
    def get(self, request):     

        caja = Caja.objects.filter (estado = True)
        serializers = CajaSerializer(caja, many=True)
        return Response(serializers.data)

    #Creamos una nueva caja
    @swagger_auto_schema (request_body=CajaSerializer, responses={201: CajaSerializer()})
    def post(self, request):

        serializer = CajaSerializer(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class CajaApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (Caja, pk=pk, estado= True)    
    
    #Obtenemos una caja por su id
    @swagger_auto_schema (responses={200: CajaSerializer()})
    def get(self, request, pk):

        caja = self.get_object (pk)
        serializer = CajaSerializer(caja)
        return Response(serializer.data)

    #Actualizamos una caja por su id
    @swagger_auto_schema (responses={200: CajaSerializer()})
    def patch (self, request, pk):

        caja = self.get_object (pk)
        serializer = CajaSerializer(caja, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    #Eliminamos una caja por su id (eliminado logico)
    @swagger_auto_schema (responses={204: 'Caja eliminado correctamente'})
    def delete(self, request, pk):
        
        caja = self.get_object(pk)
        caja.estado = False
        caja.save()
        return Response(status=status.HTTP_204_NO_CONTENT)