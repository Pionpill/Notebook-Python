# 例5-6：使用 reduce 和 sum 求和
from functools import reduce
from operator import add

print(reduce(add,range(99)))    # 4851
print(sum(range(99)))           # 4851