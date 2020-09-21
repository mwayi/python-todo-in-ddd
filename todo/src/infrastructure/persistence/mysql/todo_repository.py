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
        self.log.debug(cursor._last_executed)
        return cursor.fetchall()

    def add_todo(self, add_todo):
        statement = """
            insert into {} (
                `uuid`,
                `description`,
                `created`,
                `status`
            ) values (%s, %s, %s, %s)
        """.format(
            Table.TODOS
        )

        parameters = (
            str(add_todo.id), 
            add_todo.description,
            str(add_todo.created),
            add_todo.status.value
        )

        cursor = self.connection.cursor()
        cursor.execute(statement, parameters)
        self.log.debug(cursor._last_executed)
        self.connection.commit()
    