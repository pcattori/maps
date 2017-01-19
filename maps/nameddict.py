import maps.utils as utils

class NamedDict(dict):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name):
        self[name] = value

