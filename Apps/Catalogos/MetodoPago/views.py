from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import MetodoPago
from .serializers import MetodooPagoSerializers

from drf_yasg.utils import swagger_auto_schema

class MetodoPagoApiView(APIView):
    
    @swagger_auto_schema (responses={200: MetodooPagoSerializers(many = True)})
    def get(self, request):     

        metodoPago = MetodoPago.objects.filter (estado = True)
        serializers = MetodooPagoSerializers(metodoPago, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=MetodooPagoSerializers, responses={201: MetodooPagoSerializers()})
    def post(self, request):

        serializer = MetodooPagoSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class MetodoPagoApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (MetodoPago, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: MetodooPagoSerializers()})
    def get(self, request, pk):

        metodoPago = self.get_object (pk)
        serializer = MetodooPagoSerializers(metodoPago)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: MetodooPagoSerializers()})
    def patch (self, request, pk):

        metodoPago = self.get_object (pk)
        serializer = MetodooPagoSerializers(metodoPago, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Metodo de pago eliminado correctamente'})
    def delete(self, request, pk):
        
        metodoPago = self.get_object(pk)
        metodoPago.estado = False
        metodoPago.save()
        return Response(status=status.HTTP_204_NO_CONTENT)