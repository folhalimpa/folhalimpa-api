# folhalimpa-api

Para que os passos descritos aqui funcionem, é preciso ter construído a imagem do banco de dados anteriormente. Veja [aqui](https://github.com/folhalimpa/folhalimpa-db) como criar a imagem do banco de dados.

Pra construir a imagem do docker, de dentro da raiz do projeto execute:

`docker-compose build`

O docker vai construir uma imagem a partir do `Dockerfile` e depois que o processo terminar você vai ver uma imagem chamada `fl-api` quando executar o comando `docker images`. Para criar um container a partir da imagem criada no passo anterior, execute `docker-compose run api`. Quando o processo terminar, você deverá ter uma API rodando na porta 8000. Para verificar, execute `curl localhost:8000`.
