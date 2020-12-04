class _Struct:
    def __init__(self, name, fields):
        self.__name__ = name
        self._fields = fields

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self._fields:
                raise AttributeError("Unexpected attribute: %s" % key)
            setattr(self, key, value)
        return self

def Struct(name, fields):
    return _Struct(name, fields)

