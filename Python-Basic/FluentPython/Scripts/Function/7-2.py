# 例7-2：装饰器的执行
registry = []   # 保留被修饰的函数的引用


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func  # 这里返回的与参数传入的一样，没有进行处理


@register
def f1():
    print('running f1')


@register
def f2():
    print('running f2')


def f3():
    print('running f3')


def main():
    print('running main')
    print('register ->', register)
    f1()
    f2()
    f3()


if __name__ == '__main__':  # 只有把该文件当作脚本时才调用 main()
    main()

# running register(<function f1 at 0x000002A1961EEF70>)
# running register(<function f2 at 0x000002A19620D040>)
# running main
# register -> <function register at 0x000002A1961EEEE0 >
# running f1
# running f2
# running f3
