# 例5-24：attrgetter 处理
from collections import namedtuple
from operator import attrgetter

metro_data = [
    ('Tokyo', 'JP', 36.9, (35.6, 139.69)),
    ('Delhi NCR', 'IN', 21.9, (28.6, 77.2)),
    ('Mexico City', 'MX', 20.1, (19.4, -99.1)),
    ('New York-Newark', 'US', 20.1, (40.8, -74.0)),
]

LatLong = namedtuple('Latlong','lat long')
Metropolis = namedtuple('Metropolis','name cc pop coord')
metro_areas = [Metropolis(name,cc,pop,LatLong(lat,long)) for name,cc,pop,(lat,long) in metro_data]

name_lat = attrgetter('name','coord.lat')
for city in sorted(metro_areas,key=attrgetter('coord.lat')):
    print(name_lat(city))
# ('Mexico City', 19.4)
# ('Delhi NCR', 28.6)
# ('Tokyo', 35.6)
# ('New York-Newark', 40.8)