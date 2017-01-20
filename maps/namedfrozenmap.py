import abc
import collections
import collections.abc
import maps.utils as utils
from maps.frozenmap import FrozenMap

class NamedFrozenMapMeta(abc.ABCMeta):
    def __new__(cls, typename, fields=[]):
        # validate names
        for name in [typename] + fields:
            utils._validate_name(name)
        utils._validate_fields(fields)

        # common methods
        def getattr__(self, name):
            try:
                return self._data[name]
            except KeyError:
                raise AttributeError(f"'{typename}' object has no attribute {name!r}")

        def setattr__(self, name, value):
            if not name.startswith('_'):
                if name in self._data:
                    raise AttributeError("can't set attribute")
                raise AttributeError(f"'{typename}' object has no attribute {name!r}")
            super(self.__class__, self).__setattr__(name, value)

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
            '    super(self.__class__, self).__init__()',
            '    self._data = collections.OrderedDict({kwargs})'])
        args = ', '.join(fields)
        kwargs = ', '.join([f'{i}={i}' for i in fields])
        namespace = {'collections': collections}
        exec(template.format(args=args, kwargs=kwargs), namespace)
        methods['__init__'] = namespace['__init__']

        return super().__new__(cls, typename, (FrozenMap,), methods)

    def __init__(cls, name, fields=[]):
        super().__init__(cls)
