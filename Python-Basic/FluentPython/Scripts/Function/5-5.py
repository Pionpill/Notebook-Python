# 例5-5：map filter 与列表推导
def factorial(n):
    """return n!"""
    return n if n<2 else n * factorial(n-1)

fact = factorial

print(list(map(fact,range(6))))     # [0, 1, 2, 6, 24, 120]
print([fact(n) for n in range(6)])  # [0, 1, 2, 6, 24, 120]

print(list(map(fact,filter(lambda n:n % 2,range(6)))))    # [1, 6, 120]
print([fact(n) for n in range(6) if n % 2])               # [1, 6, 120]