# 例 7-13：改进后的平均值函数(有缺陷)
def make_averager():
    total = 0
    count = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total/count

    return averager
