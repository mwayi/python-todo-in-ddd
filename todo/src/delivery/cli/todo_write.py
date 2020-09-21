from todo.src.infrastructure.logging.logger import Logger


class TodoWrite:

    def __init__(self, container, command_bus, environment, parameters):
        self.log_root = container.provide_singleton(Logger)
        self.log = self.log_root.getLogger(__name__)
        self.environment = environment
        self.parameters = parameters
        self.command_bus = command_bus

    def execute(self):
        pass
