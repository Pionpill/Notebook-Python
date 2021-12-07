# 例8-15：接收可变参数的风险
class TwilightBus:
    def __init__(self,passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers    # 这个赋值语句将 self.passengers 变成 passengers 的别名
            
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,name):
        self.passengers.remove(name)
        
team = ['Alice','David','Mike']
bus = TwilightBus(team)
bus.drop('Alice')
print(team)     # ['David', 'Mike']