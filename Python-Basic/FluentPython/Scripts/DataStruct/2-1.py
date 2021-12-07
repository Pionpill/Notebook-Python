# 例2-1：使用 for 循环建立新列表
symbols = '$€￡$€￡'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)
