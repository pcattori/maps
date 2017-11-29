Developer Interface
===================

Maps
----

.. autoclass:: maps.FrozenMap
    :members: recurse
.. autoclass:: maps.FixedKeyMap
    :members: recurse

Named Maps
----------

.. autofunction:: maps.namedfrozen
.. autofunction:: maps.namedfixedkey
.. autoclass:: maps.NamedDict
   :members: __getattr__, __setattr__, recurse

Named Map MetaClasses
---------------------

The `Named Maps`_ section details :func:`maps.namedfrozen` and
:func:`maps.namedfixedkey`, which are the recommended way to instantiate Named Map
classes. Under the hood, those 2 functions leverage the metaclasses detailed below.

.. autoclass:: maps.NamedFrozenMapMeta
    :members: _getattr, _setattr
.. autoclass:: maps.NamedFixedKeyMapMeta
    :members: _getattr, _setattr

