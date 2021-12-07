# 例8-8：深复制
import copy

class Bus:
    '''汽车类，可以转载乘客'''
    def __init__(self,passengers=None) -> None:
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
            
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,name):
        self.passengers.remove(name)
        
bus1 = Bus(['Alice','Bill','Claire','David'])
bus2 = copy.copy(bus1)                  # bus2 是 bus1 的浅复制
bus3 = copy.deepcopy(bus1)              # bus3 是 bus1 的深复制
print(id(bus1),id(bus2),id(bus3))       # 1391927464840 1391927489288 1391927490504
bus1.drop('Bill')
print(bus2.passengers)                  # ['Alice', 'Claire', 'David']
for bus in [bus1,bus2,bus3]:            # bus1 bus2 实际上共享一个列表对象
    print(id(bus.passengers),end=' ')   # 1391967343432 1391967343432 1391927554568
    print()
print(bus3.passengers)                  # ['Alice', 'Bill', 'Claire', 'David']