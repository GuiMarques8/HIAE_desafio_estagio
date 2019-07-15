# API Phenotypes

Desafio realizado por Guilherme Marques


# Configurações iniciais
Versões utilizadas: 
Python: 3.7.1
PostgreSQL: 10.9
Django: 2.2.3

Necessário ter o Python instalado e o PostgreSQL. Links:
https://www.python.org/downloads/
https://www.postgresql.org/download/

Para testar a API recomenda-se o uso do Postman:

https://www.getpostman.com/downloads/

Executar os comandos

> pip install django

> pip install django-postgres-copy

> pip install psycopg2

## Executando o projeto
Abrir o projeto em um interpretador de Python e no arquivo 'settings.py' alterar os seguintes campos:

'NAME': 'postgres',  
'USER': 'postgres',  
'PASSWORD': 'admin',  
'HOST': '127.0.0.1',  
'PORT': '5432',

Esses campos devem ser preenchidos com as informações do banco de dados utilizado, e podem ser extraídos ao se rodar o pgAdmin 4, proveniente da instalação do Postgres.

Entrar na pasta do projeto pelo cmd utilizando o comando 'cd' e executar os seguintes passos:

> python manage.py makemigrations MyApp

> python manage.py migrate

> python manage.py importcsv

> python manage.py runserver

Abir o Postman e inserir o link http gerado pelo comando runserver com a rota 'findphenotypes/'
Por exemplo:

http://localhost:8000/findphenotypes/

- Setar como comando 'GET' 
- Na guia 'Body' selecionar 'raw' como input e informar o tipo de texto como 'application/json'
- Escrever o nome do gene correspondente entre aspas duplas. 
Exemplo: "ATR"

