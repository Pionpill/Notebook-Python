# 例5-22：使用 reduce 和 operator.mul 计算阶乘
from functools import reduce
from operator import mul

def fact(n):
    return reduce(mul,range(1,n+1))