from .abc import *
class Int(CTypeBase):
    def __init__(self, value=0):
        self.proto_type = int
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, self.proto_type):
            val = self.proto_type(val)
        if val > 2147483647 or val < -2147483648:
            raise OverflowError("Overflow")
        self._value = val

    def __add__(self, other):
        self._type_check(other)
        val = self.value + other.value
        return Int(val)
    
    def __sub__(self, other):
        self._type_check(other)
        val = self.value - other.value
        return Int(val)

    def __mul__(self, other):
        self._type_check(other)
        val = self.value * other.value
        return Int(val)

    def __div__(self, other):
        self._type_check(other)
        val = int(self.value / other.value)
        return Int(val)

    def __pow__(self, other):
        self._type_check(other)
        val = pow(self.value, other.value)
        return Int(val)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return 'c-like int(' + str(self.value) + ')'

    def __eq__(self, other):
        self._type_check(other)
        return self.value == other.value

    def __lt__(self, other):
        self._type_check(other)
        return self.value < other.value

    __gt__ = lambda self, other: other < self
    __le__ = lambda self, other: self < other or self == other
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not (self == other)
    
    def _type_check(self, other):
        if not isinstance(other, CTypeBase):
            raise TypeError("Type mismatch: %s != %s" % (self.__class__.__name__, other.__class__.__name__))
        

class Float(CTypeBase):
    def __init__(self, value=0):
        self.proto_type = float
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, self.proto_type):
            val = self.proto_type(val)
        if val > 2**127 or val < -2**128:
            raise OverflowError("Overflow")
        self._value = val

    def _type_check(self, other):
        if not isinstance(other, CTypeBase):
            raise TypeError("Type mismatch: %s != %s" % (self.__class__.__name__, other.__class__.__name__))
        
    
    def __add__(self, other):
        self._type_check(other)
        val = self.value + other.value
        return Float(val)
    
    def __sub__(self, other):
        self._type_check(other)
        val = self.value - other.value
        return Float(val)

    def __mul__(self, other):
        self._type_check(other)
        val = self.value * other.value
        return Float(val)

    def __div__(self, other):
        self._type_check(other)
        val = self.value / other.value
        return Float(val)

    def __pow__(self, other):
        self._type_check(other)
        val = pow(self.value, other.value)
        return Float(val)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return 'c-like float(' + str(self.value) + ')'

    def __eq__(self, other):
        self._type_check(other)
        return self.value == other.value

    def __lt__(self, other):
        self._type_check(other)
        return self.value < other.value
    
    __gt__ = lambda self, other: other < self
    __le__ = lambda self, other: self < other or self == other
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not (self == other)

class LongInt(Int):
    def __repr__(self):
        return 'c-like long(' + str(self.value) + ')'
    
    def __add__(self, other):
        i = super().__add__(self, other)
        return LongInt(i.value)

    def __sub__(self, other):
        i = super().__sub__(self, other)
        return LongInt(i.value)

    def __mul__(self, other):
        i = super().__mul__(self, other)
        return LongInt(i.value)

    def __div__(self, other):
        i = super().__div__(self, other)
        return LongInt(i.value)

    def __pow__(self, other):
        i = super().__pow__(self, other)
        return LongInt(i.value)
        

Long = LongInt

class LongLong(CTypeBase):
    def __init__(self, value=0):
        self.proto_type = int
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, self.proto_type):
            val = self.proto_type(val)
        if val > 2**63-1 or val < -2**63:
            raise OverflowError("Overflow")
        self._value = val

    def _type_check(self, other):
        if not isinstance(other, CTypeBase):
            raise TypeError("Type mismatch: %s != %s" % (self.__class__.__name__, other.__class__.__name__))
        
    
    def __add__(self, other):
        self._type_check(other)
        val = self.value + other.value
        return LongLong(val)
   
    def __sub__(self, other):
        self._type_check(other)
        val = self.value - other.value
        return LongLong(val)

    def __mul__(self, other):
        self._type_check(other)
        val = self.value * other.value
        return LongLong(val)

    def __div__(self, other):
        self._type_check(other)
        val = int(self.value / other.value)
        return LongLong(val)

    def __pow__(self, other):
        self._type_check(other)
        val = pow(self.value, other.value)
        return LongLong(val)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return 'c-like long long(' + str(self.value) + ')'

    def __eq__(self, other):
        self._type_check(other)
        return self.value == other.value

    def __lt__(self, other):
        self._type_check(other)
        return self.value < other.value

    __gt__ = lambda self, other: other < self
    __le__ = lambda self, other: self < other or self == other
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not (self == other)

