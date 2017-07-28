from django.db import models


class Pagamento(object):
    def __init__(self, **kwargs):
        for campo in ('cd_UGestora', 'de_ugestora', 'de_cargo', 'de_tipocargo', 'cd_CPF', 'dt_MesAnoReferencia',
                      'no_Servidor', 'vl_vantagens', 'de_UOrcamentaria'):
            setattr(self, campo, kwargs.get(campo, None))


class Servidor(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(unique=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'servidores_municipios'

    def __str__(self):
        return self.nome


class UnidadeGestoraMunicipio(models.Model):
    codigo = models.CharField(unique=True, max_length=15)
    nome = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'unidades_gestoras_municipios'

    def __str__(self):
        return self.nome


class VinculoMunicipio(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vinculos_municipios'

class CargoMunicipio(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cargos_municipios'


class FolhaMunicipio(models.Model):
    id_servidor = models.IntegerField()
    id_cargo = models.IntegerField()
    id_vinculo = models.IntegerField()
    id_unidade_gestora = models.IntegerField()
    id_unidade_orcamentaria = models.IntegerField()
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'folhas_municipios'
