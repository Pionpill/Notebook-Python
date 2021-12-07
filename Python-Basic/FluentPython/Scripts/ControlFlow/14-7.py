# 例14-7：第4版Sentence类
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    
    def __init__(self, text):
        self.text = text        # 这里不构建 words
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        # re.finditer 函数构建一个迭代器，包含 self.text 中匹配 RE_WORD 的单词，返回 MatchObject 实例
        for match in RE_WORD.finditer(self.text):
            yield match.group() # 从 MatchObject 实例中提取匹配正则表达式的具体文本