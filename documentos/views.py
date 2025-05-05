from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoDeDocumento
from .serializers import TipoDeDocumentoSerializer

class TipoDeDocumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoDeDocumento.objects.all()
    serializer_class = TipoDeDocumentoSerializer
