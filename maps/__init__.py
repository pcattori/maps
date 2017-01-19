from maps.fixedkeymap import FixedKeyMap
from maps.frozenmap import FrozenMap
from maps.namedfixedkeymap import NamedFixedKeyMapMeta
from maps.namedfrozenmap import NamedFrozenMapMeta

def namedmap(typename, fields, mutable_values=False):
    if mutable_values:
        return NamedFixedKeyMapMeta(typename, fields)
    return NamedFrozenMapMeta(typename, fields)
