# Projeto Django MVC com Mongo

git commit -m "Primeiro commit: estrutura inicial do projeto Flask"
git branch -M main

# Histórico de passos e comandos de setup

iniciei e ativei venv
pip install django==3.1.12 sqlparse==0.2.4
pip install djongo, django-environ
sudo django-admin startproject config .
python manage.py migrate
python manage.py runserver

### Comando Especial

Para resetar containers Docker:

```bash
docker stop $(docker ps -aq) &&
docker rm $(docker ps -aq) &&
docker-compose down -v &&
docker volume prune -f
```
