# 例5-16：partial 函数的使用
from operator import mul
from functools import partial

triple = partial(mul,3)     # 使用 mul 创建 triple 函数，把第一个定位参数定为 3
triple(7)                   # 21
print(list(map(triple,range(10))))  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]