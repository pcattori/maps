Quickstart
==========

Eager to get started? This page gives a good introduction in how to get started
with Maps.

First, make sure that:

   1. Maps is installed: ``pip install maps``

   2. Maps is up-to-date: ``pip install --upgrade maps``

A compass for your Map
----------------------

+-------------------------+--------------------------+----------------------------+------------------------+
|                         | Frozen                   | Fixed-Key                  | Mutable                |
+-------------------------+--------------------------+----------------------------+------------------------+
| Bracket-notation access | :class:`maps.FrozenMap`  | :class:`maps.FixedKeyMap`  | :py:class:`dict`       |
+-------------------------+--------------------------+----------------------------+------------------------+
| Dot-notation access     | :func:`maps.namedfrozen` | :func:`maps.namedfixedkey` | :func:`maps.NamedDict` |
+-------------------------+--------------------------+----------------------------+------------------------+

