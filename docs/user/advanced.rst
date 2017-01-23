Advanced Usage
==============

Not-so-secret attributes
------------------------

Named Maps use leading underscores to distinguish between user-defined attributes
and developer-defined attributes [#]_. This is a `common convention <https://docs.python.org/3/tutorial/classes.html#private-variables>`_, especially when implementing custom ``__setattr__``
methods and is in fact how :py:func:`collections.namedtuple` does this.

Most people are `responsible users <https://github.com/kennethreitz/python-guide/blob/master/docs/writing/style.rst#we-are-all-responsible-users>`_, so if you would like to leverage this
convention to provide additional attributes, you can do so::

   >>> import maps
   >>> RGB = maps.namedfrozen('RGB', ['red', 'green', 'blue'])
   >>> lavender = RGB(230, 230, 250)
   >>> lavender._is_purpleish = True
   >>> lavender
   RGB(red=230, green=230, blue=250)
   >>> lavender._is_purpleish
   True

.. [#] In this context `user` refers to someone who uses Maps, whereas `developer`
       refers to someone who contributes to the Maps code-base

