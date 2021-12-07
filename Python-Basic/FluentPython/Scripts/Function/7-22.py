# 例7-22：示例 7-2 的简化版
registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


print('running main()')
print('registry ->', registry)
f1()
