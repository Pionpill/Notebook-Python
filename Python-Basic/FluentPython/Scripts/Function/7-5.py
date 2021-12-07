# 例7-5：global 关键字
b = 6
def f3(a):
    global b
    print(a)
    print(b)
    b = 100
    
f3(10)      # 10  6
print(b)    # 100