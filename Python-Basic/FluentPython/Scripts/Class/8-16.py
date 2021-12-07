# 例8-16：del 语句
import weakref

s1 = {1,2,3}
s2 = s1

def bye():          # 这个函数一定不能是要销毁的对象的绑定方法，否则会有一个指向对象的引用
    print('Gone with the wind...')
    
ender = weakref.finalize(s1,bye)    # 在 s1 引用上注册 bye 回调
print(ender.alive)  # True: 在调用 finalize 对象之前，.alive 属性为 True

s2 = 'spam'         # Gone with the wind...: 此时 s2 重新绑定了一个对象，原来的对象被释放了
print(ender.alive)  # False 