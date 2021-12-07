# 例2-21：通过改变数组中一个字节来更新数组里某个元素值
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)              # array('h', [-2, -1, 0, 1, 2])：原始 numbers

memv = memoryview(numbers)
print(len(memv))            # 内存视图的基础操作
print(memv[0])

memv_oct = memv.cast('B')
# [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]：将机器码转换为整型后以列表形式输出
print(memv_oct.tolist())
memv_oct[5] = 4
# array('h', [-2, -1, 1024, 1, 2])：内存处机器码改变，numbers 也改变
print(numbers)
