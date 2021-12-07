# 例8-11：函数传参
def f(a,b):
    a += b
    return a

x = 1
y = 2
print(f(x,y))   # 3
print(x,y)      # 1 2   值没有变

a = [1,2]
b = [3,4]
print(f(a,b))   # [1,2,3,4]
print(a,b)      # [1,2,3,4] [3,4]   列表变了

t = (1,2)
u = (3,4)
print(f(t,u))   # (1,2,3,4)
print(t,u)      # (1,2) (3,4)       元组没有变