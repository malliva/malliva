# malliva
Power your marketplace platform

Run 
export DJANGO_SETTINGS_MODULE='malliva.environments.development_settings'

or 

$env:DJANGO_SETTINGS_MODULE='malliva.environments.development_settings'

python manage.py migrate

python manage.py createsuperuser

python .\manage.py runserver

API end points

http://localhost:8000/api/v1/user/register POST

http://localhost:8000/api/v1/marketplace/create/ POST

npm install -g nx
npm install
nx serve marketing-app or 
npm run nx -- serve marketing-app