from rest_framework import serializers
from pagamentos.models import Servidor, UnidadeGestoraMunicipio, FolhaMunicipio, CargoMunicipio


class PagamentoSerializer(serializers.Serializer):
    cd_UGestora = serializers.CharField(max_length=256)
    de_ugestora = serializers.CharField(max_length=256)
    de_cargo = serializers.CharField(max_length=256)
    de_tipocargo = serializers.CharField(max_length=256)
    cd_CPF = serializers.CharField(max_length=256)
    dt_MesAnoReferencia = serializers.CharField(max_length=256)
    no_Servidor = serializers.CharField(max_length=256)
    vl_vantagens = serializers.CharField(max_length=256)
    de_UOrcamentaria = serializers.CharField(max_length=256)


class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = ('id', 'nome')


class UnidadeGestoraMunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeGestoraMunicipio
        fields = ('id', 'nome', 'codigo')


class FolhaMunicipioSerializer(serializers.ModelSerializer):
    nome_servidor = serializers.SerializerMethodField()
    nome_unidade = serializers.SerializerMethodField()
    cargo = serializers.SerializerMethodField()

    def get_nome_servidor(self, obj):
        return Servidor.objects.get(pk=obj.id_servidor).nome

    def get_nome_unidade(self, obj):
        return UnidadeGestoraMunicipio.objects.get(pk=obj.id_unidade_gestora).nome

    def get_cargo(self, obj):
        return CargoMunicipio.objects.get(pk=obj.id_cargo).nome

    class Meta:
        model = FolhaMunicipio
        fields = ('id_servidor', 'id_unidade_gestora', 'valor', 'nome_servidor', 'nome_unidade', 'cargo', 'data_pagamento')
