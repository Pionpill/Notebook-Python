# 例2-2：使用列表推导创建新列表
symbols = '$€￡$€￡'
codes = [ord(symbol) for symbol in symbols]

print(codes)
