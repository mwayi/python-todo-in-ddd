import os
from dotenv import load_dotenv
from todo.src.infrastructure.cqrs.abstract_bus import AbstractBus
from todo.src.infrastructure.dependency_injection.container import Container
from todo.src.infrastructure.dependency_injection.definition import Definition
from todo.src.delivery.cli.todo_read import TodoRead
from todo.src.delivery.cli.todo_write import TodoWrite
from todo.src.delivery.cli.usecase import Usecase
from todo.src.delivery.cli.request import Request
from todo.src.application.command.make_command_bus import MakeCommandBus
from todo.src.application.query.make_query_bus import MakeQueryBus


class Cli:

    def process(self):
        parameters = Request().resolve()
        container = Container()

        if (os.path.isfile('./.env') is False):
            print('Failed to load the envrionment file .env')
            return

        load_dotenv()

        Definition(os.environ, parameters).apply_to(container)

        try:
            Definition(os.environ, parameters).apply_to(container)
        except Exception:
            print('Failed to connect to the database')
            return

        try:
            if parameters.usecase in (Usecase.TODO_VIEW):
                query_bus = MakeQueryBus(container, AbstractBus).make_bus()
                usecase = TodoRead(container, query_bus, os.environ, parameters)
                usecase.execute()
            return

            if parameters.usecase in (Usecase.TODO_ADD, Usecase.TODO_REMOVE, Usecase.TODO_COMPLETE):
                command_bus = MakeCommandBus(container, AbstractBus).make_bus()
                usecase = TodoWrite(container, command_bus, os.environ, parameters)
                usecase.execute()
                return

        finally:
            pass


if __name__ == '__main__':
    Cli().process()
