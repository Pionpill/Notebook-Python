# 例7-1：装饰器将一个函数转换成另一个函数
def deco(func):     # 在函数中嵌套定义了函数
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target')


target()            # 调用被装饰的 target 其实会运行 inner。
# running inner()
print(target)       # 发现 terget 现在是 inner 的引用
# <function deco.<locals>.inner at 0x0000016889199A60>
