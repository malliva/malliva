# This will manage all Malliva mongodb database connections

# from django.conf import settings

from mongoengine import (
    connect,
    context_managers,
    disconnect,
    disconnect_all,
)

from config.config_loader import settings


class connect_to_database:
    def __init__(self, database, alias):
        self.alias = alias
        self.database = database
        self.port = "27017"
        self.host = settings.PLATFORM_DB_HOST
        self.username = settings.DB_USERNAME
        self.password = settings.DB_PASSWORD

    def initiate_db_connection(self):
        connect(
            alias=self.alias,
            db=self.database,
            host=self.host,
            username=self.username,
            password=self.password,
        )

    def switch_database(new_database):
        context_managers.switch_db()

    def switch_collection(new_collection):
        context_managers.switch_collection(collection)

    def end_db_connection():
        disconnect(
            alias=self.alias,
            db=self.database,
            host=self.host,
            username=self.username,
            password=self.password,
        )
