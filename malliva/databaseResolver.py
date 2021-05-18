# This class receives the request, resolve the domain name associated with the request,
# determines the database and return the database name

from threadlocals.threadlocals import set_request_variable
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

# from django.contrib.sites.models import Site


class getSubdomainMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        self.current_marketplace = get_current_site(request).domain.split(".")[0]
        # print("subdomain middleware starts here")
        # print(self.current_marketplace)
        if self.current_marketplace == settings.MALLIVA_DOMAIN:
            # request.META["database_name"] = "default"
            set_request_variable("database_name", settings.MALLIVA_DEFAULT_DB)
        else:
            set_request_variable("database_name", self.current_marketplace)
        # Make the database to default here if you wish to use it no longer

        return self.get_response(request)
