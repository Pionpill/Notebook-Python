# 例9-4：比较 classmethod 和 staticmethod
class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    
    @staticmethod
    def statmeth(*args):
        return args
    
    def fun(*args):
        return args
    
# 不管怎样调用 klassmeth，它的第一个参数始终是 Demo 类
print(Demo.klassmeth())             # (<class '__main__.Demo'>,)
print(Demo.klassmeth('spam'))       # (<class '__main__.Demo'>, 'spam')
# statmeth 的行为与普通的函数相似
print(Demo.statmeth())              # ()
print(Demo.statmeth('spam'))        # ('spam',)
# 普通函数
print(Demo.fun())                   # ()
print(Demo.fun('spam'))             # ('spam',)