# 例9-7：私有的 Vector2d
class Vector2d:
    typecode = 'd'
    
    def __init__(self,x,y) -> None:
        self.__x = float(x)
        self.__y = float(y)
        
    @property       # 装饰器：读值方法
    def x(self):    # 读值方法与公开属性同名
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def __iter__(self):     # 读取公开特性而不是私有属性
        return (i for i in (self.x,self.y))
    
    def __hash__(self) -> int:
        return hash(self.x) ^ hash(self.y)
    