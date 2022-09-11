import mysql.connector

class Connection:
    '''
    Connection

    MySQL connection class.
    '''
    def __init__(self, host, port, user, password, database):
        '''
        __init__

        Gets the database information.
        '''
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        '''
        connect

        Connects to the database, retrieving a cursor to execute any query.
        '''
        return mysql.connector.connect(
            user=self.user, 
            password=self.password,
            host=self.host,
            database=self.database
        )
    
    def query_data(self, query, params):
        '''
        query_data

        Queries data from the database.
        '''
        results = []

        conn = self.connect()
        cursor = conn.cursor(buffered=True, dictionary=True)
        cursor.execute(query, params)

        for result in cursor:
            results.append(result)
        
        cursor.close()
        conn.close()

        return results
