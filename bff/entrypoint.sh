#!/bin/bash

# Aguarda o banco de dados estar pronto
./wait-for-it.sh db:5432 --timeout=30 --strict -- echo "Banco de dados está pronto!"

# Executa as migrações
echo "Executando as migrações..."
python manage.py migrate

# Inicia o servidor
echo "Iniciando o servidor..."
exec python manage.py runserver 0.0.0.0:8000