import abc
import collections
import namedmaps.utils as utils

class NamedMap(abc.ABCMeta):
    def __new__(cls, typename, fields=[]):
        # validate names
        for name in [typename] + fields:
            utils._validate_name(name)
        utils._validate_fields(fields)

        # common methods
        def getattr__(self, name):
            return self._data[name]

        def setattr__(self, name, value):
            if not name.startswith('_'):
                raise AttributeError(f"'{typename}' object has no attribute {name!r}")
            super(self.__class__, self).__setattr__(name, value)

        def repr__(self):
            kwargs = ', '.join(f'{key}={value!r}' for key, value in self.items())
            return f'{typename}({kwargs})'

        methods = {
            '__getattr__': getattr__,
            '__getitem__': lambda self, name: self._data[name],
            '__iter__': lambda self: iter(self._data),
            '__len__': lambda self: len(self._data),
            '__repr__': repr__}
            '__setattr__': setattr__,

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

        return super().__new__(cls, typename, (collections.Mapping,), methods)

    def __init__(cls, name, fields=[]):
        super().__init__(cls)
