import maps.utils as utils

class NamedDict(dict):
    '''A subclass of :py:class:`dict` whose items can be accessed via standard
    bracket-notation (i.e. ``__getitem`` and ``__setitem__``) as well as
    dot-notation (i.e. ``__getattr__`` and ``__setattr__``).

    Usage::

       >>> import maps
       >>> nd = maps.NamedDict({'a': 1, 'b': 2})
       >>> nd['a']
       1
       >>> nd.b
       2
       >>> nd['c'] = 3
       >>> nd.c
       3
       >>> nd.d = 4
       >>> nd.d
       4
       >>> d = dict(nd)
       >>> d
       {'a': 1, 'b': 2, 'c': 3}
    '''

    @classmethod
    def recurse(cls, obj, list_fn=None, object_fn=None):
        '''Recursively create :class:`NamedDict` s when :py:class:`collections.Mapping`
        are encountered.

        :param obj: Object to be recursively converted.
        :param func list_fn: Conversion function applied to any :py:class:`collections.Sequence` s and :py:class:`collections.Set` s encountered. Defaults to the identity function.
        :param func object_fn: Conversion function applied to all other objects encountered. Defaults to the identity function.

        Usage::

           >>> import maps
           >>> fm = maps.NamedDict.recurse({'a': 1, 'b': [2, {'c': 3}]})
           >>> fm.b[1]
           FrozenMap(c=3)
        '''
        return utils._recurse(obj, map_fn=cls, list_fn=list_fn, object_fn=object_fn)

    def __getattr__(self, name):
        '''Retrieves the corresponding value for the specified key via
        dot-notation.

        :param str name: Key for desired item
        :raises KeyError: if the specified key is not in the dictionary.
        :return: Value of desired item
        '''
        return self[name]

    def __setattr__(self, name, value):
        '''Sets the value for the specified key via dot-notation.

        :param str name: Key for desired item
        :param value: New value of desired item
        '''
        self[name] = value

    def __repr__(self): # pragma: no cover
        return '{}({})'.format(type(self).__name__, super(NamedDict, self).__repr__())
