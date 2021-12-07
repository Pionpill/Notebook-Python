# 例3-5：defaultdict 的使用
import collections

bag = ['apple','banana','peach','watermelon','apple','banana','apple']
count = collections.defaultdict(int)    # int() 生成 0
for fruit in bag:
    count[fruit] += 1
# defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'peach': 1, 'watermelon': 1})