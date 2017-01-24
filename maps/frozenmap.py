try:
    import collections.abc as collections_abc
except ImportError:
    import collections as collections_abc

class FrozenMap(collections_abc.Mapping):
    '''An immutable, hashable key-value mapping accessible via bracket-notation
    (i.e. ``__getitem__``).

    :param args: Position arguments in the same form as the :py:class:`dict` constructor.
    :param kwargs: Keyword arguments in the same form as the :py:class:`dict` constructor.

    Usage::

       >>> import maps
       >>> fm = maps.FrozenMap({'a': 1, 'b': 2})
       >>> fm['a']
       1
       >>> list(fm.items())
       [('a', 1), ('b', 2)]
       >>> len(fm)
       2
       >>> hash(fm)
       3212389899479848432
    '''

    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)
        self._hash = None

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __hash__(self):
        if self._hash is None:
            self._hash = hash(frozenset(self.items()))
        return self._hash

    def __repr__(self): # pragma: no cover
        return '{}({!r})'.format(type(self).__name__, self._data)
