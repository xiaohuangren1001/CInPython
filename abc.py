from abc import ABCMeta, abstractmethod
class CTypeBase(metaclass=ABCMeta):
    def __init__(self, value=None, proto_typ=object):
        self.value = value
        self.proto_type = proto_typ

    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError("This method is not implemented for the base; you should implement it by yourself.")

    @value.setter
    @abstractmethod
    def value(self, val):
        raise NotImplementedError("This method is not implemented for the base; you should implement it by yourself.")

    
