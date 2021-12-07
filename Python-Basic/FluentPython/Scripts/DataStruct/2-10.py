# 例2-10 具名元组的属性和方法
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
print(City._fields)     # ("name","country","population","coordinates")

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', '21.9', LatLong(28.6, 77.2))
delhi = City._make(delhi_data)
for key, value in delhi._asdict().items():
    print(key+':', value)
