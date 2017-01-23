import abc
import collections
import collections.abc
import maps.utils as utils
from maps.frozenmap import FrozenMap

class NamedFrozenMapMeta(abc.ABCMeta):
    '''Returns a new :class:`maps.FrozenMap` subclass named ``typename``. The new
    subclass is used to create :py:class:`dict`-like objects that have fields
    accessible by attribute lookup as well as being indexable by name and iterable.
    Instances of the subclass also have a helpful docstring (with typename and
    field_names) and a helpful __repr__() method which lists the mapping contents
    in a name=value format.

    ``field_names`` can be a sequence of strings such as ``['x', 'y']``.

    Any valid Python identifier may be used for a fieldname except for names
    starting with an underscore. Valid identifiers consist of letters, digits,
    and underscores but do not start with a digit or underscore and cannot be a
    keyword such as class, for, return, global, pass, or raise.

    This metaclass injects 3 methods into the subclass:
    ``__getattr__``, ``__setattr__``, and ``__repr__``.

    1. ``__getattr__`` attempts to retrieve attributes from an instance's
    underlying ``_data`` dictionary, raising :py:exc:`AttributeError`
    if the attribute is not found.

    2. ``__setattr__`` raises :py:exc:`TypeError` unless the
    attribute name has a leading underscore, in which case the attribute will be
    set normally.

    3. ``__repr__`` simply replaces ``FrozenMap`` with the name of the instantiated
    class.

    :func:`maps.namedfrozen` provides a convenient alias for calling this metaclass.

    :param str typename: Name for the new class
    :param iterable fields: Names for the fields of the new class
    :raises ValueError: if the type name or field names provided are not properly formatted
    :return: Newly created subclass of :class:`maps.FrozenMap`
    '''

    @staticmethod
    def _getattr(self, name):
        '''Retrieves attribute by name.

        :param str name: Name of the desired attribute
        :raises AttributeError: if an attribute with the specified name cannot be found
        :return: Desired attribute
        '''
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute {name!r}")

    @staticmethod
    def _setattr(self, name, value):
        '''Raises a TypeError as attribute assignment is not supported.

        :raises TypeError:
        '''
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

        cls.__doc__ = f'''{typename}: An immutable, hashable key-value mapping
        accessible via bracket-notation (i.e. ``__getitem__``). Has fields
        ({cls._fields}).

        :param args: Position arguments in the same form as the :py:class:`dict` constructor.
        :param kwargs: Keyword arguments in the same form as the :py:class:`dict` constructor.
        '''

        return super().__new__(cls, typename, (FrozenMap,), methods)

    def __init__(cls, typename, fields=[]):
        super().__init__(cls)
