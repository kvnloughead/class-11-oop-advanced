import copy

class OrderedDict:

    def __init__(self):
        self._keys = []
        self._values = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        return list(zip(self._keys, self._values))

    def __len__(self):
        return len(self._keys)

    def __iter__(self):
        return zip(self._keys, self._values)

    def __setitem__(self, key, value):
        if key in self._keys:
            # update existing key with value
            self._values[self._keys.index(key)] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __getitem__(self, key):
        for k, v in self.items():
            if k == key:
                return v
        raise KeyError(key)

    def __contains__(self, key):
        return key in self._keys

    def __delitem__(self, key):
        if key not in self._keys:
            raise KeyError("Key not found.")
        del self._values[self._keys.index(key)]
        self._keys.remove(key)

    def __eq__(self, other):
        #return set(self.items()) == set(other.items())
        for i, item in enumerate(self.items()):
            if item != list(other.items())[i]:
                return False
        return True

    def __str__(self):
        if not self._keys:
            return "{}"
        s = "{"
        for k, v in self.items():
            s += "{}: {}, ".format(repr(k), repr(v))
        return s[:-2    ] + "}"

    __repr__ = __str__

    def __add__(self, other):
        new = copy.copy(self)
        for key, val in other.items():
            new[key] = val
        return new

    @classmethod
    def from_keys(cls, iter):
        d = OrderedDict()
        for k in iter:
            d._keys.append(k)
            d._values.append(None)
        return d


if __name__ == '__main__':
    def testing():
        d1 = OrderedDict()
        d1['a'] = 1
        d1['b'] = 2

        print(d1)

        d2 = {'a':1, 'b':2}
        print(d2)

        print(d1 == d2)
        print(d1['c'])

    testing()
