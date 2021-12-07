# 例7-19：生成第 n 个斐波那契数列，lru 修饰改善
import functools
import time

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(','.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_lst.append(','.join(pairs))
        arg_str = ','.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed,name,arg_str,result))
        return result
    return clocked

@functools.lru_cache()  # 这里加括号的原因后文说明
@clock                  # 叠放了修饰器
def fibonacci(n):
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))