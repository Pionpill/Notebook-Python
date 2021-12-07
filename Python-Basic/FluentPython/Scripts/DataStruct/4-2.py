# 例4-2：bytes 和 bytearray 对象
cafe = bytes('café', encoding='utf_8')  # b'caf\xc3\xa9'
print(cafe[0])  # 99
print(cafe[:1])  # b'c', bytes 对象的切片还是 bytes 对象

cafe_arr = bytearray(cafe)
print(cafe_arr)  # bytearray(b'caf\xc3\xa9')
