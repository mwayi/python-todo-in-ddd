from todo.src.infrastructure.persistence.mysql.table import Table


class TodoRepository:

    def __init__(self, log, connection):
        self.log = log.getLogger(__name__)
        self.connection = connection

    def fetch_todos(self):
        statement = '''
            select      *

            from        {} t;
        '''.format(
            Table.TODOS
        )

        self.log.debug(statement)

        cursor = self.connection.cursor()
        cursor.execute(statement)
        return cursor.fetchall()
