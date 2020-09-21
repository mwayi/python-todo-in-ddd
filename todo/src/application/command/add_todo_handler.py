import uuid
import datetime
from todo.src.domain.model.status import Status
from todo.src.domain.model.todo import Todo
from todo.src.domain.model.add_todo import AddTodo, AddTodoBuilder


class AddTodo:

    def __init__(
        self,
        description
    ):
        self.description = description


class AddTodoHandler:

    def __init__(self, log, todo_repository):
        self.log_root = log
        self.log = log.getLogger(__name__)
        self.todo_repository = todo_repository

    def handle(self, command):
        print(111, command.description)

        parameters = {}
        parameters[Todo.ID] = uuid.uuid4()
        parameters[Todo.DESCRIPTION] = command.description
        parameters[Todo.CREATED] = datetime.datetime.now()

        add_todo_builder = AddTodoBuilder(parameters)
        add_todo = add_todo_builder.to_add_todo()
        self.todo_repository.add_todo(add_todo)
