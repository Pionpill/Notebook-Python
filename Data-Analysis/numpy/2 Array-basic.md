<link rel=stylesheet href=style.css>
<h1> 数组基础 </h1>
<h2> 1 NumPy 数组属性 </h2>
<h3> 1.1 NumPy 数组基础概念 </h3>
<h4> 数组维度与 ndarray 对象属性 </h4>

  - 数组维度
    - 在 NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）
    - axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第 1 轴进行操作，即对每一行进行操作。
  - 对象属性
    | 属性             | 说明                                                                                   |
    | ---------------- | -------------------------------------------------------------------------------------- |
    | ndarray.ndim     | 秩，即轴的数量或维度的数量                                                             |
    | ndarray.shape    | 数组的维度，对于矩阵，n 行 m 列                                                        |
    | ndarray.size     | 数组元素的总个数，相当于 .shape 中 n*m 的值                                            |
    | ndarray.dtype    | ndarray 对象的元素类型                                                                 |
    | ndarray.itemsize | ndarray 对象中每个元素的大小，以字节为单位                                             |
    | ndarray.flags    | ndarray 对象的内存信息                                                                 |
    | ndarray.real     | ndarray元素的实部                                                                      |
    | ndarray.imag     | ndarray 元素的虚部                                                                     |
    | ndarray.data     | 包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。 |

<h3> 1.2 NumPy 属性说明 </h3>
<h4> ndarray.ndim </h4>

  - 用于返回数组的维数，等于秩
    ```python
    a = np.array(24)
    print (a.ndim)     # 1
    b = a.reshape(2,4,3)
    print (b.ndim)     # 3
    ```

<h4> ndarray.shape </h4>

  - 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目
    ```python
    # 基础使用
    a = np.array([[1,2,3],[4,5,6]])  
    print (a.shape)    # (2,3) 
    # 调整维度
    a = np.array([[1,2,3],[4,5,6]]) 
    a.shape =  (3,2)  
    print (a)          # [[1 2] [3 4] [5 6]]
    # reshape 函数提供相似结果
    a = np.array([[1,2,3],[4,5,6]]) 
    b = a.reshape(3,2)  
    print (b)          # [[1,2],[3,4],[5,6]]
    ```
<h4> ndarray.itemsize </h4>

  - 以字节的形式返回数组中每一个元素的大小
    ```python 
    x = np.array([1,2,3,4,5], dtype = np.int8)  
    print (x.itemsize)      # 1
    y = np.array([1,2,3,4,5], dtype = np.float64)  
    print (y.itemsize)      # 8
    ```

<h4> ndarray.flags </h4>

  - ndarray.flags 返回 ndarray 对象的内存信息
    | 属性             | 描述                                                                   |
    | ---------------- | ---------------------------------------------------------------------- |
    | C_CONTIGUOUS (C) | 数据是在一个单一的C风格的连续段中                                      |
    | F_CONTIGUOUS (F) | 数据是在一个单一的Fortran风格的连续段中                                |
    | OWNDATA (O)      | 数组拥有它所使用的内存或从另一个对象中借用它                           |
    | WRITEABLE (W)    | 数据区域可以被写入，将该值设置为 False，则数据为只读                   |
    | ALIGNED (A)      | 数据和所有元素都适当地对齐到硬件上                                     |
    | UPDATEIFCOPY (U) | 这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新 |

<h2> 2 NumPy 创建数组 </h2>
<h3> 2.1 ndarray 构造器 </h3>
<h4> 使用 array 函数构建数组 </h4>

  - array 方法原型
    ```python
    numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
    ```
  - 详见第一节
<h3> 2.2 创建"空"数组的方法 </h3>
<h4> numpy.empty 方法 </h4>

  - np.empty 用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
    ```python
    numpy.empty(shape, dtype = float, order = 'C')
    ```
    - shape: 数组形状
    - dtype: 数据类型，可选
    - order: 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。

<h4> numpy.zeros </h4>

  - 创建指定大小的数组，数组元素以 0 来填充：
    ```python
    numpy.zeros(shape, dtype = float, order = 'C')
    ```

