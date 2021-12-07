# 示例15-5：改进后的使用 @contextmanager 编写的 LookingGlass 类
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
        
    sys.stdout.write = reverse_write
    msg = ''    # 用于保存错误信息
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)