[![PyPI version](https://badge.fury.io/py/maps.svg)](https://badge.fury.io/py/maps)
[![Build Status](https://travis-ci.org/pcattori/maps.svg?branch=master)](https://travis-ci.org/pcattori/maps)
[![Test Code Coverage](https://codecov.io/gh/pcattori/maps/branch/master/graph/badge.svg)](https://codecov.io/gh/pcattori/maps)

# maps

## Install

```sh
$ pip install maps
```
## API

### NamedDict

Just a plain ol' Python `dict`, but super-charged with access via dot-notation
(i.e. `__getattr__` and `__setattr__`).

```python
>>> import maps
>>> d = maps.NamedDict({'a': 1, 'b': 2})
>>> isinstance(d, dict) # drop-in replacement for a `dict`! Can do anything a `dict` can!
True
>>> d.a
1
>>> d.b = 'two'
>>> d
NamedDict({'a': 1, 'b': 'two'})
>>> d.c = 3
>>> d
NamedDict({'a': 1, 'b': 'two', 'c': 3})
>>> d.d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'd'
```

### namedfrozen

`namedfrozen` is like `namedtuple`, but with `collections.abc.Mapping` under the
hood instead of `tuple`.

In other words, its an immutable mapping with access via bracket-notation
(i.e. `__getitem__`) as well as dot-notation (i.e. `__getattr__`).

```python
>>> import maps
>>> RGB = maps.namedfrozen('RGB', ['red', 'green', 'blue'])
>>> rgb = RGB(red='rouge', green='forest', blue='azul')
>>> print(rgb)
RGB(red='rouge', green='forest', blue='azul')
>>> rgb['red'] # access via bracket-notation
'rouge'
>>> rgb.green # access via dot-notation
'forest'

>>> rgb['grey']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'grey'

>>> rgb['grey'] = 'pewter'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'RGB' object does not support item assignment

>>> rgb.gray
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'RGB' object has no attribute 'gray'

>>> rgb.gray = 'pewter'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'RGB' object does not support attribute assignment

>>> rgb.blue = 'topaz' # NamedMaps are immutable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'RGB' object does not support attribute assignment
```

### namedfixedkey

The `namedfixedkey` variant is more flexible, allowing edits to existing keys.

```python
>>> import maps
>>> CMYK = maps.namedfixkey('CMYK', ['cyan', 'magenta', 'yellow', 'black'])
>>> cmyk = CMYK(255, 30, 25, 55) # same API as `namedfrozen`, except...
>>> print(cymk)
CMYK(255, 30, 25, 55)
>>> cmyk['magenta'] = 'periwinkle' # overwrite existing items
>>> cmyk.black += 45 # overwrite existing items
>>> print(cmyk)
CMYK(255, 30, 25, 100)

>>> cmyk['grey']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'grey'

>>> rgb['grey'] = 'pewter' # cannot add new keys
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'CMYK' object does not support new item assignment

>>> cmyk.gray
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'CMYK' object has no attribute 'gray'

>>> rgb.gray = 'pewter' # cannot add new keys
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'CMYK' object does not support new attribute assignment
```
