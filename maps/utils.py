import keyword

def _validate_name(name):
    if not all(c.isalnum() or c == '_' for c in name):
        raise ValueError((
            'Type names and field names can only contain'
            f' alphanumeric characters and underscores: {name!r}'))
    if keyword.iskeyword(name):
        raise ValueError(
            f'Type names and field names cannot be a keyword: {name!r}')
    if name[0].isdigit():
        raise ValueError((
            'Type names and field names cannot start with a number:'
            f' {name!r}'))

def _validate_fields(fields):
    seen_names = set()
    for name in fields:
        if name.startswith('_'):
            raise ValueError(
                f'Field names cannot start with an underscore: {name!r}')
        if name in seen_names:
            raise ValueError(f'Encountered duplicate field name: {name!r}')
        seen_names.add(name)
