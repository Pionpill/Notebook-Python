# 例15-3：LookingGlass 类
class LookingGlass:
    
    def __enter__(self):    # enter 方法只传入 self
        import sys
        self.original_write = sys.stdout.write  # 将原来的输出保存
        sys.stdout.write = self.reverse_write   # 打猴子补丁，替换成自编写的方法
        return 'JABBERWOCKY'    # 返回值
    
    def reverse_write(self, text):
        self.original_write(text[::-1])
        
    # 如果一切正常，传入的参数是 None, None, None; 否则返回对应异常
    def __exit__(self, exc_type, exc_value, traceback): 
        import sys      # 重复导入模块不会消耗很多的资源，因为 Python 会缓存导入的模块
        sys.stdout.write = self.original_write  # 还原成原来的 sys.stdout.write
        if exc_type is ZeroDivisionError:   # 若有异常，打印一个消息
            print('Please DO NOT divide by zero!')  
            return True # 返回 True 告诉编译器已经处理了，否则，向上冒泡告诉编译器
        