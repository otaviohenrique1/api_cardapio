# api_cardapio

## Links

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

## Comandos

### Criar venv

- python -m virtualenv .venv

### Ativar venv

- venv\scripts\activate
- venv/scripts/activate
- source venv\scripts\activate
- source venv/scripts/activate

### Desativar venv

- deactivate

### Pacotes

- pip install django
- pip install python-dotenv
- pip install virtualenv
- pip install djangorestframework
- pip install markdown
- pip install django-filter
- pip install validate-docbr
- pip install Faker
- pip install django-cors-headers
- pip install pillow

## Exibir pacotes instalados

- pip freeze
- pip freeze > requirements.txt

## Instalar pacotes

- pip install -r requirements.txt

### Comandos do Django

- django-admin help => ajuda
- django-admin startproject setup . => cria o projeto
- python manage.py runserver => roda o server
- python manage.py help => ajuda
- python manage.py startapp galeria => cria um app
- python manage.py collectstatic => cria arquivos estaticos
- python manage.py makemigrations => cria a migration
- python manage.py migrate => roda a migration
- python manage.py shell => abre o shell do Django
- python manage.py createsuperuser => cria o super usuario
- python manage.py makemessages -l pt_BR => cria arquivo de mensagens
- python manage.py compilemessages -l pt_BR => compila arquivo de mensagens
- python manage.py test => rodar os testes

### Comando para criar secret key para o django

- python scripts/secret_key_generator.py

### Comandos para inicializar o projeto (da primeira vez)

1. python -m virtualenv .venv
2. source .venv/scripts/activate
3. pip install -r requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver
