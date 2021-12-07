# 例9-1：Vector2d 的多种表示形式
from array import array
import math

class Vector2d:
    typecode = 'd'
    
    def __init__(self,x,y) -> None:
        self.x = float(x)
        self.y = float(y)
        
    '''实现迭代，从而实现拆包'''
    def __iter__ (self):    
        return (i for i in (self.x,self.y))
    
    '''{!r} 获取各个分量的表示形式'''
    def __repr__(self) -> str:
        class_name = type(self).__name__    # type(self).__name__ 是类名，self.__name__　对象名
        return '{}({!r},{!r})'.format(class_name,*self)
    
    def __str__(self) -> str:
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode,self)))
    
    '''有个缺陷：其他可迭代对象也可进行比较'''
    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x , self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
v1 = Vector2d(3,4)
print(v1)                   # (3.0, 4.0): 调用了 __str__
x,y = v1        
print(x,y)                  # 3.4 4.0: 调用了 __iter__ 进行拆包
print(repr(v1))             # Vector2d(3.0,4.0)
v1_clone = eval(repr(v1))   # repr 函数调用 Vector2d 实例得到的是对构造方法的准确表述
print(v1 == v1_clone)       # True
print(bytes(v1))            # b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'
print(abs(v1))              # 5.0
print(bool(v1))             # True