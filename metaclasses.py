class RegistryMeta(type):

    registry = {}

    def __new__(cls, name, bases, attrs):

        new_class = super().__new__(cls, name, bases, attrs)

        if name != "BasePlugin":
            cls.registry[name] = new_class

        return new_class

class BasePlugin(metaclass=RegistryMeta):
    pass
