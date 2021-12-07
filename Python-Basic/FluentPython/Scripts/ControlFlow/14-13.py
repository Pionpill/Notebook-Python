# 例14-13：有穷等差数列
import itertools


def aritprog_gen(begin, step, end):
    first = type(begin+step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen
