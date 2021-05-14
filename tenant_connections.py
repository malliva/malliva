# This will manage all Malliva mongodb database connections

class connect_to_database:
    def __init__(self, alias, database, username, password, host):
        self.alias = alias
        self.database = database
        self.username = username
        self.password = password
        self.host = host
        #self.port = port
        
    def initiate_db_connection():
        mongoengine.connect(alias=self.alias, db=self.database, host=self.host, username=self.username, password=self.password)

    def switch_database(new_database):
        #mongoengine.context_managers.switch_db()

    def end_db_connection():
        mongoengine.disconnect(alias=self.alias, db=self.database, host=self.host, username=self.username, password=self.password)
