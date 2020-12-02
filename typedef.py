from .abc import *
class _DefType:
    '''
    The special type for typedef function.
    Only use in this module. Don't export it (although you can)
    '''
    def __init__(self, *, orig_type=type(None), name=''):
        self.orig_type = orig_type
        self.__name__ = name

    def __call__(self, val):
        return self.orig_type(val)

def typedef(orig_type, new_type_name):
    '''
    Define a new type as name as new_type_name.
    Although actually it is orig_type.
    If you use:
    >>> from carray import typedef, Int
    >>> Handle = typedef(Int, 'Handle')
    >>> Handle is Int
    False
    >>>
    But, when you use this:
    >>> from carray import typedef, Int
    >>> Handle = typedef(Int, 'Handle')
    >>> Handle(3)
    c-like int(3)
    >>> Int(3)
    c-like int(3)
    >>>
    
    '''
    return _DefType(orig_type=orig_type, name=new_type_name)
