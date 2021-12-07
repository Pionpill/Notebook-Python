# 例2-5：用生成器表达式创建元组和数组
import array

symbols = '$€￡$€￡'
ascii = tuple(ord(symbol) for symbol in symbols)
sen = array.array('I', (ord(symbol) for symbol in symbols))
