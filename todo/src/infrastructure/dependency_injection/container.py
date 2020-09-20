class FactoryNotFound(Exception):
    pass

class Container:

    def __init__(self):
        self._providers = {}
        self._singletons = {}

    def register_provider(self, name, factory):
        self._providers[name] = factory

    def provide(self, name):
        if name in self._providers:
            return self._providers[name](self)
        raise FactoryNotFound('Factory [%s] not found.'.format(name))

    def provide_singleton(self, name):
        if name not in self._singletons:
            self._singletons[name] = self.provide(name)
        return self._singletons[name]