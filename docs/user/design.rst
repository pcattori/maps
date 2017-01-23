Design
======

Design Principles
-----------------

Syntax should convey intent.

----

Choice of data structure should convey intent.

----

From `PEP 20 <https://www.python.org/dev/peps/pep-0020/#the-zen-of-python>`_.

   Beautiful is better than ugly.

   Explicit is better than implicit.

   Readability counts.

----

Within reason, Maps should be interoperable with :py:class:`dict`.

Why Python needs Maps
---------------------

Python has a mutable mapping implementation in :py:class:`dict`.

But Python is missing:

1. An immutable, hashable mapping (e.g. ``frozendict`` ala `PEP 416 <https://www.python.org/dev/peps/pep-0416/>`_)

2. A fixed-key mapping

3. Access-by-name / dot-notation via ``__getattr__`` and ``__setattr__`` (ala :py:func:`collections.namedtuple`) for: (3.a) immutable, (3.b) fixed-key, and (3.c) mutable mappings

+-------------------------+--------+-----------+------------------+
|                         | Frozen | Fixed-Key | Mutable          |
+-------------------------+--------+-----------+------------------+
| Bracket-notation access | ?      | ?         | :py:class:`dict` |
+-------------------------+--------+-----------+------------------+
| Dot-notation access     | ?      | ?         | ?                |
+-------------------------+--------+-----------+------------------+

----

Maps fills these gaps:

1. :class:`maps.FrozenMap`

2. :class:`maps.FixedKeyMap`

3. Access-by-name / dot-notation:

   a. :func:`maps.namedfrozen`

   b. :func:`maps.namedfixedkey`

   c. :class:`maps.NamedDict`

+-------------------------+--------------------------+----------------------------+------------------------+
|                         | Frozen                   | Fixed-Key                  | Mutable                |
+-------------------------+--------------------------+----------------------------+------------------------+
| Bracket-notation access | :class:`maps.FrozenMap`  | :class:`maps.FixedKeyMap`  | :py:class:`dict`       |
+-------------------------+--------------------------+----------------------------+------------------------+
| Dot-notation access     | :func:`maps.namedfrozen` | :func:`maps.namedfixedkey` | :func:`maps.NamedDict` |
+-------------------------+--------------------------+----------------------------+------------------------+

Named Maps: class vs function
-----------------------------

Just like :py:func:`collections.namedtuple`, :func:`maps.namedfrozen` and
:func:`maps.namedfixedkey` are **functions** that help you to dynamically
instantiate new classes with a fixed set of fields.

   >>> import maps
   >>> RGB = maps.namedfrozen('RGB', ['red', 'green', 'blue']) # create RGB class; all RGB instances are guaranteed to have only `red`, `green`, and `blue` fields
   >>> cerulean_rgb = RGB(0, 123, 167) # make an instance of `RGB`


   >>> import maps
   >>> CMYK = maps.namedfixedkey('CMYK', ['cyan', 'magenta', 'yellow', 'black']) # create CMYK class; all CMYK instances are guaranteed to have only `cyan`, `magenta`, `yellow`, and `black` fields
   >>> cerulean_cmyk = CMYK(100, 26, 0, 35) # make an instance of `CMYK`

Encapsulating knowledge of the fields into a class makes code easier to reason
about as it makes guarantees as to what fields will be available. So when
possible, its nice to encode the fixed set of fields into a class.
E.g. :py:func:`collections.namedtuple` is able to do this since :py:class:`tuple`
is immutable.

   >>> import collections
   >>> Point = namedtuple('Point', ['x', 'y']) # dynamically instantiate the `Point` class with a fixed set of fields (`x`, `y`)
   >>> p = Point(11, y=22) # make an instance of `Point`


Since :class:`maps.NamedDict` represents a fully mutable mapping, there is not a
notion of a "fixed set of fields". As such, it does not make sense to make a new
class for every "fixed set of fields". Therefore, :class:`maps.NamedDict` is
simply a **class**.

   >>> import maps;
   >>> bob = maps.NamedDict(name='bob', age=40)
   >>> bob.height = 1.76 # meters
   >>> bob['hobbies'] = ('tennis', 'tv')

Leading Underscore
------------------

Commandeering dot-notation (e.g. ``__getattr__`` and ``__setattr__``) makes code
more `beautiful and readable <Design Principles>`_, but overriding ``__setattr__``
can cause internals to blow up if one is not careful.

Maps borrows the "leading underscore" approach from
:py:func:`collections.namedtuple`. In particular it leverages the convention that
attributes with a leading underscore are `not part of the intended API <https://docs.python.org/3/tutorial/classes.html#private-variables>`_, but still allows `responsible users <https://github.com/kennethreitz/python-guide/blob/master/docs/writing/style.rst#we-are-all-responsible-users>`_ to access those attributes.
