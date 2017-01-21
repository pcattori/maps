import abc
import maps.utils as utils
from maps.fixedkeymap import FixedKeyMap

class NamedFixedKeyMapMeta(abc.ABCMeta):
    def __new__(cls, typename, fields=[]):
        fields = tuple(fields)
        # validate names
        for name in (typename,) + fields:
            utils._validate_name(name)
        utils._validate_fields(fields)

        cls._fields = fields

        def getattr__(self, name):
            try:
                return self._data[name]
            except KeyError:
                raise AttributeError(f"'{typename}' object has no attribute {name!r}")

        def setattr__(self, name, value):
            if name.startswith('_'):
                super(self.__class__, self).__setattr__(name, value)
            elif name in self._data:
                self._data[name] = value
            else:
                raise TypeError(
                    f"'{typename}' object does not support new attribute assignment")

        def repr__(self): # pragma: no cover
            kwargs = ', '.join(f'{key}={value!r}' for key, value in self.items())
            return f'{typename}({kwargs})'

        methods = {
            '__getattr__': getattr__,
            '__repr__': repr__,
            '__setattr__': setattr__}

        # handle custom __init__
        template = '\n'.join([
            'def __init__(self, {args}):',
            '    super(self.__class__, self).__init__({kwargs})'])
        args = ', '.join(fields)
        kwargs = ', '.join([f'{i}={i}' for i in fields])
        exec(template.format(args=args, kwargs=kwargs), methods)

        return super().__new__(cls, typename, (FixedKeyMap,), methods)

    def __init__(cls, name, fields=[]):
        super().__init__(cls)
