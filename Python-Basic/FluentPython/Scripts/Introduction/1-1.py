# 例1-1：几个内置函数的理解
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):  # 内置函数 len()
        return len(self._cards)

    def __getitem__(self, position):    # 内置迭代器
        return self._cards[position]
