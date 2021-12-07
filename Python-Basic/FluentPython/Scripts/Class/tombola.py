import abc

class Tombola(abc.ABC):     # 自定义抽象基类需要继承自 abc.ABC
    
    @abc.abstractmethod     # 抽象方法装饰器
    def load(self, iterable):
        """从可迭代对象中添加元素"""
        
    @abc.abstractclassmethod
    def pick(self):
        """随机删除元素，然后将其返回
        如果实例为空，这个方法应该抛出 'LookupError'
        """
    
    def loaded(self):       # 抽象基类可以包含具体方法
        """如果至少有一个元素，返回 'True', 否则返回 'False'"""
        return bool(self.inspect())     # 抽象基类中的具体方法只能依赖抽象基类定义的接口
    
    def inspect(self):
        """返回一个有序元组，由当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)    # 挑选完后，再用 .load 把元素放回去
        return tuple(sorted(items))    