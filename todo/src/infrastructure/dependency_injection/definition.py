from todo.src.infrastructure.logging.logger import Logger
from todo.src.infrastructure.persistence.mysql.mysql import Mysql
from todo.src.infrastructure.persistence.mysql.todo_repository import TodoRepository
from todo.src.application.query.view_todo_handler import ViewTodoHandler
from todo.src.application.command.add_todo_handler import AddTodoHandler
from todo.src.application.command.complete_todo_handler import CompleteTodoHandler
from todo.src.application.command.remove_todo_handler import RemoveTodoHandler


class Definition:

    def __init__(self, environment, parameters):
        self._environment = environment
        self._parameters = parameters

    def apply_to(self, container):

        container.register_provider(
            Logger,
            lambda container: Logger.make_logger(
                self._parameters.log_level
            )
        )

        container.register_provider(
            Mysql,
            lambda container: Mysql.make_connection(
                self._environment
            )
        )

        container.register_provider(
            TodoRepository,
            lambda container: TodoRepository(
                container.provide_singleton(Logger),
                container.provide_singleton(Mysql),
            )
        )

        container.register_provider(
            ViewTodoHandler,
            lambda container: ViewTodoHandler(
                container.provide_singleton(Logger),
                container.provide_singleton(TodoRepository)
            )
        )

        container.register_provider(
            AddTodoHandler,
            lambda container: AddTodoHandler(
                container.provide_singleton(Logger),
                container.provide_singleton(TodoRepository)
            )
        )

        container.register_provider(
            CompleteTodoHandler,
            lambda container: CompleteTodoHandler(
                container.provide_singleton(Logger),
                container.provide_singleton(TodoRepository)
            )
        )

        container.register_provider(
            RemoveTodoHandler,
            lambda container: RemoveTodoHandler(
                container.provide_singleton(Logger),
                container.provide_singleton(TodoRepository)
            )
        )
