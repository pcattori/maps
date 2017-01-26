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

+------------------------+--------+-----------+------------------+
|                        | Frozen | Fixed-Key | Mutable          |
+------------------------+--------+-----------+------------------+
| Bracket-only access    | ?      | ?         | :py:class:`dict` |
+------------------------+--------+-----------+------------------+
| Dot and bracket access | ?      | ?         | ?                |
+------------------------+--------+-----------+------------------+

----

Maps fills these gaps:

+------------------------+--------------------------+----------------------------+------------------------+
|                        | Frozen                   | Fixed-Key                  | Mutable                |
+------------------------+--------------------------+----------------------------+------------------------+
| Bracket-only access    | :class:`maps.FrozenMap`  | :class:`maps.FixedKeyMap`  | :py:class:`dict`       |
+------------------------+--------------------------+----------------------------+------------------------+
| Dot and bracket access | :func:`maps.namedfrozen` | :func:`maps.namedfixedkey` | :func:`maps.NamedDict` |
+------------------------+--------------------------+----------------------------+------------------------+

Named Maps
----------

From `darkf <https://github.com/darkf>`_'s `"Problems I have with Python" <http://darkf.github.io/posts/problems-i-have-with-python.html>`_

   Python classes are useful, but it is a ton of boilerplate to write variant classes such as::

      class Node: pass

      class FooNode(Node):
          def __init__(self, x, y):
              self.x = x
              self.y = y

      class BarNode(Node): pass

   :py:class:`collections.namedtuple` would better solve this, but unfortunately they're immutable (like normal Python tuples) and thus make bad "bag of mutable data" objects.

With Named Maps its easy to define "bag of data" classes and objects with specific
levels of immutability.

----

Replace :py:class:`collections.namedtuple` with :func:`maps.namedfrozen` if you
want access by string name::

   >>> import collections
   >>> Point = collections.namedtuple('Point', ['x', 'y'])
   >>> p = Point(1, 2)
   >>> p.x
   1
   >>> p[1] # access by numerical index

   >>> import maps
   >>> Point = maps.namedfrozen('Point', ['x', 'y'])
   >>> p = Point(1, 2)
   >>> p.x
   1
   >>> p['y'] # access by string name

This is especially, for example, if you are reading JSON data, where attribute
names will be represented as strings.

----

Replace :py:class:`collections.namedtuple` with :func:`maps.namedfixedkey` if you
want access by string name and you want to edit the values for the fixed set of keys::

   >>> import collections
   >>> Point = collections.namedtuple('Point', ['x', 'y'])
   >>> p = Point(1, 2)
   >>> p = p._replace('x', p.x * -1) # not beautiful nor easy to read


   >>> import maps
   >>> Point = maps.namedfrozen('Point', ['x', 'y'])
   >>> p = Point(1, 2)
   >>> p.x *= -1 # beautiful and legible

----

Replace :py:class:`collections.namedtuple` with :class:`maps.NamedDict` if you
want `dict` under the hood instead of `tuple`::

   >>> import collections
   >>> Point = collections.namedtuple('Point', ['x', 'y'])
   >>> p = Point(1, 2)
   >>> Point3D = collections.namedtuple('Point3D', Point._fields + ('z',))
   >>> p = Point3D(p.x, p.y, 3)
   >>> p[2]
   3

   >>> import maps
   >>> p = maps.NamedDict(x=1, y=2)
   >>> p.z = 3
   >>> p['z']
   3

You may have noticed that :func:`maps.namedfrozen` and :func:`maps.namedfixedkey`
are both functions while :class:`maps.NamedDict` is a class. You might have also
noticed that :class:`maps.NamedDict` skipped creating a ``Point`` class altogether.

If you would like to know why this is the case, keep reading...

class vs function
^^^^^^^^^^^^^^^^^

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
