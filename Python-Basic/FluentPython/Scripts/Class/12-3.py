# 例12-3：继承自 UserDict 的字典子类
import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)
        
dd = DoppelDict2(one = 1)   # {'one': [1, 1]}
dd['two'] = 2               # {'one': [1, 1], 'two': [2, 2]}
dd.update(three = 3)        # {'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}