# 例12-1：内置类型子类化
class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key,[value] * 2)
        
dd = DoppelDict(one = 1)    # {'one': 1}
dd['two'] = 2               # {'one': 1, 'two': [2, 2]}
dd.update(three = 3)        # {'one': 1, 'two': [2, 2], 'three': 3}