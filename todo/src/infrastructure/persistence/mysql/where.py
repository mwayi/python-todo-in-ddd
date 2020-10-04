class Where:

    def __init__(self, statements = [], parameters = []):
        self.statements = statements
        self.parameters = parameters

    def has_statements(self):
        return len(self.statements) > 0

    def to_statement(self, prefix = ''):
        if self.has_statements():
            return  prefix + ' ' + (' ' .join(self.statements))

        return ''

    def to_parameters(self):
        return self.parameters