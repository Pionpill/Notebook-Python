# 例2-4：列表推导笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts1 = [(color, size) for color in colors for size in sizes]  # 先颜色后尺码
tshirts2 = [(color, size) for size in sizes for color in colors]  # 先尺码后颜色
