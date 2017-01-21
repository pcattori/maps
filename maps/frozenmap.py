import collections.abc

class FrozenMap(collections.abc.Mapping):

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
        '''Caches lazily-computed hash value.'''
        if self._hash is None:
            self._hash = hash(frozenset(self.items()))
        return self._hash

    def __repr__(self): # pragma: no cover
        return f'{type(self).__name__}({self._data!r})'
