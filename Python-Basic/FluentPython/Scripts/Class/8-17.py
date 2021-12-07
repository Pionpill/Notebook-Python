# 例8-17：弱引用
import weakref

a_set = {0,1}
wref = weakref.ref(a_set)   # 创建弱引用对象 wref，下一行审查它
print(wref)         # <weakref at 0x0000014415BF4E58; to 'set' at 0x0000014415C0A668>
print(wref())       # {0,1}: 调用 wref() 返回的是被引用的对象
a_set = {2,3,4}     # 将 a_set 绑定到新的对象
print(wref() is None)   # True: 对象不存在，弱引用返回 None