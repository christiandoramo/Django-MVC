# Teste de projeto Django MVC com Mongo

# RF01 - Criar usuário a partir de endpoint usando email, name (opcional), password (criptografada), registra o usuario com id uuid automatico e deve retornar message e status na resposta. (tornar email único)

## Histórico de passos e comandos de setup

- iniciei e ativei venv
- pip install django==3.1.12 sqlparse==0.2.4
- pip install djongo, django-environ
- sudo django-admin startproject config .
- python manage.py migrate
- python manage.py runserver

## Comando para resetar containers docker:

```bash
docker stop $(docker ps -aq) &&
docker rm $(docker ps -aq) &&
docker-compose down -v &&
docker volume prune -f
```
