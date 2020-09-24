import sqlite3
from unittest2 import TestCase
from tabulate import tabulate
import pymysql
import pymysql.cursors


class BaseTestCase(TestCase):

    def execute_query(self, connection, sql_path):
        sql = open(sql_path).read()
        cursor = connection.cursor()
        cursor.execute(sql)

    def create_database(self):
        return pymysql.connect(
            host = 'db',
            user = 'todo',
            password = 'root',
            db = 'todo',
            port = 3306,
            cursorclass = pymysql.cursors.DictCursor
        )
