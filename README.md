# malliva
Power your marketplace platform

Run 
export DJANGO_SETTINGS_MODULE='malliva.environments.development_settings'

or 

$env:DJANGO_SETTINGS_MODULE='malliva.environments.development_settings'


docker-compose up -d

# when you want to rebuild image otherwise just run the above
docker-compose up -d --build

python .\manage.py makemigrations
python manage.py migrate

python .\manage.py loaddata categories.json

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