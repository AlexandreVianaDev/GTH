# GTH

## Rodar a aplicação

    Clone este repositório
    No docker-compose.yml altere o POSTGRES_USER e o DATABASE_URL de Alexandre para o usuário do seu computador
    Pode ser necessário dar permissão para o arquivo entrypoint.sh rodar as migrations e levantar: `chmod +x bff/entrypoint.sh`
    Abra o terminal na raiz do projeto clonado e execute o comando: `docker-compose up --build`
    API vai estar em `http://127.0.0.1:8000/api/`
    Frontend na url: `http://localhost:3000/`
