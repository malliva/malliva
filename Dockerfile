FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /app
ENV DJANGO_SETTINGS_MODULE='malliva.environments.development_settings'
COPY . /app
RUN pip install -r requirements.txt