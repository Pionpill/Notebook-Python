# 例7-9：高阶函数计算平均值
def make_averager():
    '''
    计算平均值，需要传一个新值
    '''
    series = []
    
    def averager(new_value):
        series.append(new_value)
        return sum(series)/len(series)
    
    return averager

avg = make_averager()
print(avg(10))          # 10
print(avg(12))          # 11
print(avg(14))          # 12