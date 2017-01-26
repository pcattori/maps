[![PyPI version](https://badge.fury.io/py/maps.svg)](https://badge.fury.io/py/maps)
[![Build Status](https://travis-ci.org/pcattori/maps.svg?branch=master)](https://travis-ci.org/pcattori/maps)
[![Test Code Coverage](https://codecov.io/gh/pcattori/maps/branch/master/graph/badge.svg)](https://codecov.io/gh/pcattori/maps)
[![Compatible Python Versions](https://img.shields.io/pypi/pyversions/maps.svg)](https://pypi.python.org/pypi/maps)
[![Documentation Status](https://readthedocs.org/projects/maps/badge/?version=latest)](http://maps.readthedocs.io/en/latest/?badge=latest)

# maps

Python's missing mappings

|                        | Frozen             | Fixed-key            | Mutable          |
| ---                    | ---                | ---                  | ---              |
| bracket access         | `maps.FrozenMap`   | `maps.FixedKeyMap`   | `dict`           |
| dot and bracket access | `maps.namedfrozen` | `maps.namedfixedkey` | `maps.NamedDict` |

## Install

```sh
$ pip install maps
```
## API

Check out the [official Maps docs](http://maps.readthedocs.io/) for more!

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
```
