from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import ClienteSerializers
from .models import Cliente

from drf_yasg.utils import swagger_auto_schema 

class ClienteApiView (APIView):
    
    @swagger_auto_schema (responses= {200: ClienteSerializers (many = True)})
    def get (self, request):
        cliente = Cliente.objects.filters (estado = True)
        serializers = ClienteSerializers (cliente, many =True)
        return Response (serializers.data)
    
    @swagger_auto_schema (request_body= ClienteSerializers, response= {201: ClienteSerializers()})
    def post (self, request):
        serializers = ClienteSerializers (data = request.data)
        serializers.is_valid (raise_exception= True)
        serializers.save()
        return Response (data = serializers.data, status = status.HTTP_201_CREATED)
    
class ClienteApiViewDetail (APIView):

    def get_object (self, pk):
        return get_object_or_404 (Cliente, pk=pk, estado= True)

    @swagger_auto_schema (response = {200: ClienteSerializers})
    def get (self, request, pk):
        cliente = self.get_object(pk)
        serializers = ClienteSerializers(cliente)
        return Response (serializers.data)
    
    @swagger_auto_schema (responses= {200: ClienteSerializers()})
    def path (self, request, pk):
        cliente = self.get_object (pk)
        serializers = ClienteSerializers (cliente, data= request.data, partial= True)
        serializers.is_valid (raise_exception= True)
        serializers.save()
        return Response (serializers.data)
    
    swagger_auto_schema (responses={204: "Cliente eliminado correctamente"})
    def delete (self, request, pk):
        cliente = self.get_object (pk)
        cliente.estado = False
        cliente.save()
        return Response (status= status.HTTP_204_NO_CONTENT)