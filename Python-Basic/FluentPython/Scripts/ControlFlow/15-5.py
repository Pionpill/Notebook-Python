# 例15-5：使用 @contextmanager 编写的 LookingGlass 类
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
        
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY' # 产出一个值，这个值会绑定到 with 语句中的 as 子句的目标变量上。执行 with 模块时，函数将在这一点暂停
    sys.stdout.write = original_write