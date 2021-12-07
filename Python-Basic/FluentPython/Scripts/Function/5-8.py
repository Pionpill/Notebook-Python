# 例5-8：调用 BingoCage 实例，从打乱的列表中取出一个元素
import random

class BingoCage:
    def __init__(self,items) -> None:
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):     # bingo.pick() 的快捷方式是 bingo()
        return self.pick()

bingo = BingoCage(range(3))
print(bingo())              # 2