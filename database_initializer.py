# This will ensure that all existing marketplace schema are always up to date

# from django.db import router

# https://www.fullstackpython.com/django-db-router-examples.html
# using = router.db_for_write(opts.model)

# https://docs.djangoproject.com/en/3.2/topics/db/multi-db/#topics-db-multi-db-hints

import os
from mongoengine import connect

from config.config_loader import settings

if __name__ == "__main__":
    print("Migrations now running")

    # manage makemigrations
    # connect("malliva21_db")
    # print("connected")

    os.system("mongoengine_migrate --log-level=debug -u mongodb://mallivay21:P123Malliva@malliva33y21_db:27017/malliva21_db makemigrations -m models.mallivaUsers")

    os.system(
        "mongoengine_migrate --log-level=debug -u mongodb://mallivay21:P123Malliva@malliva33y21_db:27017/malliva21_db migrate")

    # print("default initial data loaded")
