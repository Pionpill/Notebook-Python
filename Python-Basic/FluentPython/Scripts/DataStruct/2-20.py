# 例2-20：数组使用
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
