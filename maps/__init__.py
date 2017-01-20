from maps.fixedkeymap import FixedKeyMap
from maps.frozenmap import FrozenMap
from maps.nameddict import NamedDict
from maps.namedfixedkeymap import NamedFixedKeyMapMeta
from maps.namedfrozenmap import NamedFrozenMapMeta

def namedmap(typename, fields, fixed_keys=False):
    if fixed_keys:
        return NamedFixedKeyMapMeta(typename, fields)
    return NamedFrozenMapMeta(typename, fields)
