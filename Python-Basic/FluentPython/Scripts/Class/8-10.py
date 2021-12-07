# 例8-10：deepcopy 处理循环引用
from copy import deepcopy

a = [10,20]
b = [a,30]
a.append(b)
print(a)    # [10, 20, [[...], 30]]
c = deepcopy(a)
print(c)    # [10, 20, [[...], 30]]