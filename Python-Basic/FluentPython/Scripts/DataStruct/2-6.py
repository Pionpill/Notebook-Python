# 例2-6：生成器表达式计算笛卡尔积
colors = ['white', 'black']
sizes = ['M', 'L', 'S']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
