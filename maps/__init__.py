from maps.fixedkeymap import FixedKeyMap
from maps.frozenmap import FrozenMap
from maps.nameddict import NamedDict
from maps.namedfixedkeymap import NamedFixedKeyMapMeta
from maps.namedfrozenmap import NamedFrozenMapMeta

def namedfrozen(typename, fields):
    return NamedFrozenMapMeta(typename, fields)

def namedfixedkey(typename, fields):
    return NamedFixedKeyMapMeta(typename, fields)
