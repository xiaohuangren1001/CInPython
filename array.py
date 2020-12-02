from .abc import CTypeBase
class Array:
    def __init__(self, *args, type):
        from builtins import type as _type
        self.size = len(args)
        self.type = type
        self.data = list(args)
        if issubclass(type, CTypeBase):
            self.isc = True
        else:
            self.isc = False
        for i in self.data:
            if _type(i) != self.type:
                raise TypeError("Type mismatch: %s != %s" % (_type(i).__name__, self.type.__name__))

    @property
    def length(self):
        return self.size

    def __getitem__(self, ind):
        return self.data[ind]

    def __setitem__(self, ind, val):
        if self.size > ind:
            if type(val) != self.type:
                raise TypeError("Type mismatch: %s != %s" % (_type(i).__name__, self.type.__name__))
            self.data[ind] = val
        else:
            raise TypeError("Index out of range")

    def __delitem__(self, ind):
        if self.isc:
            raise TypeError("C array did not support deleting")
        elif self.size > ind:
            del self.data[ind]
        else:
            raise TypeError("Index out of range")
    
