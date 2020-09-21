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

class TodoRepositoryTest(BaseTestCase):

    def setUp(self):
        self.database = self.create_database(
            './todo/fixtures/database/create-database.sql'
        )
        self.logger = LoggerDummy()

    def tearDown(self):
        self.database.close()

    def test_that_we_can_retrieve_todos(self):
        ## Abandon test
        self.execute_query(
            self.database,
            './todo/fixtures/database/insert-todos.sql'
        )

        subject = TodoRepository(self.logger, self.database)
        todos = subject.fetch_todos()

        self.assertEqual('3ac66762-fb8e-11ea-adc1-0242ac120002', todos[0][3])

    def test_that_we_can_add_todo(self):
        ## Abandon test
        parameters = {}
        parameters[Todo.ID] = uuid.uuid4()
        parameters[Todo.DESCRIPTION] = 'foo'
        parameters[Todo.CREATED] = datetime.datetime.now()

        add_todo_builder = AddTodoBuilder(parameters)
        add_todo = add_todo_builder.to_add_todo()

        subject = TodoRepository(self.logger, self.database)
        subject.add_todo(add_todo)
        
        todos = subject.fetch_todos()
        self.assertEqual(str(parameters[Todo.ID]), todos[0][3])
        self.assertEqual(str(parameters[Todo.CREATED]), todos[0][1])
