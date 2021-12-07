# 例2-18：bisect 函数的一个应用
import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grade='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grade[i]


for score in [33, 99, 77, 70, 89, 90, 100]:
    print(grade(score))
