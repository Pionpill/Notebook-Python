# 例7-25：参数化 clock 装饰器
import time

DEFAULT_FORMAT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FORMAT):      # clock 是参数化装饰器的工厂函数
    def decorate(func):             # decorate 是真正的装饰器
        def clocked(*_args):        # 包装被修饰的函数
            t0 = time.time()
            _result = func(*_args)  # 被修饰的函数返回的真正的结果
            elapsed = time.time() - t0
            name = func.__name__
            args = ','.join(repr(arg) for arg in _args)  # args 是用于显示的字符串
            result = repr(_result)
            # 这里的 **local() 是为了在 fmt 中引用 clocked 的局部变量
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


@clock()
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(.123)
# [0.12497544s] snooze(0.123) -> None
# [0.13129973s] snooze(0.123) -> None
# [0.13858795s] snooze(0.123) -> None
