# This will ensure that all existing marketplace schema are always up to date

# from django.db import router

# https://www.fullstackpython.com/django-db-router-examples.html
# using = router.db_for_write(opts.model)

# https://docs.djangoproject.com/en/3.2/topics/db/multi-db/#topics-db-multi-db-hints

import os

if __name__ == "__main__":
    print("Migrations now running")

    # manage makemigrations
    os.system("python manage.py makemigrations")

    os.system("python manage.py migrate")

    os.system("python manage.py loaddata users.json")
    print("default super user data loaded")

    os.system("python manage.py loaddata categories.json")
    print("default category data loaded")
