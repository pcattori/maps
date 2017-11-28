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
