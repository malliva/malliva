# This will manage all Malliva mongodb database connections

from mongoengine import (
    connect,
    context_managers,
    register_connection,
    disconnect,
    disconnect_all,
)


class connect_to_database:
    def __init__(self, alias, database, username, password, host):
        self.alias = alias
        self.database = database
        self.username = username
        self.password = password
        self.host = host
        # self.port = port

    def initiate_db_connection():
        register_connection(
            alias=self.alias,
            db=self.database,
            host=self.host,
            username=self.username,
            password=self.password,
        )

    def switch_database(new_database):
        context_managers.switch_db()

    def switch_collection(collection):
        context_managers.switch_collection(collection)

    def end_db_connection():
        disconnect(
            alias=self.alias,
            db=self.database,
            host=self.host,
            username=self.username,
            password=self.password,
        )
