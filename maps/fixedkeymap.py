import collections
import collections.abc

class FixedKeyMap(collections.abc.MutableMapping):
    def __init__(self, *args, **kwargs):
        self._data = collections.OrderedDict(*args, **kwargs)

    def __getitem__(self, name):
        return self._data[name]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __delitem__(self, name):
        raise TypeError(
            f"'{self.__class__.__name__}' object does not support item deletion")

    def __setitem__(self, name, value):
        if name not in self._data:
            raise TypeError(
                f"'{self.__class__.__name__}' object does not support new item assignment")
        self._data[name] = value

