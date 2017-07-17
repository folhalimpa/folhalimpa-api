from rest_framework import serializers
from pagamentos.models import Servidor, UnidadeGestoraMunicipio


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
        fields = ('id', 'nome', 'cpf')


class UnidadeGestoraMunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeGestoraMunicipio
        fields = ('id', 'nome', 'codigo')
