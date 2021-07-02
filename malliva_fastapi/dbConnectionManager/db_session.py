from .tenant_connections import connect_to_database
from config.config_loader import settings

# create mongo connection instance

platform_db_connection_instance = connect_to_database(settings.PLATFORM_DEFAULT_ALIAS)

accounts_db_connection_instance = connect_to_database(settings.ACCOUNT_DEFAULT_ALIAS)
