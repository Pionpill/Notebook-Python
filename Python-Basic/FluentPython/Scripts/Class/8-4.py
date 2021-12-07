# 例8-3：两个相同数据类型的变量
charles = {'name':'Charles L. Dragon','born':1832}
alex = {'name':'Charles L. Dragon','born':1832}

print(charles == alex)  # True: 内部数据一样
print(charles is alex)  # False: 不是相同对象，所指的内存空间不一样
print(id(charles))      # 1391934254840
print(id(alex))         # 1391934254840