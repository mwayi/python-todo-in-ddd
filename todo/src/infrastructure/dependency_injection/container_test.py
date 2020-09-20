from todo. \
    src.infrastructure.dependency_injection.container import Container, FactoryNotFound
from todo.shared.base_test_case import BaseTestCase

class FakeClassA:
    def __init__(self):
        self._name = None

    def name(self):
        return self._name

    def change_name(self, name):
        self._name = name

class StubClassB:
    def __init__(self, dummy_class_a):
        pass

class StubClassC:
    def __init__(self, dummy_class_a, dummy_class_b):
        pass

class ContainerTest(BaseTestCase):

    def test_container_instance_is_not_found(self):

        container = Container()

        with self.assertRaises(FactoryNotFound):
            container.provide(FakeClassA)

    def test_container_provides_instance_of_class(self):

        container = Container()
        container.register_provider(
            FakeClassA, 
            lambda container: FakeClassA()
        )

        instance = container.provide(FakeClassA)
        
        self.assertEqual(FakeClassA, instance.__class__)

    def test_container_provides_instance_of_classes_with_dependencies(self):

        container = Container()
        container.register_provider(
            FakeClassA, 
            lambda container: FakeClassA()
        )
        container.register_provider(
            StubClassB, 
            lambda container: StubClassB(container.provide(FakeClassA))
        )
        container.register_provider(
            StubClassC, 
            lambda container: StubClassC(
                container.provide(FakeClassA), 
                container.provide(StubClassB)
            )
        )

        instance = container.provide(StubClassB)
        self.assertEqual(StubClassB, instance.__class__)

        instance = container.provide(StubClassC)
        self.assertEqual(StubClassC, instance.__class__)

    
    def test_container_can_provide_singleton(self):

        container = Container()
        container.register_provider(
            FakeClassA, 
            lambda container: FakeClassA()
        )

        instance1 = container.provide(FakeClassA)
        self.assertEqual(None, instance1.name())

        instance2 = container.provide(FakeClassA)
        instance2.change_name('foo')
        self.assertEqual(None, instance1.name())
        self.assertEqual('foo', instance2.name())

        instance1 = container.provide_singleton(FakeClassA)
        self.assertEqual(None, instance1.name())

        instance2 = container.provide_singleton(FakeClassA)
        instance2.change_name('foo')
        self.assertEqual('foo', instance1.name())
        self.assertEqual('foo', instance2.name())