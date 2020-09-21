from todo.src.domain.model.todo import Todo
from todo.src.domain.model.status import Status
from todo.src.domain.model.exceptions import RequiredParameterNotFound


class AddTodo:

    def __init__(
        self,
        id,
        description,
        created,
        status,
        deleted = None
    ):
        self.id = id
        self.description = description
        self.created = created
        self.status = status
        self.deleted = deleted


class AddTodoBuilder:

    REQUIRED_PARAMETERS = (
        Todo.ID,
        Todo.DESCRIPTION,
        Todo.CREATED
    )

    def __init__(self, parameters):
        self.parameters = self.resolve_paramaters(parameters)

    def resolve_paramaters(self, parameters):
        for parameter in self.REQUIRED_PARAMETERS:
            if parameter not in parameters:
                raise RequiredParameterNotFound('{}'.format(parameter))

        parameters[Todo.STATUS] = Status.TODO
        parameters[Todo.DELETED] = None

        return parameters

    def to_add_todo(self):
        return AddTodo(
            self.parameters[Todo.ID],
            self.parameters[Todo.DESCRIPTION],
            self.parameters[Todo.CREATED],
            self.parameters[Todo.STATUS],
            self.parameters[Todo.DELETED]
        )
