from array import array
import reprlib
import math

class Vector:
    typecode = 'd'
    
    def __init__(self,components):
        self._components = array(self.typecode,components)  # 受保护的属性
        
    def __iter__(self):                             
        return iter(self._components)       # iter 会在下面的章节讲解
    
    def __repr__(self):
        components = reprlib.repr(self._components)     # reprlib.repr() 获取有限长度表示形式
        components = components[components.find('['):-1]    # 去掉前面的 array('d')[ 和后面的 ]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes(self):
        return (bytes[ord(self.typecode)]) + bytes(self._components)
    
    def __eq__(self,other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
    
    def __bool__(self):
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)