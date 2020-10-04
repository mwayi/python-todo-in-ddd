class CompleteTodo:

    def __init__(self, id):
        self.id = id


class CompleteTodoHandler:

    def __init__(self, log, todo_repository):
        self.log_root = log
        self.log = log.getLogger(__name__)
        self.todo_repository = todo_repository

    def handle(self, command):
        ids = list(map(int, command.id.split(',')))

        if len(ids) < 1:
            self.log.error('No ids supplied')
        else :
            self.todo_repository.complete_todos(ids)
            self.log.info('Success, those items have been marked as complete')
