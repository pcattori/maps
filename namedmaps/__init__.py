from namedmaps.fixedkeymap import FixedKeyMap
from namedmaps.fixedkeynamedmap import FixedKeyNamedMap
from namedmaps.namedmap import NamedMap

def namedmap(typename, fields, mutable_values=False):
    if mutable_values:
        return FixedKeyNamedMap(typename, fields)
    return NamedMap(typename, fields)
