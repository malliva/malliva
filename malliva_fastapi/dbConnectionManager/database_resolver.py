# This class receives the request, resolve the domain name associated with the request,
# determines the database and return the database name

from config.config_loader import settings
from fastapi import Depends, Request


async def get_db_name(request):

    # current_marketplace = request.base_url.hostname.split(":")[0]
    current_marketplace = request
    print(current_marketplace)

    for domain in settings.MALLIVA_DOMAIN:
        if current_marketplace == domain:
            db_name = current_marketplace + "53Q4"
            print(db_name)

    if db_name is None:
        db_name = settings.PLATFORM_DEFAULT_DB

    # Make the database to default here if you wish to use it no longer
    return db_name
