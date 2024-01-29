import psycopg2

class DataBase:
    def __init__(self, host, user, password, database):
        try:
            self.connection= psycopg2.connect(host=host, user=user, password=password, database=database)
            self.connection.autocommit=True,
            self.cursor= self.connection.cursor()
            print('all good')
        except psycopg2.Error as e:
            print('bad news', {e})

    def execute(self, query):
        try:
            self.cursor.execute(query)
        except psycopg2.Error as e:
            print(e)

    def featch(self, query):
        try:
            self.cursor.execute(query)
            result= self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(e)
            return []


    def __del__(self):
        try:
            self.cursor.close()
            self.connection.close()
            print('end connect')
        except psycopg2.Error as e:
            print(f'error close{e}')
