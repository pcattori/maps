# nameddict

https://github.com/tonnydourado/nameddict

Note: `namedtuple` uses leading `_` to namespace between attrs and items. `nameddict` should do the same

## API

```python
Stats = nameddict('Stats', ['attack', 'defense', 'special', 'speed', 'hp'])
# TODO do default args make sense? maybe not since providing a custom __init__ is hairy
stats = Stats(attack=10, defense=10, special=5, speed=4, hp=3)
stats.attack # => 10
stats['attack'] # => 10
stats.new # => KeyError
# TODO immutability?
stats.new = 'blah'
stats.hp += 5

Stats = nameddict('Stats', [...], immutable=True)
```
