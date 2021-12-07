# 例5-2：函数名参数传递
def factorial(n):
    """return n!"""
    return n if n<2 else n * factorial(n-1)

fact = factorial
print(fact(5))                          # 120
print(list(map(factorial,range(11))))   # [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
