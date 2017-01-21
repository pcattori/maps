import maps.utils as utils

class NamedDict(dict):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __repr__(self): # pragma: no cover
        return f'{type(self).__name__}({super().__repr__()})'
