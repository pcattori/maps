try:
    import collections.abc as collections_abc
except ImportError:
    import collections as collections_abc
import maps.utils as utils

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

    @classmethod
    def recurse(cls, obj, list_fn=tuple, object_fn=None):
        '''Recursively create :class:`FrozenMap` s when :py:class:`collections.Mapping`
        are encountered.

        :param obj: Object to be recursively converted.
        :param func list_fn: Conversion function applied to any :py:class:`collections.Sequence` s and :py:class:`collections.Set` s encountered. Defaults to :py:class:`tuple`.
        :param func object_fn: Conversion function applied to all other objects encountered. Defaults to the identity function.

        Usage::

           >>> import maps
           >>> fm = maps.FrozenMap.recurse({'a': 1, 'b': [2, {'c': 3}]})
           >>> fm.b[1]
           FrozenMap(c=3)
        '''
        return utils._recurse(obj, map_fn=cls, list_fn=list_fn, object_fn=object_fn)

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
