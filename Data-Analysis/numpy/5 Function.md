<link rel=stylesheet href=style.css>
<h1> NumPy 函数 </h1>
<h2> 1 字符串函数 </h2>
<h3> 1.1 字符串函数基础 </h3>
<h4> 函数概述 </h4>

  - 用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作
  - 基于 Python 内置库中的标准字符串函数
  - 这些函数在字符数组类（numpy.char）中定义
    | 函数         | 描述                                       |
    | ------------ | ------------------------------------------ |
    | add()        | 对两个数组的逐个字符串元素进行连接         |
    | multiply()   | 返回按元素多重连接后的字符串               |
    | center()     | 居中字符串                                 |
    | capitalize() | 将字符串第一个字母转换为大写               |
    | title()      | 将字符串的每个单词的第一个字母转换为大写   |
    | lower()      | 数组元素转换为小写                         |
    | upper()      | 数组元素转换为大写                         |
    | split()      | 指定分隔符对字符串进行分割，并返回数组列表 |
    | splitlines() | 返回元素中的行列表，以换行符分割           |
    | strip()      | 移除元素开头或者结尾处的特定字符           |
    | join()       | 通过指定分隔符来连接数组中的元素           |
    | replace()    | 使用新字符串替换字符串中的所有子字符串     |
    | decode()     | 数组元素依次调用str.decode                 |
    | encode()     | 数组元素依次调用str.encode                 |

<h3> 1.2 常用字符串函数 </h3>
<h4> numpy.char.add() </h4>

  - 依次对两个数组的元素进行字符串连接
    ```python
    print (np.char.add(['hello'],[' xyz']))
    # ['hello xyz']
    print (np.char.add(['hello', 'hi'],[' abc', ' xyz']))
    # ['hello abc' 'hi xyz']
    ```

<h4> numpy.char.multiply() </h4>

  - 执行多重连接
    ```python
    print (np.char.multiply('Runoob ',3))
    # Runoob Runoob Runoob 
    ```

<h4> numpy.char.center() </h4>

  - 用于将字符串居中，并使用指定字符在左侧和右侧进行填充
    ```py
    print (np.char.center('Runoob', 20,fillchar = '*'))
    # *******Runoob*******
    ```

<h4> numpy.char.capitalize() </h4>

  - 将字符串的第一个字母转换为大写
    ```py
    print (np.char.capitalize('runoob'))
    # Runoob
    ```

<h4> numpy.char.title() </h4>

  - 将字符串的每个单词的第一个字母转换为大写
    ```python
    print (np.char.title('i like runoob'))
    # I Like Runoob
    ```

<h4> numpy.char.lower() </h4>

  - 对数组的每个元素转换为小写。它对每个元素调用 str.lower
    ```python
    print (np.char.lower(['RUNOOB','GOOGLE']))
    # ['runoob' 'google']
    ```

<h4> numpy.char.upper() </h4>

  - 对数组的每个元素转换为大写。它对每个元素调用 str.upper
    ```python
    print (np.char.upper(['runoob','google']))
    # ['RUNOOB' 'GOOGLE']
    ```

<h4> numpy.char.split() </h4>

  - 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格。
    ```python
    print (np.char.split ('www.runoob.com', sep = '.'))
    # ['www', 'runoob', 'com']
    ```

<h4> numpy.char.splitlines() </h4>

  - 以换行符 \n \r \r\n 作为分隔符来分割字符串，并返回数组
    ```py
    print (np.char.splitlines('i\nlike runoob?')) 
    # ['i', 'like runoob?']
    ```

<h4> numpy.char.strip() </h4>

  - 用于移除开头或结尾处的特定字符
    ```py
    print (np.char.strip(['arunooba','admin','java'],'a'))
    # ['runoob' 'dmin' 'jav']
    ```

<h4> numpy.char.join() </h4>

  - 通过指定分隔符来连接数组中的元素或字符串
    ```py
    print (np.char.join([':','-'],['runoob','google']))
    ```

