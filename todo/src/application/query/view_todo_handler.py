class ViewTodo:
    def __init__(
        self,
        filter,
        export
    ):
        self.filter = filter
        self.export = export


class ViewTodoHandler:
    def __init__(self, log, todo_repository):
        self.log_root = log
        self.log = log.getLogger(__name__)
        self.todo_repository = todo_repository

    def handle(self, command):
        todos = self.todo_repository.fetch_todos()

        return todos
