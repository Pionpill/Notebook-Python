# 例11-17：Sized 类部分源码
from abc import ABCMeta, abstractmethod

class Sized(metaclass = ABCMeta):
    
    __slots__ = ()
    
    @abstractmethod
    def __len__(self):
        return 0
    
    @classmethod
    def __subclasshook__(cls,C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True     # 如果超类有 __len__ 返回 True
        return NotImplemented   # 否则，返回 NotImplemented 让子类检查