<h4> numpy.char.replace() </h4>

  - 使用新字符串替换字符串中的所有子字符串
    ```py
    print (np.char.replace ('i like runoob', 'oo', 'cc'))
    ```

<h4> numpy.char.encode() </h4>

  - 对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器。
    ```py
    a = np.char.encode('runoob', 'cp500') 
    # b'\x99\xa4\x95\x96\x96\x82'
    ```

<h4> numpy.char.decode() </h4>

  - 对编码的元素进行 str.decode() 解码

<h2> 2 数学函数 </h2>
<h3> 2.1 三角函数 </h3>
<h4> 前置说明 </h4>

  - np.pi: &pi;
  - np.degrees(): 将弧度转换为角度

<h4> 三角函数 </h4>

  - np.sin()
  - np.cos()
  - np.tan()
  - np.arcsin()
  - np.arccos()
  - np.arctan()

<h3> 2.2 常用函数 </h3>
<h4> 舍入函数 numpy.around() </h4>

  - 返回指定数字的四舍五入值
    ```py
    numpy.around(a,decimals)
    ```
    - decimals: 舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
  - 举例
    ```py
    a = np.array([1.0,5.55,  123,  0.567,  25.532])
    print (np.around(a))
    # [  1. 6. 123. 1. 26.]
    print (np.around(a, decimals =  1))
    # [  1. 5.6 123.  0.6  25.5]
    print (np.around(a, decimals =  -1))
    # [  0. 10. 120.  0. 30.]
    ```

<h4> 取整函数 </h4>

  - 向下取整函数：返回小于或者等于指定表达式的最大整数，即向下取整
    ```py
    numpy.floor() 
    ```
  - 向上取整函数：返回大于或者等于指定表达式的最小整数，即向上取整
    ```py
    numpy.ceil()
    ```

<h2> 3 算术函数 </h2>
<h3> 3.1 四则运算 </h3>
<h4> 加减乘除 </h4>

  - 算术函数包含简单的加减乘除。和使用运算符原理一致
  - add(),subtract(),multiply(),divide()

<h3> 3.2 重要运算函数 </h3>
<h4> numpy.reciprocal() </h4>
  
  - 倒数运算

<h4> numpy.power() </h4>

  - 指数运算

<h4> numpy.mod() </h4>

  - 取余运算
  -  numpy.remainder() 也产生相同的结果

<h2> 4 NumPy 统计函数 </h2>
<h3> 4.1 常用统计函数 </h4>
<h4> numpy.amin() 和 numpy.amax() </h4>

  - 用于计算数组中元素沿指定轴的最大最小值
    ```py
    a = np.array([[3,7,5],[8,4,3],[2,4,9]])
    print (np.amin(a,1))    # [3 3 2]
    print (np.amin(a,0))    # [2 4 3]
    print (np.amax(a))      # 9
    print (np.amax(a, axis = 0)) # [8 7 9]
    ```

<h4> numpy.ptp() </h4>

  - 计算数组中元素最大值与最小值的差（最大值 - 最小值）
    ```py
    a = np.array([[3,7,5],[8,4,3],[2,4,9]])
    print (np.ptp(a))     # 7
    print (np.ptp(a, axis =  1))  # [4 5 7]
    print (np.ptp(a, axis =  0))  # [6 3 6]
    ```

<h4> numpy.percentile() </h4>

  - 小于这个值的观察值的百分比
    ```py
    numpy.percentile(a, q, axis)
    ```
    - a: 输入数组
    - q: 要计算的百分位数，在 0 ~ 100 之间
    - axis: 沿着它计算百分位数的轴
  - 举例
    ```py
    a = np.array([[10, 7, 4], [3, 2, 1]])
    print (np.percentile(a, 50)) # 3.5
    print (np.percentile(a, 50, axis=0)) 
    # [6.5 4.5 2.5]
    print (np.percentile(a, 50, axis=1)) 
    # [7. 2.]
    print (np.percentile(a, 50, axis=1, keepdims=True))
    # [[7.] [2.]]
    ```

