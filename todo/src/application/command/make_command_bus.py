from todo. \
    src.application.command.add_todo_handler import AddTodo, AddTodoHandler
from todo. \
    src.application.command.complete_todo_handler import CompleteTodo, CompleteTodoHandler
from todo. \
    src.application.command.remove_todo_handler import RemoveTodo, RemoveTodoHandler


class MakeCommandBus:
    def __init__(self, container, bus):
        self.container = container
        self.bus = bus

    def make_bus(self):
        return self.bus({
            AddTodo: self.container.provide(AddTodoHandler),
            CompleteTodo: self.container.provide(CompleteTodoHandler),
            RemoveTodo: self.container.provide(RemoveTodoHandler)
        })
