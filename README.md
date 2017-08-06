# Folha Limpa API

Folha Limpa é um projeto do Hackfest 2017 que tem como objetivo exibir visualizações de anomalias nas folhas de pagamento do estado e dos municípios da Paraíba.

O Folha Limpa pode ser acessado no endereço: [folhalimpa.org](http://folhalimpa.org/).

## Como executar localmente

O Folha Limpa utiliza o [Docker](https://www.docker.com) para sua execução.

Antes de executar a API é necessário ter construído a imagem do banco de dados. Veja [aqui](https://github.com/folhalimpa/folhalimpa-db) como criar a imagem do banco de dados.

Pra construir a imagem do docker, de dentro da raiz do projeto execute:

`docker-compose build api redis`

O docker construirá uma imagem a partir do `Dockerfile` e depois que o processo terminar você verá uma imagem chamada `fl-api` quando executar o comando `docker images`. Para criar um container a partir da imagem criada no passo anterior, execute `docker-compose up api redis`. Quando o processo terminar, você deverá ter uma API rodando na porta 8000. Para verificar, execute `curl 127.0.0.1:8000`.
