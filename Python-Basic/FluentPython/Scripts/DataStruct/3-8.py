# 例3-8：继承自 UserDict 的映射类
import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return self(str(key))

    def __contains__(self, key):
        return str(key) in self.data    # data 中所有键均为 str

    def __setitem__(self, key, item):
        self.data[str(key)] = item      # 具体的实现委托给了 data 属性