import argparse
from todo.src.delivery.cli.usecase import Usecase


class Request:

    def __init__(self):

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            'usecase',
            help = 'Use cases',
            choices = (
                Usecase.TODO_ADD,
                Usecase.TODO_REMOVE,
                Usecase.TODO_COMPLETE,
                Usecase.TODO_VIEW
            )
        )

        self.parser.add_argument(
            '--d',
            required = False
        )

        self.parser.add_argument(
            '--log-level',
            help = 'Log level (debug = 0, info = 1(default), warning = 2, error = 3, critical = 4)',
            default = 1,
            type = int
        )

        self.parser.add_argument(
            '--filter',
            required = False
        )

        self.parser.add_argument(
            '--export',
            required = False
        )

    def resolve(self):
        return self.parser.parse_args()
