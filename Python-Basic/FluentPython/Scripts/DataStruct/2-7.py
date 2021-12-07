# 例2-7：将元组作为记录
lax_coordinate = (33.19, -118.40)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s,%s' % passport)       # % 运算符匹配到对应元组变量上
for country, _ in traveler_ids:     # 第二个元素没什么用，用 _ 占位
    print(country)
