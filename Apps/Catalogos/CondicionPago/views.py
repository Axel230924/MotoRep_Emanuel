from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import CondicionPago
from .serializers import CondicionPagoSerializers

from drf_yasg.utils import swagger_auto_schema

class CondicionPagoApiView(APIView):
    
    @swagger_auto_schema (responses={200: CondicionPagoSerializers(many = True)})
    def get(self, request):     

        condicionPago = CondicionPago.objects.filter (estado = True)
        serializers = CondicionPagoSerializers(condicionPago, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=CondicionPagoSerializers, responses={201: CondicionPagoSerializers()})
    def post(self, request):

        serializer = CondicionPagoSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class CondicionPagoApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (CondicionPago, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: CondicionPagoSerializers()})
    def get(self, request, pk):

        condicionPago = self.get_object (pk)
        serializer = CondicionPagoSerializers(condicionPago)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: CondicionPagoSerializers()})
    def patch (self, request, pk):

        condicionPago = self.get_object (pk)
        serializer = CondicionPagoSerializers(condicionPago, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Condicion de pago eliminado correctamente'})
    def delete(self, request, pk):
        
        condicionPago = self.get_object(pk)
        condicionPago.estado = False
        condicionPago.save()
        return Response(status=status.HTTP_204_NO_CONTENT)