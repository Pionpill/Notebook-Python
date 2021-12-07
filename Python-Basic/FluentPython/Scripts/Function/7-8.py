# 例7-8：计算移动平均值的类
class Averager():
    
    def __init__(self) -> None:
        self.series = []
        
    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series)/len(self.series)
    
avg = Averager()
    
print(avg(10))      # 10
print(avg(12))      # 11
print(avg(14))      # 12