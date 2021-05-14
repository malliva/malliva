FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ENV DJANGO_SETTINGS_MODULE='malliva.environments.development_settings'

COPY . /app

CMD python manage.py runserver 0.0.0.0:8000