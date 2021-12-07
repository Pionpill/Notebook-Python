<link rel=stylesheet href=style.css>
<h1> NumPy 矩阵 </h1>
<h2> 1 矩阵库概念 </h2>
<h3> 1.1 矩阵库 </h3>
<h4> np.matlib </h4>

  - NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵

<h4> 矩阵转置 </h4>

  - numpy.transpose 函数来对换数组的维度
  - T 属性对换数组的维度

<h4> 矩阵与数组转换 </h4>

  - np.asarray(i): 转换为数组
  - np.asmatrix(i): 转换为矩阵

<h2> 2 矩阵库函数 </h2>
<h3> 2.1 构建矩阵函数 </h3>
<h4> matlib.empty() </h4>

  - 通过伪随机创建一个新的矩阵
    ```python
    numpy.matlib.empty(shape, dtype, order)
    ```
    - shape: 定义新矩阵形状的整数或整数元组
    - dtype: 可选，数据类型
    - order: C(行优先)，F(列优先)
  - 举例
    ```py
    import numpy.matlib 
    import numpy as np
    print (np.matlib.empty((2,2)))
    # [[-1.49166815e-154 -1.49166815e-154]
    # [ 2.17371491e-313  2.52720790e-212]]
    ```

<h4> matlib.zeros() </h4>

  - 创建一个以 0 填充的矩阵

<h4> matlib.ones() </h4>

  - 创建一个以 1 填充的矩阵

<h4> numpy.matlib.eye() </h4>

  - 返回一个矩阵，对角线元素为 1，其他位置为零
    ```python
    numpy.matlib.eye(n,M,k,dtype)
    ```
    - n: 返回矩阵的行数
    - M: 返回矩阵的列数，默认为 n
    - k: 对角线的索引
    - dtype: 数据类型
  - 举例
    ```python
    import numpy.matlib 
    import numpy as np 
    print (np.matlib.eye(n = 3, M = 4, k = 0, dtype = float))
    # [[1. 0. 0. 0.]
    # [0. 1. 0. 0.]
    # [0. 0. 1. 0.]]
    ```

<h4> matlib.identity() </h4>

  - 返回给定大小的单位矩阵
    ```py
    import numpy.matlib 
    import numpy as np 
    print (np.matlib.identity(2, dtype = float))
    # [[1. 0.]
    # [0. 1.]]
    ```

<h4> matlib.rand() </h4>

  - 创建一个给定大小的矩阵，数据随机填充，范围在 0-1 之间
    ```py
    import numpy.matlib 
    import numpy as np 
    print (np.matlib.rand(3,3))
    # [[0.23966718 0.16147628 0.14162  ]
    # [0.28379085 0.59934741 0.62985825]
    # [0.99527238 0.11137883 0.41105367]]
    ```

<h4> np.matrix() </h4>

  - 通过 matrix() 的两种赋值方法
    ```python
    A1=np.matrix([[1,2,3],[4,5,6],[7,8,9]])     #方法1
    A1=np.matrix('1 2 3;4 5 6;7 8 9')           #方法2
    ```