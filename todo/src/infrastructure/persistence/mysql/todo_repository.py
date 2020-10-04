from todo.src.infrastructure.persistence.mysql.table import Table
from todo.src.infrastructure.persistence.mysql.where import Where
from expression.src.condition import Condition, Conjunction
from datetime import datetime


class TodoRepository:

    def __init__(self, log, connection):
        self.log = log.getLogger(__name__)
        self.connection = connection

    def fetch_todos(self, conditions = None):
        where = self._transform_conditions_to_where(conditions)
        statement = '''
            select      *

            from        {} t
            {}
        '''.format(
            Table.TODOS,
            where.to_statement('where')
        )

        cursor = self.connection.cursor()
        cursor.execute(statement, where.to_parameters())
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

    def _transform_conditions_to_where(self, conditions):
        if conditions is None:
            return Where()
        
        statements = []
        parameters = []
        for condition in conditions.conditions:
            if isinstance(condition, Conjunction):
                statements.append(condition.value)

            if isinstance(condition, Condition):
                if condition.key == 'date' and condition.operator == 'between':
                    values = condition.value.split(',')
                    parameters.append(str(datetime.strptime(values[0], '%Y-%m-%d')))
                    parameters.append(str(datetime.strptime(values[1], '%Y-%m-%d')))
                    statements.append("(t.created between %s and %s)")

                if condition.key == 'status':
                    parameters.append(condition.value)
                    statements.append("(t.status = %s)")
        
        return Where(statements, parameters)
