try:
    import collections.abc as collections_abc
except ImportError:
    import collections as collections_abc

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

