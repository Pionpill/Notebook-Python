# 例4-14：去掉全部组合记号的函数

import unicodedata
import string

def shave_marks(txt):
    """去掉重音符号"""
    norm_txt = unicodedata.normalize('NFD',txt) # 将所有字符分解基字符与组合记号
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))   # 过滤组合记号
    return unicodedata.normalize('NFC',shaved)  # 重组所有字符