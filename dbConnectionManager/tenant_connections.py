# This will manage all Malliva mongodb database connections

# from django.conf import settings

import re
import logging
from mongoengine import (
    connect,
    register_connection,
    context_managers,
    disconnect,
    disconnect_all,
)

from config.config_loader import settings

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)


class connect_to_database():
    def __init__(self, alias):
        self.alias = alias
        self.database = settings.PLATFORM_DEFAULT_DB
        self.port = settings.PLATFORM_DB_PORT
        self.host = settings.PLATFORM_DB_HOST
        self.username = settings.DB_USERNAME
        self.password = settings.DB_PASSWORD
        logger.info("database connection instance created successfully")

    async def initiate_db_connection(self):
        connect(
            alias=self.alias,
            db=self.database,
            host=self.host,
            username=self.username,
            password=self.password,
        )
        logger.info("database connection started successfully")

    async def register_new_db_connection(self, current_db):
        await self.reset_class_variables(current_db)
        register_connection(
            alias=self.alias,
            db=self.database,
            host=self.host,
            username=self.username,
            password=self.password
        )
        logger.info("new database connection started successfully")

    async def switch_database(self, model_class, new_database):
        await self.reset_class_variables(new_database)
        return context_managers.switch_db(model_class, new_database)

    async def switch_collection(self, model_class, new_collection):
        return context_managers.switch_collection(model_class, new_collection)

    async def end_db_connection(self):
        disconnect(
            alias=self.alias
        )
        logger.info("database connection ended successfully")

    async def reset_class_variables(self, current_db):
        self.database = current_db
