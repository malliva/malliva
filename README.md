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

http://localhost:8000/api/v1/accounts/register POST