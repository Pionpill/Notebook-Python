<link rel=stylesheet href=style.css>
<h1> Numpy 基础知识 </h1>
<h2> 1 Ndarray 对象 </h2>
<h3> 1.1 ndarray 数组对象概念 </h3>
<h4> ndarray 作用 </h4>

  - 存放同类型元素的多维数组
  - 每个元素拥有相同的内存大小

<h4> ndarray 组成 </h4>

  - 指向数据的指针
  - 数据类型或 dtype
  - 一个表示数组形状 (shape) 的元组
  - 一个跨度元组 (stride) ,其中整数指的是为了前进到当前维度下一个元素需要跨过的字节数

<h3> 1.2 ndarray 数组对象创建 </h3>
<h4> 方法原型及参数说明 </h4>

  - array 方法原型
    ```python
    numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
    ```
  - 参数说明
    |  名称  |               描述               |  可选   |
    | :----: | :------------------------------: | :-----: |
    | object |         数组或嵌套的数列         |         |
    | dtype  |        数组元素的数据类型        | &radic; |
    |  copy  |           对象是否复制           | &radic; |
    | order  |  C:行方向 F:列方向 A:任意(默认)  | &radic; |
    | subok  | 默认但会一个与基类类型一致的数组 | &radic; |
    | ndmin  |      指定生成数组的最小维度      | &radic; |

<h4> 实例 </h4>

  - import numpy as np
    ```python
    a = np.array([1,2,3])
    print(a)                # [1 2 3]
    b = np.array([[1,2],[3,4]])
    print(b)                # [[1 2 ][3 4]]
    c = np.array([1,2,3,4,5], ndmin = 2)
    print(c)                # [[1,2,3,4,5]]
    d = np.array([1,2,3], dtype = complex)
    print(d)                # [1.+0.j 2.+0.j 3.+0.j]
    ```

<h2> 2 NumPy 数据类型 </h2>
<h3> 2.1 数据类型 </h3>

  - 常用基本数据类型
    |    名称    |             描述             |           说明            |
    | :--------: | :--------------------------: | :-----------------------: |
    |   bool_    |      布尔值(True/False)      |                           |
    |    int_    |         默认整数类型         | 类似于C的long,int32,int64 |
    |    intc    |       与 C 的 int 一致       |                           |
    |    intp    |      用于索引的整数类型      |                           |
    |  int(num)  |       指定位数的整型数       |  int8,int16,int32,int64   |
    | uint(num)  |    指定位数的无符号整型数    |  int8,int16,int32,int64   |
    |   float_   |      float64 类的的缩写      |
    | float(num) |       指定位数的整型数       |  float16,float32,float64  |
    |  complex_  | complex的默认类型 complex128 |                           |
    | complex64  | 双32位浮点数(实数和虚数部分) |
    | complex128 | 双64位浮点数(实数和虚数部分) |

<h3> 2.2 数据类型对象 </h3>

> 详细说明与例子 [runoob](https://www.runoob.com/numpy/numpy-dtype.html)
<h4> np.dtype </h4>

  - 数据类型对象（numpy.dtype 类的实例）用来描述与数组对应的内存区域是如何使用，它描述了数据的以下几个方面：
    - 数据的类型（整数，浮点数或者 Python 对象）
    - 数据的大小（例如， 整数使用多少个字节存储）
    - 数据的字节顺序（小端法或大端法）
      - 字节顺序是通过对数据类型预先设定 < 或 > 来决定的。 < 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。> 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)。
    - 在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分
    - 如果数据类型是子数组，那么它的形状和数据类型是什么。

