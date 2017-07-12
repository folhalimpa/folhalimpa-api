import pandas as pd

pagamentos = pd.read_csv('dados/TCE-PB-SAGRES-Folha_Pessoal_Esfera_Municipal.txt', encoding='utf-8', sep='|')

prefeituras = pagamentos[pagamentos.de_ugestora.str.contains('Prefeitura Municipal de ')]

u_prefeituras = prefeituras['de_ugestora'].unique()
cidades = [prefeitura.replace('Prefeitura Municipal de ','') for prefeitura in u_prefeituras]
cidades.sort()

len(cidades)


# Atenção! ter cuidado com os matches de:
# - "Belém" e "Belém do Brejo do Cruz"
# - "Belém do Brejo do Cruz" e "Brejo do Cruz"
# - "Cuité" e "Cuité de Mamanguape"
# - 'Riachão','Riachão do Bacamarte' e 'Riachão do Poço'
# - 'São Domingos' e 'São Domingos do Cariri'

# Identificador de tretas
for primeira_cidade in cidades:
    for segunda_cidade in cidades:
        if segunda_cidade.find(primeira_cidade) != -1 and primeira_cidade != segunda_cidade:
            print('treta: {}/{}'.format(primeira_cidade, segunda_cidade))


def _filtro_por_cidade(pagamentos, cidade):
    return pagamentos['de_ugestora'].str.contains(cidade) & ~(_filtro_por_similares(pagamentos, cidade))

def _filtro_por_similares(pagamentos, cidade):
    filtro = None
    similares = _similares(cidade)
    if len(similares) == 0:
        filtro = pd.Series([False] * len(pagamentos))
    else:
        filtro =  _filtro_por_cidade(pagamentos, similares[0])
        for similar in similares[1:]:
            filtro = filtro | _filtro_por_cidade(pagamentos, similar)

    return filtro

def _similares(cidade):
    similares = []
    for outra_cidade in cidades:
        if outra_cidade.find(cidade) != -1 and cidade != outra_cidade:
            similares.append(outra_cidade)
    return similares


# TODO
def _salva_csv(cidade):
    pass




