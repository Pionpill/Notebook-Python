# 例4-3：使用数组中的原始数据初始化 bytes 对象
import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)  # b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'
