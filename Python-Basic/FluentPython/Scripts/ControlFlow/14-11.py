# 例14-11：等差数列生成器
class ArithmeticProgression:

    def __init__(self, begin, stop, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> 无穷数列

    def __iter__(self):
        # 这一段将 self.begin 传给 result，不过会先强制转换成前面的加法算式得到的类型
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index  # 由于算术运算符会隐式转换数值类型，这里没有必要强制转换