<h4> numpy.ones </h4>

  - 创建指定形状的数组，数组元素以 1 来填充：
    ```python
    numpy.ones(shape, dtype = None, order = 'C')
    ```

<h3> 2.3 从已有的数组创建数组 </h3>
<h4> numpy.asarray </h4>

  - numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个.
    ```python
    numpy.asarray(a, dtype = None, order = None)
    ```
    - a: 任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组

<h4> numpy.frombuffer </h4>

  - numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象。
    ```python
    numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
    ```
    - buffer	可以是任意对象，会以流的形式读入。
    - dtype	返回数组的数据类型，可选
    - count	读取的数据数量，默认为-1，读取所有数据。
    - offset	读取的起始位置，默认为 0。
    - buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b。
  - 例子
    ```python
    s =  b'Hello World' 
    a = np.frombuffer(s, dtype =  'S1')  
    print (a)    # [b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd']
    ```
<h4> numpy.fromiter </h4>

  - numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组
    ```python
    numpy.fromiter(iterable, dtype, count=-1)
    ```
    - iterable	可迭代对象

<h3> 2.4 从数值范围创建数组 </h3>
<h4> numpy.arange </h4>

  - 使用 arange 函数创建数值范围并返回 ndarray 对象
    ```python
    numpy.arange(start, stop, step, dtype)
    ```
<h4> numpy.linspace </h4>

  - numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的
    ```python
    np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    ```
    - stop: 序列的终止，如果 endpoint 为 true, 该值包含于数列中
    - num: 要生成的等步长的样本数量，默认值为 50
    - endpoint: true: 数列中包含 stop 值
    - retstep: True:生成的数组中会显示间距，反之不显示

<h4> numpy.logspace </h4>

  - np.logspace 用于创建一个等比数列
    ```python
    np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
    ```
    - base: 对数 log 的底数

<h2> 3 Numpy 切片和索引 </h2>
<h3> 3.1 切片 </h3>
<h4> slice 函数 </h4>

  - numpy 和 python 的 list 切片操作一样
  - 可以通过内置的 slice 函数操作
    ```python
    object.slice(start,stop,step)
    ```
    - 多维数组同样适用
  - 例子
    ```python
    a = np.arange(10)
    s = slice(2,7,2)  
    print (a[s])    # [2,4,6]
    ```
  - 切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同
    ```python
    a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
    print (a[...,1])   # 第2列元素
    print (a[1,...])   # 第2行元素
    print (a[...,1:])  # 第2列及剩下的所有元素
    ```

<h3> 3.2 索引 </h3>
<h4> 整数数组索引 </h4>

  - 数组索引可以获得对应多位索引下的元素
    ```python
    # 获得 (0,0) (1,1) (2,0) 处数组元素
    x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
    y = x[[0,1,2],  [0,1,0]]  
    print (y)     # [1  4  5]
    ```
  - 同样可以借助 :, ...与索引数组组合
    ```python
    a = np.array([[1,2,3], [4,5,6],[7,8,9]])
    b = a[1:3, 1:3]     # [[5 6][8,9]]
    c = a[1:3,[1,2]]    # [[5 6][8,9]]
    d = a[...,1:]       # [[2 3][5 6][8 9]]
    ```
<h4> 布尔索引 </h4>

  - 布尔索引通过布尔运算来获取符合指定条件的元素的数组
    ```python
    x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])   
    print (x[x >  5])   # [ 6  7  8  9 10 11]
    ```
  - 使用函数
    ```python
    a = np.array([np.nan,  1,2,np.nan,3,4,5])  
    print (a[~np.isnan(a)])  # [ 1.   2.   3.   4.   5.]
    ```

<h4> 花式索引 </h4>

  - 花式索引指的是利用整数数组进行索引。
  - 花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。
    ```python
    x=np.arange(32).reshape((8,4))
    print (x[[4,2,1,7]])
    # [[16 17 18 19] [ 8  9 10 11] [ 4  5  6  7] [28 29 30 31]]
    ```
  - 传入多个索引数组
    ```python
    x=np.arange(32).reshape((8,4))
    print (x[np.ix_([1,5,7,2],[0,3,1,2])])
    # [[ 4  7  5  6] [20 23 21 22] [28 31 29 30] [ 8 11  9 10]]
    ```