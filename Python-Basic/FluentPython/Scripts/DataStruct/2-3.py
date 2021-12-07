# 例2-3：比较 filter/map 与 列表推导
symbols = '$€￡$€￡'

ascii1 = [ord(s) for s in symbols if ord(s) > 127]
ascii2 = list(filter(lambda c: c > 127, map(ord, symbols)))
