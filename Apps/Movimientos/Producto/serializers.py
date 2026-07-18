from rest_framework.serializers import ModelSerializer, CharField
from .models import Producto, DetalleProducto
from Apps.Catalogos.Moto.serializers import MotoSerializers

class ProductoSerializer(ModelSerializer):

    Categoria_nombre = CharField(source='CategoriaId.Nombre', read_only=True)

    class Meta:
        
        model = Producto
        fields = [
                    'Nombre', 
                    'Codigo', 
                    'CategoriaId',
                    'Categoria_nombre'
                  ]

class DetalleProductoSerializer(ModelSerializer):

    Moto_nombre = MotoSerializers(read_only=True)

    Producto_nombre = CharField(source='ProductoId.Nombre', read_only=True)
    Marca_nombre = CharField(source='MarcaId.Nombre', read_only=True)
    ColorProducto_nombre = CharField(source='ColorProductoId.Color', read_only=True)
    TamañoProducto_nombre = CharField(source='TamañoProductoId.Tamaño', read_only=True)

    class Meta:
        
        model = DetalleProducto
        fields = [
                    'ProductoId',
                    'MarcaId', 
                    'MotoId', 
                    'ColorProductoId', 
                    'TamañoProductoId',
                    'Producto_nombre',
                    'Marca_nombre',
                    'Moto_nombre',
                    'ColorProducto_nombre',
                    'TamañoProducto_nombre'
                   ]