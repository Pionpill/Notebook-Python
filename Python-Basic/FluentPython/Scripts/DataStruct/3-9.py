# 例3-9：字典只读实例 mappingproxy
from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)   # mappingproxy instance {1: 'A'}
# d_proxy[2] = 'x'              # Error：不能通过 d_proxy 修改
d[2] = 'B'                      # d_proxy 是动态的，可以通过 d 修改 d_proxy 视图
print(d_proxy)                  # mappingproxy instance {1: 'A', 2: 'B'}