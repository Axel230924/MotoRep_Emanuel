from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Moto
from .serializers import MotoSerializers

from drf_yasg.utils import swagger_auto_schema

class MotoApiView(APIView):
    
    @swagger_auto_schema (responses={200: MotoSerializers(many = True)})
    def get(self, request):     

        moto = Moto.objects.filter (estado = True)
        serializers = MotoSerializers(moto, many=True)
        return Response(serializers.data)

    @swagger_auto_schema (request_body=MotoSerializers, responses={201: MotoSerializers()})
    def post(self, request):

        serializer = MotoSerializers(data=request.data)       
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        
class MotoApiViewDetail(APIView):

    def get_object (self, pk):
        return get_object_or_404 (Moto, pk=pk, estado= True)    
    
    @swagger_auto_schema (responses={200: MotoSerializers()})
    def get(self, request, pk):

        moto = self.get_object (pk)
        serializer = MotoSerializers(moto)
        return Response(serializer.data)

    @swagger_auto_schema (responses={200: MotoSerializers()})
    def patch (self, request, pk):

        moto = self.get_object (pk)
        serializer = MotoSerializers(moto, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    @swagger_auto_schema (responses={204: 'Moto eliminado correctamente'})
    def delete(self, request, pk):
        
        moto = self.get_object(pk)
        moto.estado = False
        moto.save()
        return Response(status=status.HTTP_204_NO_CONTENT)