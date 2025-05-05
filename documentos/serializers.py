from rest_framework import serializers
from .models import TipoDeDocumento

class TipoDeDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeDocumento
        fields = ['id', 'nombre', 'descripcion']