# namedmaps

## Install

```sh
$ pip install namedmaps
```
## API

Quick way: use `namedmap` convenience function.

```python
>>> from namedmaps import namedmap
>>> RGB = namedmap('RGB', ['red', 'green', 'blue'])
>>> rgb = RGB(red='rouge', green='forest', blue='azul')
# ...
>>> CMYK = namedmap('CMYK', ['cyan', 'magenta', 'yellow', 'black'], mutable_values=True)
>>> cmyk = CMYK(255, 30, 25, 55) # same API as above, except...
```

`RGB` is made via `NamedMap`, and `CMYK` is made via `FixedKeyNamedMap` (more details below).


### NamedMap

`NamedMap` is a `collections.abc.Mapping` version of `namedtuple`.

```python
>>> from namedmaps import NamedMap
>>> RGB = NamedMap('RGB', ['red', 'green', 'blue'])
>>> rgb = RGB(red='rouge', green='forest', blue='azul')
>>> print(rgb)
RGB(red='rouge', green='forest', blue='azul')
>>> rgb['red'] # access via bracket-notation
'rouge'
>>> rgb.green # access via dot-notation
'forest'
>>> rgb['grey']
KeyError: 'grey'
>>> rgb.gray
AttributeError: 'RGB' object has no attribute 'gray'
>>> rgb.blue = 'topaz' # NamedMaps are immutable
AttributeError: can't set attribute
```

### FixedKeyNamedMap

`FixedKeyNamedMap` is a bit more flexible by allowing edits to existing keys.

```python
>>> from namedmaps import FixedKeyNamedMap
>>> CMYK = FixedKeyNamedMap('CMYK', ['cyan', 'magenta', 'yellow', 'black'])
>>> cmyk = CMYK(255, 30, 25, 55) # same API as above, except...
>>> print(cymk)
CMYK(255, 30, 25, 55)
>>> cmyk.black += 45 # we can overwrite existing items
>>> print(cmyk)
CMYK(255, 30, 25, 100)
>>> cmyk['grey'] # cannot add new keys
KeyError: 'grey'
>>> cmyk.gray # cannot add new keys
AttributeError: 'CMYK' object has no attribute 'gray'
```
