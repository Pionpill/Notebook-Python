# 例4-1：编码与解码
s = 'cafe'
b = s.encode('utf8')    # 使用 utf-8 将 'cafe' 编码成 bytes 对象
b.decode('utf8')        # 使用 utf-8 将 bytes 对象解码成 str 对象
