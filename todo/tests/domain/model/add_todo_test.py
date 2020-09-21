import uuid
import datetime
from todo.src.domain.model.status import Status
from todo.src.domain.model.todo import Todo
from todo.src.domain.model.add_todo import AddTodo, AddTodoBuilder
from todo.tests.base_test_case import BaseTestCase
from todo.src.domain.model.exceptions import RequiredParameterNotFound


class AddTodoTest(BaseTestCase):

    def test_add_todo_can_be_built_from_builder(self):

        parameters = {}
        parameters[Todo.ID] = uuid.uuid4()
        parameters[Todo.DESCRIPTION] = 'foo'
        parameters[Todo.CREATED] = datetime.datetime.now()

        add_todo_builder = AddTodoBuilder(parameters)
        add_todo = add_todo_builder.to_add_todo()

        self.assertEqual(parameters[Todo.ID], add_todo.id)
        self.assertEqual(parameters[Todo.DESCRIPTION], add_todo.description)
        self.assertEqual(parameters[Todo.CREATED], add_todo.created)
        self.assertEqual(add_todo.status, Status.TODO)

    def test_add_todo_not_built_when_required_parameters_missing(self):
        
        parameters = {}
       
        with self.assertRaises(RequiredParameterNotFound):
            AddTodoBuilder(parameters)
        
        parameters[Todo.ID] = uuid.uuid4()
        with self.assertRaises(RequiredParameterNotFound):
            AddTodoBuilder(parameters)
        
        parameters[Todo.DESCRIPTION] = 'foo'
        with self.assertRaises(RequiredParameterNotFound):
            AddTodoBuilder(parameters)
