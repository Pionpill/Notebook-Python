# 例8-3：别名
charles = {'name':'Charles L. Dragon','born':1832}
lewis = charles
print(lewis == charles)     # True
print(id(lewis))            # 1391967345784
print(id(charles))          # 1391967345784 