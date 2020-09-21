from todo. \
    src.infrastructure.cqrs.abstract_bus import AbstractBus, ActionNotFound
from todo.tests.base_test_case import BaseTestCase


class StubCommand:
    pass


class SpyCommandHandler:
    def __init__(self):
        self.command_handled = None

    def handle(self, command):
        self.command_handled = command


class AbstractBusTest(BaseTestCase):

    def test_abstract_bus_handler_is_not_found(self):

        abstract_bus = AbstractBus()

        with self.assertRaises(ActionNotFound):
            abstract_bus.handle(StubCommand)

    def test_abstract_bus_can_handle_command(self):

        spy_command_handler = SpyCommandHandler()
        abstract_bus = AbstractBus({
            StubCommand: spy_command_handler
        })

        abstract_bus.handle(StubCommand)

        self.assertEqual(StubCommand, spy_command_handler.command_handled)