class Double(CTypeBase):
    def __init__(self, value=0):
        self.proto_type = int
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, self.proto_type):
            val = self.proto_type(val)
        if val > 2**1023-1 or val < -2**1023:
            raise OverflowError("Overflow")
        self._value = val

    def _type_check(self, other):
        if not isinstance(other, CTypeBase):
            raise TypeError("Type mismatch: %s != %s" % (self.__class__.__name__, other.__class__.__name__))
        
    
    def __add__(self, other):
        self._type_check(other)
        val = self.value + other.value
        return Double(val)
   
    def __sub__(self, other):
        self._type_check(other)
        val = self.value - other.value
        return Double(val)

    def __mul__(self, other):
        self._type_check(other)
        val = self.value * other.value
        return Double(val)

    def __div__(self, other):
        self._type_check(other)
        val = self.value / other.value
        return Double(val)

    def __pow__(self, other):
        self._type_check(other)
        val = pow(self.value, other.value)
        return Double(val)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return 'c-like double(' + str(self.value) + ')'

    def __eq__(self, other):
        self._type_check(other)
        return self.value == other.value

    def __lt__(self, other):
        self._type_check(other)
        return self.value < other.value

    __gt__ = lambda self, other: other < self
    __le__ = lambda self, other: self < other or self == other
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not (self == other)

class Short(CTypeBase):
    def __init__(self, value=0):
        self.proto_type = int
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, self.proto_type):
            val = self.proto_type(val)
        if val > 65535 or val < -65536:
            raise OverflowError("Overflow")
        self._value = val

    def _type_check(self, other):
        if not isinstance(other, CTypeBase):
            raise TypeError("Type mismatch: %s != %s" % (self.__class__.__name__, other.__class__.__name__))
        
    
    def __add__(self, other):
        self._type_check(other)
        val = self.value + other.value
        return Short(val)
   
    def __sub__(self, other):
        self._type_check(other)
        val = self.value - other.value
        return Short(val)

    def __mul__(self, other):
        self._type_check(other)
        val = self.value * other.value
        return Short(val)

    def __div__(self, other):
        self._type_check(other)
        val = int(self.value / other.value)
        return Short(val)

    def __pow__(self, other):
        self._type_check(other)
        val = pow(self.value, other.value)
        return Short(val)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return 'c-like short(' + str(self.value) + ')'

    def __eq__(self, other):
        self._type_check(other)
        return self.value == other.value

    def __lt__(self, other):
        self._type_check(other)
        return self.value < other.value

    __gt__ = lambda self, other: other < self
    __le__ = lambda self, other: self < other or self == other
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not (self == other)

class Char(CTypeBase):
    def __init__(self, value=0):
        self.proto_type = int
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            val = ord(val)
        if not isinstance(val, self.proto_type):
            val = self.proto_type(val)
        if val > 127 or val < -128:
            raise OverflowError("Overflow")
        self._value = val

    def _type_check(self, other):
        if not isinstance(other, CTypeBase):
            raise TypeError("Type mismatch: %s != %s" % (self.__class__.__name__, other.__class__.__name__))
        
    
    def __add__(self, other):
        self._type_check(other)
        val = self.value + other.value
        return Char(val)
   
    def __sub__(self, other):
        self._type_check(other)
        val = self.value - other.value
        return Char(val)

    def __mul__(self, other):
        self._type_check(other)
        val = self.value * other.value
        return Char(val)

    def __div__(self, other):
        self._type_check(other)
        val = int(self.value / other.value)
        return Char(val)

    def __pow__(self, other):
        self._type_check(other)
        val = pow(self.value, other.value)
        return Char(val)

    def __str__(self):
        return chr(self.value)

    def __repr__(self):
        return 'c-like char(' + chr(self.value) + ')'

    def __eq__(self, other):
        self._type_check(other)
        return self.value == other.value

    def __lt__(self, other):
        self._type_check(other)
        return self.value < other.value

    __gt__ = lambda self, other: other < self
    __le__ = lambda self, other: self < other or self == other
    __ge__ = lambda self, other: not (self < other)
    __ne__ = lambda self, other: not (self == other)
