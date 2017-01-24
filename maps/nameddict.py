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
        return '{}({})'.format(type(self).__name__, super(type(self), self).__repr__())
