# 例5-15： 提取关于函数的信息
def clip(text,max_len=80):
    """在 max_len 前面或后面的第一个空格处截断文本"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ',0,max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ',max_len)
        if space_after >= 0:
            end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

print(clip.__defaults__)    # (80,)
print(clip.__code__)        
# <code object clip at 0x000002109AE7AAE0, file "<string>", line 2>
print(clip.__code__.co_varnames)    
# ('text', 'max_len', 'end', 'space_before', 'space_after')
print(clip.__code__.co_argcount)    # 2