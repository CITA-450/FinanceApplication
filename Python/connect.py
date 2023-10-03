import pymysql

class MySQLConnector:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Connected to the MySQL database.")
        except pymysql.Error as e:
            print(f"Error connecting to the database: {e}")

    def execute_query(self, query):
        if self.connection:
            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()
                return result
            except pymysql.Error as e:
                print(f"Error executing query: {e}")
        else:
            print("Not connected to the database.")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection to the MySQL database closed.")

# Example usage:
#if __name__ == "__main__":
#    host = "your_remote_host"  # Replace with your MySQL server's hostname or IP address
#    port = 3306  # Replace with the MySQL port (default is 3306)
#    user = "your_username"
#    password = "your_password"
#    database = "your_database_name"

#   connector = MySQLConnector(host, port, user, password, database)
#    connector.connect()

    # Example query
#    query = "SELECT * FROM your_table"
#    result = connector.execute_query(query)
#    print(result)

#    connector.close()
