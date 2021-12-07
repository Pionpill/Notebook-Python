# 例14-12：效果相同的生成器函数
def aritprog_gen(begin, step, end=None):
    result = type(begin+step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + index * step
