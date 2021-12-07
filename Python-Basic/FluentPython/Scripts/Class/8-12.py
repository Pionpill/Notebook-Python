# 例8-12：可变默认参数的危险
class HauntedBus:
    def __init__(self,passengers=[]) -> None:
        self.passengers = passengers    # 这个语句将 self.passengers 变成 passengers 的别名
        
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,name):
        self.passengers.remove(name)
        
# bus1 没什么问题
bus1 = HauntedBus(['Alice','Bill'])
print(bus1.passengers)      # ['Alice', 'Bill']
bus1.pick('David')
bus1.drop('Alice')
print(bus1.passengers)      # ['Bill', 'David']

# bus2 没什么问题，因为是第一次使用默认参数的构造函数
bus2 = HauntedBus()
bus2.pick('Alice')
print(bus2.passengers)      # ['Alice']

# bus3 出问题了，它再次使用了默认参数的构造函数
bus3 = HauntedBus()
print(bus3.passengers)      # ['Alice']