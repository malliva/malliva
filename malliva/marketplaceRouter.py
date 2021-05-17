from django.conf import settings
from django.urls import resolve, Resolver404
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site

from malliva import urls
from marketplaceRouter.models import MarketplaceRouter

# def get_current_site():
#     SITE_ID = getattr(settings, "SITE_ID", 1)
#     site_name = Site.objects.get(id=SITE_ID)
#     return site_name


def get_current_db():
    print("hello world")


class CustomDatabaseRouter(object):

    get_current_db()

    print(get_current_site)

    def db_for_read(self, model, **hints):
        # print(MarketplaceRouter.objects.filter())
        # site_name = get_current_site()
        # if site_name in ["site1"]:
        #     return "db1"
        # if site_name in ["site2"]:
        #     return "db2"
        return "default"

    def db_for_write(self, model, **hints):
        site_name = get_current_site()
        if site_name in ["site1"]:
            return "db1"
        if site_name in ["site2"]:
            return "db2"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {"primary", "replica1", "replica2"}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
