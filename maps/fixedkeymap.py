try:
    import collections.abc as collections_abc
except ImportError:
    import collections as collections_abc
import maps.utils as utils

class FixedKeyMap(collections_abc.MutableMapping):
    '''A key-value mapping with a fixed set of keys whose items are accessible
    via bracket-notation (i.e. ``__getitem__`` and ``__setitem__``). Though the
    set of keys is immutable, the corresponding values can be edited.

    :param args: Position arguments in the same form as the :py:class:`dict` constructor.
    :param kwargs: Keyword arguments in the same form as the :py:class:`dict` constructor.

    Usage::

       >>> import maps
       >>> fkm = maps.FixedKeyMap({'a': 1, 'b': 2})
       >>> fkm['a']
       1
       >>> fkm['b'] += 10
       >>> fkm['b']
       12
       >>> list(fkm.items())
       [('a', 1), ('b', 12)]
       >>> len(fkm)
       2
    '''

    @classmethod
    def recurse(cls, obj, list_fn=None, object_fn=None):
        '''Recursively create :class:`FixedKeyMap` s when :py:class:`collections.Mapping`
        are encountered.

        :param obj: Object to be recursively converted.
        :param func list_fn: Conversion function applied to any :py:class:`collections.Sequence` s and :py:class:`collections.Set` s encountered. Defaults to the identity function.
        :param func object_fn: Conversion function applied to all other objects encountered. Defaults to the identity function.

        Usage::

           >>> import maps
           >>> fkm = maps.FixedKeyMap.recurse({'a': 1, 'b': [2, {'c': 3}]})
           >>> fkm.b[1]
           FixedKeyMap(c=3)
        '''
        return utils._recurse(obj, map_fn=cls, list_fn=list_fn, object_fn=object_fn)

    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)

    def __getitem__(self, name):
        return self._data[name]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __delitem__(self, name):
        raise TypeError(
            "'{}' object does not support item deletion".format(type(self).__name__))

    def __setitem__(self, name, value):
        if name not in self._data:
            raise TypeError(
                "'{}' object does not support new item assignment".format(type(self).__name__))
        self._data[name] = value

    def __repr__(self): # pragma: no cover
        return '{}({!r})'.format(type(self).__name__, self._data)
