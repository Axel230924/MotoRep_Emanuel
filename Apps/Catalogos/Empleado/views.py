from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Empleado
from .serializers import EmpleadoSerializers

from drf_yasg.utils import swagger_auto_schema

class EmpleadoApiView(APIView):
    
    @swagger_auto_schema (responses={200: EmpleadoSerializers(many = True)})
    def get(self, request):     

        empleado = Empleado.objects.filter (estado = True)
        serializers = EmpleadoSerializers(empleado, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=EmpleadoSerializers, responses={201: EmpleadoSerializers()})
    def post(self, request):

        serializer = EmpleadoSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class EmpleadoApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (Empleado, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: EmpleadoSerializers()})
    def get(self, request, pk):

        empleado = self.get_object (pk)
        serializer = EmpleadoSerializers(empleado)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: EmpleadoSerializers()})
    def patch (self, request, pk):

        empleado = self.get_object (pk)
        serializer = EmpleadoSerializers(empleado, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Empleado eliminado correctamente'})
    def delete(self, request, pk):
        
        empleado = self.get_object(pk)
        empleado.estado = False
        empleado.save()
        return Response(status=status.HTTP_204_NO_CONTENT)