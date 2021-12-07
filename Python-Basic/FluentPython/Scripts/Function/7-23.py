# 例7-23：为了接受参数，新的 register 装饰器必须作为函数调用
registry = set()    # 集合添加和删除函数的速度更快


def register(active=True):      # 接受一个可选参数
    def decorate(func):         # decorate 函数是真正的装饰器，它的参数是一个函数
        print('running register(active=%s) -> decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func             # 装饰器返回函数
    return decorate             # 装饰器工厂函数返回 decorate


@register(active=False)         # 工厂函数必须作为函数调用，并且传参
def f1():
    print('funning f1')


@register()                     # 即使不传参，也必须作为函数调用
def f2():
    print('running f2')
