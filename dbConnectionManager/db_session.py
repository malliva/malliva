from .tenant_connections import connect_to_database
from config.config_loader import settings
from fastapi import HTTPException, status

# create mongo connection instance

platform_db_connection_instance = connect_to_database(
    settings.PLATFORM_DEFAULT_ALIAS)

accounts_db_connection_instance = connect_to_database(
    settings.ACCOUNT_DEFAULT_ALIAS)

# resolve domain from db


async def register_connection(current_db):
    """ 
    This method will create connection for the current request
    """
    try:
        await accounts_db_connection_instance.register_new_db_connection(current_db=current_db)
    except:
        raise HTTPException(detail="Could not connect to database",
                            status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