<h4> numpy.median() </h4>

  - 用于计算数组 a 中元素的中位数（中值）
    ```py
    a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 
    print (np.median(a))    # 65.0
    print (np.median(a, axis =  0))   # [50. 90. 60.]
    print (np.median(a, axis =  1))   # [65. 80. 60.]
    ```

<h4> numpy.mean() </h4>

  - 返回数组中元素的算术平均值
    ```py
    a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
    print (np.mean(a))    # 3.6666666666666665
    print (np.mean(a, axis =  0))   # [2.66666667 3.66666667 4.66666667]
    print (np.mean(a, axis =  1))   # [2. 4. 5.]
    ```

<h4> numpy.average() </h4>

  - 根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
    ```py
    a = np.array([1,2,3,4])
    print (np.average(a))   # 2.5
    wts = np.array([4,3,2,1])  
    print (np.average(a,weights = wts))  # 2.0
    print (np.average([1,2,3,  4],weights =  [4,3,2,1], returned =  True))      # (2.0, 10.0) 返回权重和
    ```

<h4> numpy.std() </h4>

  - 标准差是一组数据平均值分散程度的一种度量
    ```py
    print (np.std([1,2,3,4]))   # 1.1180339887498949
    ```

<h4> numpy.var() </h4>

  - 每个样本值与全体样本值的平均数之差的平方值的平均数
    ```py
    print (np.var([1,2,3,4]))   # 1.25
    ```

<h2> 5 NumPy 排序、条件刷选函数 </h2>
<h3> 5.1 排序函数 </h3>
<h4> numpy.sort() </h4>

  - 函数原型
    ```py
    numpy.sort(a, axis, kind, order)
    ```
    - kind: 默认为'quicksort'（快速排序）
    - order: 如果数组包含字段，则是要排序的字段
  - 三种排序方式
    |   种类    | 速度  |   最坏情况   | 空间  | 稳定性 |
    | :-------: | :---: | :----------: | :---: | :----: |
    | quicksort |   1   |   $O(n^2)$   |   0   |   否   |
    | mergeorts |   2   | $O(n\log n)$ |  n/2  |   是   |
    | heapsort  |   3   | $O(n\log n)$ |   0   |   否   |
  - 举例
    ```py
    a = np.array([[3,7],[9,1]])
    print (np.sort(a))    # [[3 7] [1 9]]
    print (np.sort(a, axis =  0)) # [[3 1] [9 7]]
    dt = np.dtype([('name',  'S10'),('age',  int)]) 
    a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)  
    print (np.sort(a, order =  'name'))
    # [(b'amar', 27) (b'anil', 25) (b'raju', 21) (b'ravi', 17)]
    ```

<h4> numpy.argsort() </h4>

  - 返回的是数组值从小到大的索引值
    ```py
    x = np.array([3,  1,  2])  
    y = np.argsort(x)    
    print (y)            # [1 2 0]
    print (x[y])         # [1 2 3]
    for i in y:  
        print (x[i], end=" ")  # 1 2 3
    ```

