# 例2-8：嵌套元组获取经度
metro_areas = [
    ('Tokyo', 'JP', 36.9, (35.6, 139.69)),
    ('Delhi NCR', 'IN', 21.9, (28.6, 77.2)),
    ('Mexico City', 'MX', 20.1, (19.4, -99.1)),
    ('New York-Newark', 'US', 20.1, (40.8, -74.0)),
]

fmt = '{:15}|{:9.1f}|{:9.1f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
     if longitude <= 0:
         print(fmt.format(name,latitude,longitude))
