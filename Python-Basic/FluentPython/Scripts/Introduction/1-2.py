# 例1-2：几个内置函数的理解
from math import hypot
import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):         # repr() 内置函数，以字符串形式表达，他和 str() 不同
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):          # abs() 内置函数
        return math.sqrt(self.x**2 + self.y**2)

    def __bool__(self):         # 判断是否为空时调用
        return bool(abs(self))

    def __add__(self, other):   # 加法运算
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):  # 数乘运算
        return Vector(self.x * scalar, self.y * scalar)
