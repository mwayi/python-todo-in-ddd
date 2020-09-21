import pymysql
import pymysql.cursors


class Mysql:

    @staticmethod
    def make_connection(environment):
        return pymysql.connect(
            host = environment.get('DATABASE_HOST'),
            user = environment.get('DATABASE_USER'),
            password = environment.get('DATABASE_PASS'),
            db = environment.get('DATABASE_NAME'),
            port = int(environment.get('DATABASE_PORT')),
            charset = environment.get('DATABASE_CHARSET'),
            cursorclass = pymysql.cursors.DictCursor
        )
