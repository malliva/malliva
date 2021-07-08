# This class receives the request, resolve the domain name associated with the request,
# determines the database and return the database name

from config.config_loader import settings
from dbConnectionManager.db_session import register_connection

db_name = None


async def get_db_name(request):
    """ 
    This method will get db name and setup connection for it
    """

    global db_name

    current_marketplace = request.base_url.hostname.split(":")[0]
    current_marketplace = request.base_url.hostname.split(".")[0]

    for domain in settings.MALLIVA_DOMAIN:
        if current_marketplace == domain:
            db_name = settings.PLATFORM_DEFAULT_DB

    # if domain name is not a malliva marketplace domain, resolve marketplace db
    if db_name is None:
        db_name = current_marketplace + "53Q4"

    # Make the database to default here if you wish to use it no longer
    await register_connection(db_name)


# async def get_db(db_name: str = Depends(get_db_name)):
    # configure database here
    # pass
