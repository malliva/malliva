# malliva
Power your marketplace platform

Run 
export DJANGO_SETTINGS_MODULE='malliva.environments.development_settings'

or 

$env:DJANGO_SETTINGS_MODULE='malliva.environments.development_settings'

Python 3.8 required 
Django 3.2

docker-compose up -d

# when you want to rebuild image otherwise just run the above
docker-compose up -d --build

python manage.py createsuperuser

python .\manage.py runserver

API end points

http://localhost:8000/api/v1/user/register POST

http://localhost:8000/api/v1/marketplace/create/ POST

npm install -g nx

npm install

sudo apt install gettext

nx serve market-app
nx serve marketing-app or 

npm run nx -- serve marketing-app

Change secret key for production

mongoengine_migrate --log-level=debug -u mongodb://localhost/malliva21_db makemigrations -m mallivaUsers.models

mongoengine_migrate --log-level=debug -u mongodb://localhost/malliva21_db migrate

mongoengine_migrate --log-level=debug -u mongodb://localhost/malliva21_db downgrade 0000_auto_20210626_1748

mongo $MONGO_INITDB_DATABASE -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD