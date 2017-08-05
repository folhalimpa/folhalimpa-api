# HackFest 2017

O Folha Limpa é um navegador dos dados de folhas de pagamento da Paraíba.

Possibilitamos a visualização dos maiores pagamentos efetuados nas unidades
gestoras dos municípios da Paraíba e a análise de possíveis casos de acúmulo de
cargos.

## Design

O Folha Limpa traz um design limpo e com interações simples para que o cidadão
consiga navegar facilmente pelos dados disponíveis.

A página inicial do Folha Limpa apresenta imagens de pontos turísticos da
Paraíba para trazer maior empatia da sociedade paraibana com o sistema.

Através de gráficos e tabelas interativas, o projeto permite que as pessoas
analisem problemas complexos de forma simplificada.

Além disso, o website possui design responsivo, podendo ser utilizado em
diferentes dispositivos com tamanhos distintos de tela.

## Sustentabilidade

A implantação e atualização do website e da API são automatizadas podendo ser
feitas em segundos.  Um conjunto de tecnologias permite isto: Docker, Git,
Django, Angular, Nginx, etc.

A API utiliza o servidor de cache Redis para tornar as respostas mais rápidas e
para evitar processamento desnecessário no servidor.

Todo o projeto é executado em dois servidores. Um servidor é utilizado para o
banco de dados de grafo e o outro para o resto da aplicação. O custo total de
manutenção da infraestrutura do Folha Limpa é de US$ 30,00 / mês.  O website é
monitorado para saber se ele está no ar
([stats.uptimerobot.com/Eqg93folR](https://stats.uptimerobot.com/Eqg93folR)).
Quando algum problema de disponibilidade acontece, a equipe é notificada.

Dois bancos de dados são utilizados, o Neo4J e o MySQL. Ambos precisam ser
carregados para a aplicação funcionar.  O repositório da aplicação traz scripts
que usam os dados obtidos no site do TCE para carregar os bancos de dados.

É possível utilizar o projeto para outros estados, basta que os dados sejam
carregados no banco de dados no formato esperado.

## Inovação e Criatividade

O Folha Limpa permite que o cidadão navegue de forma simples e visual pelos
pagamentos realizados pelos órgãos públicos ou recebidos por servidores.

Outra funcionalidade importante é a análise de acúmulo de cargos através de um
banco de dados de grafo. Esta análise cruza dados de pagamentos dos órgãos
municipais e estaduais. A solução implementada permite que futuramente que
pagamentos de outras fontes sejam incorporados a análise com pequeno custo de
mudança.

Todas as análises podem ser exportadas para arquivos .csv, que podem ser
abertos e manipulados em planilhas eletrônicas como o Excel.

## Potencial de Impacto

Cerca de 50% dos gastos dos órgãos públicos é com folhas de pagamento. Qualquer
economia obtida com os abusos evitados pode ter impacto direto na qualidade dos
serviços públicos fornecidos.

Por exemplo, um servidor que acumule cargos não estará realizando suas funções
de forma adequada nos órgãos, fazendo com que a qualidade dos serviços
prestados para população diminua. Isto é percebido em hospitais, escolas, entre
outros. 
