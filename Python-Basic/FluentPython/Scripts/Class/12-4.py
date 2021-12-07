# 多继承的命名冲突
class A:
    def ping(self):
        print('ping:', self)
        
class B(A):
    def pong(self):
        print('pong:',self)
        
class C(A):
    def pong(self):
        print('PONG:',self)
        
class D(B, C):
    def ping(self):
        print('post-ping:',self)
        
    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)