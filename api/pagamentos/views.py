import datetime
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse

from django.db.models import Sum

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework_csv.renderers import CSVRenderer

from .models import Servidor, UnidadeGestoraMunicipio, FolhaMunicipio
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
    queryset = UnidadeGestoraMunicipio.objects.all().order_by("nome")
    serializer_class = serializers.UnidadeGestoraMunicipioSerializer

    def retrieve(self, request, pk=None):
        queryset = UnidadeGestoraMunicipio.objects.all()
        unidade = get_object_or_404(queryset, pk=pk)
        serializer = serializers.UnidadeGestoraMunicipioSerializer(unidade)
        
        return Response(serializer.data)


class FolhaMunicipioViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FolhaMunicipio.objects.all()
    serializer_class = serializers.FolhaMunicipioSerializer

    def retrieve(self, request, pk=None):
        queryset = FolhaMunicipio.objects.all()
        unidade = get_object_or_404(queryset, pk=pk)
        serializer = serializers.FolhaMunicipioSerializer(unidade)
        
        return Response(serializer.data)


class PagamentoPorServidor(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.FolhaMunicipioSerializer
    lookup_url_kwarg = "servidor_id"

    def get_queryset(self):
        month_begin = self.request.query_params.get('mes_inicio', None)
        month_end = self.request.query_params.get('mes_fim', None)
        year_begin = self.request.query_params.get('ano_inicio', None)
        year_end = self.request.query_params.get('ano_fim', None)
        servidor_id = self.kwargs.get(self.lookup_url_kwarg)

        if all(v is not None for v in [month_begin, month_end, year_begin, year_end]):
            date_begin = datetime.date(int(year_begin), int(month_begin), 1)
            date_end = datetime.date(int(year_end), int(month_end), 1)

            return FolhaMunicipio.objects.filter(id_servidor=servidor_id).filter(data_pagamento__gte=date_begin).filter(data_pagamento__lte=date_end).order_by("-valor")

        return FolhaMunicipio.objects.filter(id_servidor=servidor_id).order_by("-valor")


class PagamentoPorUnidadeGestora(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.FolhaMunicipioSerializer
    lookup_url_kwarg = "unidade_id"

    def get_queryset(self):
        month_begin = self.request.query_params.get('mes_inicio', None)
        month_end = self.request.query_params.get('mes_fim', None)
        year_begin = self.request.query_params.get('ano_inicio', None)
        year_end = self.request.query_params.get('ano_fim', None)
        unidade_id = self.kwargs.get(self.lookup_url_kwarg)

        if all(v is not None for v in [month_begin, month_end, year_begin, year_end]):
            date_begin = datetime.date(int(year_begin), int(month_begin), 1)
            date_end = datetime.date(int(year_end), int(month_end), 1)

            return FolhaMunicipio.objects.filter(id_unidade_gestora=unidade_id).filter(data_pagamento__gte=date_begin).filter(data_pagamento__lte=date_end).order_by("-valor")

        return FolhaMunicipio.objects.filter(id_unidade_gestora=unidade_id).order_by("-valor")


class PagamentoServidorInfo(View):
    
    def get(self, request, servidor_id):
        month_begin = request.GET.get('mes_inicio', None)
        month_end = request.GET.get('mes_fim', None)
        year_begin = request.GET.get('ano_inicio', None)
        year_end = request.GET.get('ano_fim', None)

        if all(v is not None for v in [month_begin, month_end, year_begin, year_end]):
            date_begin = datetime.date(int(year_begin), int(month_begin), 1)
            date_end = datetime.date(int(year_end), int(month_end), 1)

            queryset = FolhaMunicipio.objects.filter(id_servidor=servidor_id).filter(data_pagamento__gte=date_begin).filter(data_pagamento__lte=date_end)
        else:
            queryset = FolhaMunicipio.objects.filter(id_servidor=servidor_id)

        number_of_payments = queryset.count()

        if number_of_payments == 0:
            total_payments = 0
            average_payments = 0
        else:
            total_payments = queryset.aggregate(Sum("valor"))["valor__sum"]
            average_payments = total_payments/number_of_payments

        return JsonResponse({"quantity": number_of_payments, "total": total_payments, "average": average_payments})


class PagamentoUnidadeGestoraInfo(View):
    
    def get(self, request, unidade_id):
        month_begin = request.GET.get('mes_inicio', None)
        month_end = request.GET.get('mes_fim', None)
        year_begin = request.GET.get('ano_inicio', None)
        year_end = request.GET.get('ano_fim', None)

        if all(v is not None for v in [month_begin, month_end, year_begin, year_end]):
            date_begin = datetime.date(int(year_begin), int(month_begin), 1)
            date_end = datetime.date(int(year_end), int(month_end), 1)

            queryset = FolhaMunicipio.objects.filter(id_unidade_gestora=unidade_id).filter(data_pagamento__gte=date_begin).filter(data_pagamento__lte=date_end)
        else:
            queryset = FolhaMunicipio.objects.filter(id_unidade_gestora=unidade_id)

        number_of_payments = queryset.count()
        
        if number_of_payments == 0:
            total_payments = 0
            average_payments = 0
        else:
            total_payments = queryset.aggregate(Sum("valor"))["valor__sum"]
            average_payments = total_payments/number_of_payments

        return JsonResponse({"quantity": number_of_payments, "total": total_payments, "average": average_payments})


class PaginatedCSVRenderer (CSVRenderer):
    results_field = 'results'

    def render(self, data, *args, **kwargs):
        if not isinstance(data, list):
            data = data.get(self.results_field, [])
        return super(PaginatedCSVRenderer, self).render(data, *args, **kwargs)


class PagamentoPorServidorCSV(viewsets.ModelViewSet):
    renderer_classes = (PaginatedCSVRenderer,)
    serializer_class = serializers.FolhaMunicipioSerializerCSV
    lookup_url_kwarg = "servidor_id"

    def get_queryset(self):
        month_begin = self.request.query_params.get('mes_inicio', None)
        month_end = self.request.query_params.get('mes_fim', None)
        year_begin = self.request.query_params.get('ano_inicio', None)
        year_end = self.request.query_params.get('ano_fim', None)
        servidor_id = self.kwargs.get(self.lookup_url_kwarg)

        if all(v is not None for v in [month_begin, month_end, year_begin, year_end]):
            date_begin = datetime.date(int(year_begin), int(month_begin), 1)
            date_end = datetime.date(int(year_end), int(month_end), 1)

            return FolhaMunicipio.objects.filter(id_servidor=servidor_id).filter(data_pagamento__gte=date_begin).filter(data_pagamento__lte=date_end).order_by("-valor")

        return FolhaMunicipio.objects.filter(id_servidor=servidor_id).order_by("-valor")


class PagamentoPorUnidadeGestoraCSV(viewsets.ModelViewSet):
    renderer_classes = (PaginatedCSVRenderer,)    
    serializer_class = serializers.FolhaMunicipioSerializerCSV
    lookup_url_kwarg = "unidade_id"

    def get_queryset(self):
        month_begin = self.request.query_params.get('mes_inicio', None)
        month_end = self.request.query_params.get('mes_fim', None)
        year_begin = self.request.query_params.get('ano_inicio', None)
        year_end = self.request.query_params.get('ano_fim', None)
        unidade_id = self.kwargs.get(self.lookup_url_kwarg)

        if all(v is not None for v in [month_begin, month_end, year_begin, year_end]):
            date_begin = datetime.date(int(year_begin), int(month_begin), 1)
            date_end = datetime.date(int(year_end), int(month_end), 1)

            return FolhaMunicipio.objects.filter(id_unidade_gestora=unidade_id).filter(data_pagamento__gte=date_begin).filter(data_pagamento__lte=date_end).order_by("-valor")

        return FolhaMunicipio.objects.filter(id_unidade_gestora=unidade_id).order_by("-valor")
