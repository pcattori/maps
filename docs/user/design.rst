Design
======

Slogan: Syntax should convey intent!

Yes, you could do all this stuff with just :py:class:`dict` and
:py:func:`collections.namedtuple`. But it gets unwieldly.
MORE IMPORTANTLY, it does not convey your intentions to someone reading your code!
Syntax should convey intent!

``namedtuple``, but for ``dict``
--------------------------------

- `namedtuple`, but with names, not indices
    - Conveys that the developer knows about this key/value.
- metaclass approach
- eg. partitioning via leading `_` (link to advanced usage)

- BUT: tuples are immutable, and dicts are not... (leads to 3 levels of immutability)

3 Levels of Immutability
------------------------

Frozen
^^^^^^

Although `PEP 406 <https://www.python.org/dev/peps/pep-0416/>`_ was rejected,
people still want a `frozendict`

Fixed Key
^^^^^^^^^

like::

    class Struct:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

BUT, this is missing a bunch of the :py:class:`collections.abc.Mapping` interface!
- `__len__`, `__iter__`, `__contains__`, `get`, etc...

BUT, new attributes can be added! (Probably not an issue for the developer who
is writing the code as they will just keep this in mind. But for a person reading
the code, you are left wondering... "Am I guaranteed that an instance of this
class won't have crazy attributes later on?") Syntax should convey intent!

Mutable
^^^^^^^

Luckily, Python already has :py:class:`dict`, so Maps just needs to implement
``maps.NamedDict``
