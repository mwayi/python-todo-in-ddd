class ActionNotFound(Exception):
    pass

class AbstractBus:

    def __init__(self, handler_map = {}):
        self._handler_map = handler_map

    def handle(self, action):
        if action in self._handler_map:
            return self._handler_map[action].handle(action)

        raise ActionNotFound('Handler does not exist for "%s"'.format(action.__class__))
