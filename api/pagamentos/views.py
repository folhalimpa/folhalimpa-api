from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers


class PagamentoViewSet(viewsets.ViewSet):
    serializer_class = serializers.PagamentoSerializer

    def list(self, request):
        pagamentos = []
        serializer = serializers.PagamentoSerializer(
            instance=pagamentos, many=True)
        return Response(serializer.data)
