from threadlocals.threadlocals import get_request_variable
from django.conf import settings


class MallivaDatabaseRouter:
    def db_for_read(self, model, **hints):

        # change the database name for this request
        database_name = get_request_variable("database_name")

        try:
            settings.DATABASES["default"]["NAME"] = database_name
        except:
            return "default"

        return "default"

    def db_for_write(self, model, **hints):
        # site_name = get_current_site(request)

        # change the database name for this request
        database_name = get_request_variable("database_name")

        settings.DATABASES["default"]["NAME"] = database_name

        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        # return True
        # don't allow relation
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        # return db == 'default'
        return True
