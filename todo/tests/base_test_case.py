import sqlite3
from unittest2 import TestCase
from tabulate import tabulate


class SqliteDatabase(object):

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        return sqlite3.connect(self.path)

    def __exit__(self, excClass, exc, traceback):
        pass


class BaseTestCase(TestCase):

    def tabulate(self, data):
        print('\n' + tabulate(data, headers = 'keys'))

    def create_inmemory_connection(self):
        with SqliteDatabase(':memory:') as connection:
            return connection

    def execute_query(self, connection, sql_path):
        sql = open(sql_path).read()
        cursor = connection.cursor()
        cursor.execute(sql)

    def create_database(self, sql_path):
        connection = self.create_inmemory_connection()
        self.execute_query(connection, sql_path)

        return connection
