from maps.fixedkeymap import FixedKeyMap
from maps.frozenmap import FrozenMap
from maps.nameddict import NamedDict
from maps.namedfixedkeymap import NamedFixedKeyMapMeta
from maps.namedfrozenmap import NamedFrozenMapMeta

def namedfrozen(typename, fields, defaults={}):
    '''Creates a new class that inherits from :class:`maps.FrozenMap` that has the
    specified fields as keys. Fields are accessible via bracket-notation
    (i.e. ``__getitem__``) as well as dot-notation (i.e. ``__getattr__``).
    Instances of the returned class are immutable.

    :param str typename: Name of the new Map class
    :param iterable fields: Names of the fields
    :param mapping defaults: Maps default values to fields
    :raises ValueError: if the type name or field names or defaults provided are not properly formatted
    :return: The newly created class
    :rtype: class

    Usage::

       >>> import maps
       >>> RGB = maps.namedfrozen('RGB', ['red', 'green', 'blue'], defaults={'green': 127, 'blue': 80})
       >>> coral = RGB(255)
       >>> coral['red']
       255
       >>> coral.green
       127
    '''
    return NamedFrozenMapMeta(typename, fields, defaults)

def namedfixedkey(typename, fields, defaults={}):
    '''Creates a new class that inherits from :class:`maps.FixedKeyMap` that has the
    speciefied fields as keys. Fields are accessible via bracket-notation
    (i.e. ``__getitem__``) as well as dot-notation (i.e. ``__getattr__``).
    Instances of the returned class have a fixed set of keys, but the values
    corresponding to those keys can be edited.

    :param str typename: Name of the new Map class
    :param iterable fields: Names of the fields
    :param mapping defaults: Maps default values to fields
    :raises ValueError: if the type name or field names or defaults provided are not properly formatted
    :return: The newly created class
    :rtype: class

    Usage::

       >>> import maps
       >>> Person = maps.namedfixedkey('Person', ['name', 'gender', 'age'], defaults={'age': 40})
       >>> bob = Person('bob', 'male')
       >>> bob['name']
       'bob'
       >>> bob.gender
       'male'
       >>> bob.age += 1
       >>> bob.age
       41
    '''
    return NamedFixedKeyMapMeta(typename, fields, defaults)
