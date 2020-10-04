import uuid
import datetime
from todo. \
    src.infrastructure.persistence.mysql.todo_repository import TodoRepository
from todo. \
    tests.infrastructure.logging.logger_dummy import LoggerDummy
from todo. \
    tests.base_test_case import BaseTestCase
from todo.src.domain.model.add_todo import AddTodoBuilder
from todo.src.domain.model.todo import Todo
from expression.src.expression import Expression

class TodoRepositoryTest(BaseTestCase):

    def setUp(self):
        self.database = self.create_database()
        self.logger = LoggerDummy()

    def tearDown(self):
        self.database.close()

    def test_that_we_can_retrieve_todos(self):

        subject = TodoRepository(self.logger, self.database)
        todos = subject.fetch_todos()

        self.assertEqual('3ac66762-fb8e-11ea-adc1-0242ac120002', todos[0].get('uuid'))

    def test_that_we_can_add_todo(self):

        parameters = {}
        parameters[Todo.ID] = uuid.uuid4()
        parameters[Todo.DESCRIPTION] = 'foo'
        parameters[Todo.CREATED] = datetime.datetime.now()

        add_todo_builder = AddTodoBuilder(parameters)
        add_todo = add_todo_builder.to_add_todo()

        subject = TodoRepository(self.logger, self.database)
        subject.add_todo(add_todo)
        
        todos = subject.fetch_todos()
        self.assertEqual(str(parameters[Todo.ID]), str(todos[4].get('uuid')))


    def test_that_we_can_filter_todo_by_status_and_date(self):

        subject = TodoRepository(self.logger, self.database)
        conditions = Expression('(status = done and date between 2020-09-21,2020-09-23)').to_conditions()
        todos = subject.fetch_todos(conditions)

        self.assertEqual(1, len(todos))

    
    def test_that_we_can_mark_items_as_complete(self):

        subject = TodoRepository(self.logger, self.database)
        todos = subject.complete_todos([3])

        todos = subject.fetch_todos()
        self.assertEqual('done', str(todos[2].get('status')))