<h4> dtype 对象语法构造 </h4>

  - 语法格式
    ```python
    numpy.dtype(object,align,copy)
    ```
    - object: 要转换为的数据类型对象
    - align: 如果为 true，填充字段使其类似 C 的结构体
    - copy: 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用
  - 例子
    ```python
    import numpy as np
    student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
    a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
    print(a)    # [('abc', 21, 50.0), ('xyz', 18, 75.0)]
    ```
    - 定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
  - 内建类型字符代码
    | 字符 | 对应类型            | 说明                                          |
    | ---- | ------------------- | --------------------------------------------- |
    | b    | 布尔                |                                               |
    | i    | (有符号)整型        | i1,i2,i4,i8 分别代表 int8, int16, int32,int64 |
    | u    | (无符号)整型        |
    | f    | 浮点型              |
    | c    | 负数浮点型          |
    | m    | timedelta(时间间隔) |
    | M    | datetime(日期时间)  |
    | O    | (Python)对象        |
    | S,a  | (byte-)字符串       |
    | U    | Unicode             |
    | V    | 原始数据(void)      |

<h2> 3 NumPy 位运算 </h2>
<h3> 3.1 位运算函数 </h3>

  - 基本位运算函数
    | 函数        | 操作符 | 描述   |
    | ----------- | ------ | ------ |
    | bitwise_and | &      | 与操作 |
    | bitwise_or  | \|     | 或操作 |
    | invert      | ~      | 取反   |
    | left_shift  |        | 左移   |
    | right_shift |        | 右移   |

<h2> 4 NumPy 字节交换 </h2>
<h3> 4.1 字节顺序 </h3>
<h4> 大端模式 </h4>

  - 数据的高字节保存在内存的低地址中，而数据的低字节保存在内存的高地址中
  - 这样的存储模式有点儿类似于把数据当作字符串顺序处理：地址由小向大增加
  - 而数据从高位往低位放；和我们的阅读习惯一致。

<h4> 小端模式 </h4>

  - 数据的高字节保存在内存的高地址中，而数据的低字节保存在内存的低地址中
  - 这种存储模式将地址的高低和数据位权有效地结合起来，高地址部分权值高，低地址部分权值低。

<h3> 4.2 端转换 </h3>
<h4> np.ndarray.byteswap() </h4>

  - 函数将 ndarray 中每个元素中的字节进行大小端转换
    ```py
    a = np.array([1,  256,  8755], dtype = np.int16)
    print (map(hex,a))        # <map object at 0x104acb400>
    print (a.byteswap(True))  # [256 1 13090]
    print (map(hex,a))        # <map object at 0x104acb3c8>
    ```

<h2> 5 Numpy 副本和视图 </h2>
<h3> 5.1 副本与视图概念 </h3>
<h4> 副本与视图定义 </h4>

  - 副本是一个数据的完整的拷贝，物理内存在不同位置
  - 视图是数据的一个别称或引用，物理内存在同一位置

<h4> 副本与视图发生 </h4>

  - 视图一般发生在
    - numpy 的切片操作返回原数据的视图
      - 这点与 python 原生语法相反
    - 调用 ndarray 的 view() 函数产生一个视图
  - 副本一般发生在
    - Python 序列的切片操作，调用deepCopy()函数
    - 调用 ndarray 的 copy() 函数产生一个副本

<h4> 无复制 </h4>

  - 简单的赋值不会创建数组对象的副本
    ```python
    a = np.arange(6)  
    print (id(a))   # 4349302224
    b = a 
    print (id(b))   # 4349302224
    print (b)       # [[0 1][2 3][4 5]]
    print (a)       # [[0 1][2 3][4 5]]
    ```

<h3> 5.2 视图或浅拷贝 </h3>
<h4> ndarray.view() </h4>

  - 创建一个新的数组对象，该方法创建的新数组的维数更改不会更改原始数据的维数
    ```python
    a = np.arange(6).reshape(3,2)  
    b = a.view()  
    print (id(a))   # 4314786992
    print (id(b))   # 4315171296
    ```

<h4> 切片 </h4>

  - 使用切片创建视图修改数据会影响到原始数组
    ```python
    arr = np.arange(12)
    print (arr)     # [0 1 2 3 4 5 6 7 8 9 10 11]
    a=arr[3:]
    b=arr[3:]
    a[1]=123
    b[2]=234
    print(arr)      # [0 1 2 3 123 234 6 7 8 9 10 11]
    ```

<h3> 5.3 副本或深拷贝 </h3>
<h4> ndarray.copy() </h4>

  - 创建一个副本,对副本数据进行修改,不会影响到原始数据