# This will ensure that all existing marketplace schema are always up to date

from django.db import router

# https://www.fullstackpython.com/django-db-router-examples.html
# using = router.db_for_write(opts.model)

# https://docs.djangoproject.com/en/3.2/topics/db/multi-db/#topics-db-multi-db-hints
