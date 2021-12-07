# 例2-23：双向队列
from collections import deque

dq = deque(range(10), maxlen=10)
dq.rotate(3)                        # 队列右移
dq.rotate(-4)                       # 队列左移
dq.appendleft(-1)                   # 队列头部插入-1，尾部最后一个元素删除
dq.extend([11, 22, 33])             # 尾部添加3个元素，头部删除三个元素
dq.extendleft([10, 20, 30, 40])     # 头部逐个添加4个元素
