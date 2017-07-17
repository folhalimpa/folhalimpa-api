from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from .models import Servidor, UnidadeGestoraMunicipio
from . import serializers


class PagamentoViewSet(viewsets.ViewSet):
    serializer_class = serializers.PagamentoSerializer

    def list(self, request):
        pagamentos = []
        serializer = serializers.PagamentoSerializer(
            instance=pagamentos, many=True)
        return Response(serializer.data)


class ServidorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Servidor.objects.all()
    serializer_class = serializers.ServidorSerializer

    def retrieve(self, request, pk=None):
        queryset = Servidor.objects.all()
        servidor = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ServidorSerializer(servidor)

        return Response(serializer.data)


class UnidadeGestoraMunicipioViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UnidadeGestoraMunicipio.objects.all()
    serializer_class = serializers.UnidadeGestoraMunicipioSerializer

    def retrieve(self, request, pk=None):
        queryset = UnidadeGestoraMunicipio.objects.all()
        unidade = get_object_or_404(queryset, pk=pk)
        serializer = serializers.UnidadeGestoraMunicipioSerializer(unidade)
        
        return Response(serializer.data)
