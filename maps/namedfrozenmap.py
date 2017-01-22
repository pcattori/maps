import abc
import collections
import collections.abc
import maps.utils as utils
from maps.frozenmap import FrozenMap

class NamedFrozenMapMeta(abc.ABCMeta):
    @staticmethod
    def _getattr(self, name):
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute {name!r}")

    @staticmethod
    def _setattr(self, name, value):
        if not name.startswith('_'):
            raise TypeError(
                f"'{type(self).__name__}' object does not support attribute assignment")
        super(type(self), self).__setattr__(name, value)

    @staticmethod
    def _repr(self): # pragma: no cover
        kwargs = ', '.join(f'{key}={value!r}' for key, value in self.items())
        return f'{type(self).__name__}({kwargs})'

    def __new__(cls, typename, fields=[]):
        fields = tuple(fields)
        # validate names
        for name in (typename,) + fields:
            utils._validate_name(name)
        utils._validate_fields(fields)

        cls._fields = fields

        methods = {
            '__getattr__': NamedFrozenMapMeta._getattr,
            '__repr__': NamedFrozenMapMeta._repr,
            '__setattr__': NamedFrozenMapMeta._setattr}

        # handle custom __init__
        template = '\n'.join([
            'def __init__(self, {args}):',
            '    super(type(self), self).__init__()',
            '    self._data = collections.OrderedDict({kwargs})'])
        args = ', '.join(fields)
        kwargs = ', '.join([f'{i}={i}' for i in fields])
        namespace = {'collections': collections}
        exec(template.format(args=args, kwargs=kwargs), namespace)
        methods['__init__'] = namespace['__init__']

        return super().__new__(cls, typename, (FrozenMap,), methods)

    def __init__(cls, name, fields=[]):
        super().__init__(cls)
