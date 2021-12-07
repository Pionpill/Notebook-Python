# 例8-18：WeakValueDictionary
import weakref

class Cheese:
    def __init__(self,kind) -> None:
        self.kind = kind
        
    def __repr__(self) -> str:
        return 'Cheese(%r)' % self.kind
    
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),Cheese('Brie'),Cheese('Parmesan')]

for cheese in catalog:      # 将奶酪的名称映射到 catalog 中 Cheese 实例的弱引用上
    stock[cheese.kind] = cheese
    
print(sorted(stock.keys())) # ['Brie', 'Parmesan', 'Red Leicester', 'Tilsit']
del catalog
print(sorted(stock.keys())) # ['Parmesan']:删除 catalog 后，大多数奶酪不见了，但不是所有
del cheese
print(sorted(stock.keys())) # []:因为 for 循环中的 cheese 也是全局变量，删掉就没事了