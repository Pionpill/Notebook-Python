# 例5-9：列出常规对象没有而函数有的属性
class C: pass
def func(): pass
obj = C()
print(sorted(set(dir(func)) - set(dir(obj))))
# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']