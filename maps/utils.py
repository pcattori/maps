import collections
import keyword

def _validate_name(name):
    if not all(c.isalnum() or c == '_' for c in name):
        raise ValueError((
            'Type names and field names can only contain'
            ' alphanumeric characters and underscores: {!r}'.format(name)))
    if keyword.iskeyword(name):
        raise ValueError(
            'Type names and field names cannot be a keyword: {!r}'.format(name))
    if name[0].isdigit():
        raise ValueError((
            'Type names and field names cannot start with a number:'
            ' {!r}'.format(name)))

def _validate_fields(fields):
    seen_names = set()
    for name in fields:
        if name.startswith('_'):
            raise ValueError(
                'Field names cannot start with an underscore: {!r}'.format(name))
        if name in seen_names:
            raise ValueError('Encountered duplicate field name: {!r}'.format(name))
        seen_names.add(name)

def _validate_defaults(fields, defaults):
    for arg in defaults:
        if arg not in fields:
            raise ValueError('Default argument does not correspond to any field: {!r}'.format(arg))

    for i, field in enumerate(fields):
        if field in defaults:
            for fieldAfterDefault in fields[i:]:
                if fieldAfterDefault not in defaults:
                    raise ValueError("non-default argument '{}' follows default argument '{}'".format(fieldAfterDefault, field))

def _recurse(obj, map_fn=None, list_fn=None, object_fn=None):
    if map_fn is None:
        map_fn = lambda x: x # pragma: no cover
    if list_fn is None:
        list_fn = lambda x: x
    if object_fn is None:
        object_fn = lambda x: x

    if isinstance(obj, (bool, int, float, complex, str)):
        return obj

    cls = type(obj)
    kwargs = dict(map_fn=map_fn, list_fn=list_fn, object_fn=object_fn)
    if isinstance(obj, collections.Mapping):
        return map_fn(**cls((k, _recurse(v, **kwargs)) for k,v in obj.items()))
    if isinstance(obj, (collections.Sequence, collections.Set)):
        return list_fn(cls(_recurse(v, **kwargs) for v in obj))
    return object_fn(obj) # pragma: no cover
