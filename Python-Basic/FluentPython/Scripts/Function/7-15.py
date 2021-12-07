# 例7-15：修饰器计算运行时间
import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)        # clocked 的闭包中包含自由变量 func
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed,name,arg_str,result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)
    
@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

snooze(.123)    
# [0.12331390s] snooze(0.123) -> None
factorial(5)
# [0.00000040s] factorial(1) -> 1
# [0.00020120s] factorial(2) -> 2
# [0.00039360s] factorial(3) -> 6
# [0.00056890s] factorial(4) -> 24
# [0.00074810s] factorial(5) -> 120