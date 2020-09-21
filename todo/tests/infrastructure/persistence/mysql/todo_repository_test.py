from todo. \
    src.infrastructure.persistence.mysql.todo_repository import TodoRepository
from todo. \
    tests.infrastructure.logging.logger_dummy import LoggerDummy
from todo. \
    tests.base_test_case import BaseTestCase


class TodoRepositoryTest(BaseTestCase):

    def setUp(self):
        self.database = self.create_database(
            './todo/fixtures/database/create-database.sql'
        )
        self.logger = LoggerDummy()

    def tearDown(self):
        self.database.close()

    def test_that_we_can_retrieve_todos(self):

        self.execute_query(
            self.database,
            './todo/fixtures/database/insert-todos.sql'
        )

        subject = TodoRepository(self.logger, self.database)
        todos = subject.fetch_todos()

        self.assertEqual('3ac66762-fb8e-11ea-adc1-0242ac120002', todos[0][3])
