# 例14-4：Sentence 第2版
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    
    def __init__(self, text):
        self.words = RE_WORD.findall(text)
        self.text = text
        
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):     # 与上一版比，没有 __getitem__
        return SentenceIterator(self.words)     # 实例化并返回一个迭代器
    
class SentenceIterator:
    
    def __init__(self, words):
        self.words = words
        self.index = 0
        
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word
    
    def __iter__(self):
        return self