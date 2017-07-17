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
