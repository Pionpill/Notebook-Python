# 例5-21：使用 reduce 和匿名函数计算阶乘
from functools import reduce

def fact(n):
    return reduce(lambda x,y:x*y , range(1,n+1))