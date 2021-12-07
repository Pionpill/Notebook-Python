# 例2-9：具名元组
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', '36.9', (35.6, 139.6))
print(tokyo.name)      # 'JP'
print(tokyo[1])        # 'JP'