# 例5-1：阶乘函数
def factorial(n):
    """return n!"""
    return n if n<2 else n * factorial(n-1)

print(factorial(10))        # 3628800
print(factorial.__doc__)    # return n!
print(type(factorial))      # <class 'function'>