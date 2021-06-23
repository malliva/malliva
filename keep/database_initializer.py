# This will ensure that all existing marketplace schema are always up to date

# from django.db import router

# https://www.fullstackpython.com/django-db-router-examples.html
# using = router.db_for_write(opts.model)

# https://docs.djangoproject.com/en/3.2/topics/db/multi-db/#topics-db-multi-db-hints

import os
from mongoengine import connect

if __name__ == "__main__":
    print("Migrations now running")

    # manage makemigrations
    # os.system("python manage.py makemigrations")
    connect("malliva21_db")
    print("connected")

    os.system("python manage.py migrate --database=malliva_maindb")

    os.system(
        "python manage.py loaddata users permissions roles categories plans subscriptions configurations template_stylings social_media_pages marketplace_accounts listings custom_fields --database=malliva_maindb"
    )
    print("default initial data loaded")
