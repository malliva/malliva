# This will manage all Malliva mongodb database connections

# from django.conf import settings

import re
from mongoengine import (
    connect,
    context_managers,
    disconnect,
    disconnect_all,
)
from pymongo import database

from config.config_loader import settings


class connect_to_database():
    def __init__(self, alias):
        self.alias = alias
        self.database = settings.PLATFORM_DEFAULT_DB
        self.port = settings.PLATFORM_DB_PORT
        self.host = settings.PLATFORM_DB_HOST
        self.username = settings.DB_USERNAME
        self.password = settings.DB_PASSWORD
        print("database connection instance created successfully")

    async def initiate_db_connection(self):
        connect(
            alias=self.alias,
            db=self.database,
            host=self.host,
            username=self.username,
            password=self.password,
        )
        print("database connection started successfully")

    async def switch_database(self, model_class, new_database):
        context_managers.switch_db(model_class, new_database)
        return model_class

    async def switch_collection(self, model_class, new_collection):
        context_managers.switch_collection(model_class, new_collection)
        return model_class

    async def end_db_connection(self):
        disconnect(
            alias=self.alias
        )
        print("database connection ended successfully")
