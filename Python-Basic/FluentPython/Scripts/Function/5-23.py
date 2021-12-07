# 例5-23：使用 itemgetter 排序一个元组列表
from operator import itemgetter

metro_data = [
    ('Tokyo', 'JP', 36.9, (35.6, 139.69)),
    ('Delhi NCR', 'IN', 21.9, (28.6, 77.2)),
    ('Mexico City', 'MX', 20.1, (19.4, -99.1)),
    ('New York-Newark', 'US', 20.1, (40.8, -74.0)),
]

for city in sorted(metro_data,key = itemgetter(1)):
    print(city)
# ('Delhi NCR', 'IN', 21.9, (28.6, 77.2))
# ('Tokyo', 'JP', 36.9, (35.6, 139.69))
# ('Mexico City', 'MX', 20.1, (19.4, -99.1))
# ('New York-Newark', 'US', 20.1, (40.8, -74.0))