from todo. \
    src.application.query.view_todo_handler import ViewTodo, ViewTodoHandler


class MakeQueryBus:
    def __init__(self, container, bus):
        self.container = container
        self.bus = bus

    def make_bus(self):
        return self.bus({
            ViewTodo: self.container.provide(ViewTodoHandler)
        })
