Maps: Python's missing mappings
===============================

Release v\ |version|. `Maps @ Github <https://github.com/pcattori/maps>`_

+------------------------+--------------------------+----------------------------+------------------------+
|                        | Frozen                   | Fixed-Key                  | Mutable                |
+------------------------+--------------------------+----------------------------+------------------------+
| Bracket-only access    | :class:`maps.FrozenMap`  | :class:`maps.FixedKeyMap`  | :py:class:`dict`       |
+------------------------+--------------------------+----------------------------+------------------------+
| Dot and bracket access | :func:`maps.namedfrozen` | :func:`maps.namedfixedkey` | :func:`maps.NamedDict` |
+------------------------+--------------------------+----------------------------+------------------------+

Testamonials
------------

**darkf**
    This is really cool. NamedDict is a useful thing indeed! [#]_

**Brando Miranda**
    I used the `beta version of this library <https://github.com/pcattori/namespaces>`_ all the time in my code! It was really simple and my code was cleaner, easier to read and write! Thanks and I am looking forward to trying out Maps now! [#]_

User Guide
----------

.. toctree::
   :maxdepth: 2

   user/design
   user/install
   user/quickstart
   user/advanced
   user/faq

Developer Interface
-------------------

.. toctree::
   :maxdepth: 2

   api

.. [#] In the context of **darkf**'s `blog post entitled "Problems I have with Python" <http://darkf.github.io/posts/problems-i-have-with-python.html>`_ `[quote source] <https://news.ycombinator.com/item?id=13483340>`__
.. [#] `[quote source] <https://news.ycombinator.com/item?id=13482814>`__
