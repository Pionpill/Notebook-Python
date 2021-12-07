# 例14-1：Sentence 第一版
import re
import reprlib

RE_WORD = re.compile('\w+')     # 匹配 ASCII 组成的单词


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.finall(text)   # 满足正则表达式的全部非重复匹配

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence (%s)' % reprlib.repr(self.text)    # 限制长度，默认 30
