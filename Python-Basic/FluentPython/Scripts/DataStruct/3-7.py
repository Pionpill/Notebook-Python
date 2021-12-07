# 例3-7：将非字符串键转换为字符串
class StrKeyDict0(dict):            # 继承自 dict

    def __missing__(self,key):
        if isinstance(key,str):     # 如果找不到的键是字符串，抛出异常
            raise KeyError(key)
        return self[str(key)]       # 如果找不到的键不是字符串，转换成字符串再查找

    def get(self,key,default=None):
        ''' get 方法把查找工作用 self[key] 形式委托给 __getitem__,这样在查找失败后还能通过 __missing__ 再给键一个机会 '''
        try:
            return self[key]       
        except KeyError:
            return default          # 如果抛出 KeyError 说明 __missing__ 也失败了，返回 default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()    
        # contains 并不会调用 __getitem__，也就不会调用 __missing__ 因此要使用 or