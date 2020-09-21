from todo.src.application.query.view_todo_handler import ViewTodo
from tabulate import tabulate
from todo.src.infrastructure.logging.logger import Logger


class TodoRead:

    def __init__(self, container, query_bus, environment, parameters):
        self.log_root = container.provide_singleton(Logger)
        self.log = self.log_root.getLogger(__name__)
        self.query_bus = query_bus
        self.environment = environment
        self.parameters = parameters

    def execute(self):
        if self.parameters.usecase == 'view':
            command = ViewTodo(self.parameters.filter, self.parameters.export)
            todos = self.query_bus.handle(command)
            self.log.info(tabulate(todos, headers = 'keys'))
