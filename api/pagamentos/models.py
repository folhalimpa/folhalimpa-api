class Pagamento(object):
    def __init__(self, **kwargs):
        for campo in ('cd_UGestora', 'de_ugestora', 'de_cargo', 'de_tipocargo', 'cd_CPF', 'dt_MesAnoReferencia',
                      'no_Servidor', 'vl_vantagens', 'de_UOrcamentaria'):
            setattr(self, campo, kwargs.get(campo, None))