<h4> numpy.lexsort() </h4>

  - 对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列
    ```py
    nm =  ('raju','anil','ravi','amar') 
    dv =  ('f.y.',  's.y.',  's.y.',  'f.y.') 
    ind = np.lexsort((dv,nm))  # [3 1 0 2]

<h4> msort、sort_complex、partition、argpartition </h4>

  - 其他常用排序函数
    | 函数                                      | 描述                                                 |
    | ----------------------------------------- | ---------------------------------------------------- |
    | msort(a)                                  | np.msort(a) 相等于 np.sort(a, axis=0)                |
    | sort_complex(a)                           | 对复数按照先实部后虚部的顺序进行排序                 |
    | partition(a, kth[, axis, kind, order])    | 指定一个数，对数组进行分区                           |
    | argpartition(a, kth[, axis, kind, order]) | 可以通过关键字 kind 指定算法沿着指定轴对数组进行分区 |

<h3> 5.2 条件筛选函数 </h3>
<h4> numpy.argmax() 和 numpy.argmin() </h4>

  - 分别沿给定轴返回最大和最小元素的索引
    ```py
    np.argmax(a, axis)
    ```

<h4> numpy.nonzero() </h4>

  - 返回输入数组中非零元素的索引
    ```py
    np.nonzero(a)
    ```

<h4> numpy.where() </h4>

  - 返回输入数组中满足给定条件的元素的索引
    ```py
    x = np.arange(9.).reshape(3, 3)
    y = np.where(x > 3)
    # (array([1, 1, 2, 2, 2]), array([1, 2, 0, 1, 2]))
    ```

<h4> numpy.extract() </h4>

  - 根据某个条件从数组中抽取元素，返回满条件的元素
    ```py
    x = np.arange(9.).reshape(3,3)
    condition = np.mod(x,2) == 0
    # [[ True False  True]
    # [False  True False]
    # [ True False  True]]
    print (np.extract(condition, x))
    # [0. 2. 4. 6. 8.]
    ```

<h2> 6 NumPy 线性代数库 </h2>
<h3> 6.1 线性代数函数 </h3>

> 三维及以上运算：[菜鸟](https://www.runoob.com/numpy/numpy-linear-algebra.html)

<h4> linalg 库 </h4>

  - NumPy 提供了线性代数函数库 linalg，该库包含了线性代数所需的所有功能
    | 函数        | 描述                     |
    | ----------- | ------------------------ |
    | dot         | 数组点积，即元素对应相乘 |
    | vdot        | 向量点积                 |
    | inner       | 数组内积                 |
    | matmul      | 数组的矩阵积             |
    | determinant | 数组的行列式             |
    | solve       | 求解线性矩阵方程         |
    | inv         | 计算矩阵的乘法逆矩阵     |

<h4> np.dot() </h4>

  - 一维数组：计算两个数组对应下表元素的乘积和
  - 二维数组：计算两个数组的矩阵乘积
  - 函数原型
    ```py
    np.dot(a,b,out=None)
    ```
    - out: 用来保存计算结果

<h4> np.vdot() </h4>

  - 两个向量的点积
    ```py
    a = np.array([[1,2],[3,4]]) 
    b = np.array([[11,12],[13,14]])
    print (np.vdot(a,b))    # 130
    ```

<h4> np.inner() </h4>

  - 一维数组的向量内积。对于更高的维度，它返回最后一个轴上的和的乘积。
    ```py
    print (np.inner(np.array([1,2,3]),np.array([0,1,0])))   # 2
    ```
    ```py
    a = np.array([[1,2], [3,4]]) 
    b = np.array([[11, 12], [13, 14]])
    print (np.inner(a,b))
    # [[35 41] [81 95]]
    # 1*11+2*12, 1*13+2*14 
    # 3*11+4*12, 3*13+4*14
    ```

<h4> numpy.matmul() </h4>

  - 回两个数组的矩阵乘积。 虽然它返回二维数组的正常乘积，但如果任一参数的维数大于2，则将其视为存在于最后两个索引的矩阵的栈，并进行相应广播
  - 如果任一参数是一维数组，则通过在其维度上附加 1 来将其提升为矩阵，并在乘法之后被去除。
    ```py
    a = [[1,0],[0,1]] 
    b = [1,2] 
    print (np.matmul(a,b))
    # [1 2]
    # [1 2]
    ```

<h4> np.linalg.det() </h4>

  - 函数计算输入矩阵的行列式
    ```py
    a = np.array([[1,2], [3,4]]) 
    # -2.0
    ```

<h4> np.linalg.solve() </h4>
  
  - 函数原型
    ```py
    numpy.linalg.solve(a, b)
    ```
    - a: 系数矩阵
    - b: 纵坐标或因变量的值
    - x: 方程组 ax=b 的解

<h4> np.linalg.inv() </h4>

  - 计算矩阵的乘法逆矩阵