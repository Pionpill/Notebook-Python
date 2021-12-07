<link rel=stylesheet href=style.css>
<h1> 数组进阶 </h1>
<h2> 1 NumPy 广播 </h2>
<h3> 1.1 广播(Broadcast) </h3>
<h4> 广播的概念 </h4>

  - 广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。
    ```python
    a = np.array([[ 0, 0, 0],
            [10,10,10]])
    b = np.array([1,2,3])
    print(a + b)    # [[1,2,3] [11,12,13]]
    ```
  - 可以使用 np.title 方法扩展维度
    ```python
    b = np.array([1,2,3])
    bb = np.tile(b, (2, 1)) 
    print(bb)  # [[1,2,3],[1,2,3]]
    ```
<h4> 广播规则 </h4>

  - 让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
  - 输出数组的形状是输入数组形状的各个维度上的最大值。
  - 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
  - 当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。

<h4> 简单理解 </h4>

  - 数组形状相同，当前维度值相等，当前维度的值有一个是1

<h2> 2 Numpy 迭代数组 </h2>
<h3> 2.1 numpy.nditer </h3>
<h4> 基本迭代 </h4>

  - 迭代器最基本的任务的可以完成对数组元素的访问
    ```python
    a = np.arange(6).reshape(2,3)
    for x in np.nditer(a):
        print (x, end=", " )       # 0,1,2,3,4,5
    ```
    - 默认迭代顺序与内存中存储顺序相同

<h4> 控制遍历顺序 </h4>

  - order 属性
    ```python
    for x in np.nditer(a, order='F')        
    # Fortran order,列序优先
    for x in np.nditer(a.T, order='C')      
    # C order,行序优先
    ```
  - 修改存储方式
    ```python
    a = np.arange(6).reshape(2,3)
    for x in np.nditer(a.T):
        print (x, end=", " )
    # 0,1,2,3,4,5
    for x in np.nditer(a.T.copy(order='C')):
        print (x, end=", " )
    # 0,3,1,4,2,5
    ```
    - a 和 a.T 的遍历顺序是一样的，因为他们在内存中的存储顺序也是一样的
    - a.T.copy(order = 'C') 的遍历结果是不同的，那是因为它和前两种的存储方式是不一样的，默认是按行访问。

<h4> 修改数组中元素的值 </h4>

  - 参数 op_flags
  - 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），为了在遍历数组的同时，实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式。
    ```python
    a = np.arange(0,60,5).reshape(3,4)  
    for x in np.nditer(a, op_flags=['readwrite']): 
        x[...]=2*x 
    print (a)
    ```

<h4> 使用外部循环 </h4>

  - nditer类的构造器拥有flags参数，它可以接受下列值：
    | 参数          | 描述                                           |
    | ------------- | ---------------------------------------------- |
    | c_index       | 跟踪C顺序的索引                                |
    | f_index       | 跟踪Fortran顺序的索引                          |
    | multi-index   | 每次迭代可以跟踪一种索引类型                   |
    | external_loop | 给出的值是具有多个值的一维数组，而不是零维数组 |
  - 举例
    ```python
    a = np.arange(0,60,5).reshape(3,4)  
    for x in np.nditer(a, flags = ['external_loop'], order = 'F'):  
        print (x, end=", " )
    # [ 0 20 40], [ 5 25 45], [10 30 50], [15 35 55],
    ```

<h4> 广播迭代 </h4>

  - 如果两个数组是可广播的，nditer 组合对象能够同时迭代它们
    ```python
    a = np.arange(0,60,5).reshape(3,4)  
    b = np.array([1,2,3,4], dtype = int)
    for x,y in np.nditer([a,b]):  
        print ("%d:%d" % (x,y), end=",")
    # 0:1, 5:2, 10:3, 15:4, 20:1, 25:2, 30:3, 35:4, 40:1, 45:2, 50:3, 55:4,
    ```

<h2> 3 Numpy 数组操作 </h2>
<h3> 3.1 修改数组形状 </h3>
<h4> 函数概述 </h4>

  - 四个修改数组形状的内置函数
    | 函数    | 描述                                           |
    | ------- | ---------------------------------------------- |
    | reshape | 不改变数据的条件下修改形状                     |
    | flat    | 数组元素迭代器                                 |
    | flatten | 返回一份数组开呗，对拷贝做的修改不影响原始数组 |
    | ravel   | 反馈展开数组                                   |
<h4> np.reshape </h4>

  - numpy.reshape 函数可以在不改变数据的条件下修改形状
    ```python
    numpy.reshape(arr, newshape, order='C')
    ```
    - arr: 要修改形状的数组
    - newshape: 整数或者整数数组
    - order：'C' 按行，'F' 按列，'A' 原顺序，'k' 元素在内存中的出现顺序

<h4> np.ndarray.flat </h4>

  - flat 是一个数组元素迭代器, 对数组中每个元素都进行处理，可以使用flat属性
    ```python
    a = np.arange(9).reshape(3,3) 
    for row in a:
        print (row)
    # [0 1 2] [3 4 5] [6 7 8]
    for element in a.flat:
        print (element)
    # 0 1 2 3 4 5 6 7 8

<h4> np.ndarray.flatten </h4>

  - numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
    ```python
    ndarray.flatten(order='C')
    ```

<h4> np.ndarray.ravel </h4>

  - numpy.ravel() 展平的数组元素，顺序通常是"C风格"，返回的是数组视图,将会影响原始数组
    ```python
    arr.ravel(a, order='C')
    ```

<h3> 3.2 翻转数组 </h3>
<h4> 函数概览 </h3>

  - 四个常用函数
    | 函数      | 描述                  |
    | --------- | --------------------- |
    | transpose | 对换数组维度          |
    | ndarray.T | 和transpose相同，转置 |
    | rollaxis  | 向后滚动指定的轴      |
    | swapaxes  | 兑换数组的两个轴      |

<h4> numpy.transpose </h4>

  - 用于兑换数组的维度
    ```python
    numpy.transpose(arr, axes)
    ```
    - axes: 整数列表，对应维度，通常所有维度都会对换。
    - 对于二维数组相当于转置运算
    - 和 ndarray.T 用法类似

<h4> numpy.rollaxis </h4>

  - 向后滚动特定的轴到一个特定位置
    ```python
    numpy.rollaxis(arr, axis, start)
    ```
    - axis: 要向后滚动的轴，其它轴的相对位置不会改变
    - start: 默认为零，表示完整的滚动。会滚动到特定位置。

<h4> numpy.swapaxes </h4>

  - 用于交换数组的两个轴
    ```python
    numpy.swapaxes(arr, axis1, axis2)
    ```
    - axis1：对应第一个轴的整数
    - axis2：对应第二个轴的整数

<h3> 3.3 修改数组维度 </h3>
<h4> 常用函数 </h4>

  - 四个常用函数
    | 函数         | 描述                       |
    | ------------ | -------------------------- |
    | broadcast    | 产生模仿广播的对象         |
    | broadcast_to | 将数组广播到新形状         |
    | expand_dims  | 扩展数组的形状             |
    | squeeze      | 从数组的形状中删除一维条目 |

<h4> numpy.broadcast </h4>

  - numpy.broadcast 用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果

<h4> numpy.broadcast_to </h4>

  - numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。 它通常不连续。
    ```python
    numpy.broadcast_to(array, shape, subok)
    ```
  - 举例
    ```python
    a = np.arange(4).reshape(1,4)
    print (np.broadcast_to(a,(4,4)))
    # [[0 1 2 3] [0 1 2 3] [0 1 2 3] [0 1 2 3]]
    ```
<h4> numpy.expand_dims </h4>

  - 通过在指定位置插入新的轴来扩展数组形状
    ```python
    numpy.expand_dims(arr, axis)
    ```
    - arr：输入数组
    - axis：新轴插入的位置
  - 举例
    ```python
    x = np.array(([1,2],[3,4]))
    y = np.expand_dims(x, axis = 0)
    print (y)                   # [[[1 2] [3 4]]]
    print (x.shape, y.shape)    # (2, 2) (1, 2, 2)
    ```
<h4> numpy.squeeze </h4>

  - 从给定数组的形状中删除一维的条目
    ```python
    numpy.squeeze(arr, axis)
    ```

<h3> 3.4 连接数组 </h4>
<h4> 常用函数 </h4>

  - 四个常用函数
    | 函数        | 描述                   |
    | ----------- | ---------------------- |
    | concatenate | 连接沿现有轴的数组序列 |
    | stack       | 沿着新轴加入一系列数组 |
    | hstack      | 水平堆叠序列中的数组   |
    | vstack      | 竖直堆叠列中的数组     |

<h4> np.concatenate </h4>

  - 用于沿指定轴连接相同形状的两个或多个数组
    ```python
    numpy.concatenate((a1, a2, ...), axis)
    ```

<h4> np.stack </h4>

  - 用于沿新轴连接数组序列
    ```python
    numpy.stack(arrays, axis)
    ```
  - np.hstack 通过水平堆叠来生成数组
  - np.vstack 通过垂直堆叠来生成数组
    ```python
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])
    print (np.hstack((a,b)))
    # [[1 2 5 6] [3 4 7 8]]
    print (np.vstack((a,b)))
    # [[1 2] [3 4] [5 6] [7 8]]
    ```

<h3> 3.5 分割函数 </h3>
<h4> 常用函数 </h4>

  - 三个常用函数
    | 函数   | 数组及操作                             |
    | ------ | -------------------------------------- |
    | split  | 将一个数组分割为多个子数组             |
    | hsplit | 将一个数组水平分割为多个子数组（按列） |
    | vsplit | 将一个数组垂直分割为多个子数组（按行） |

<h4> np.split </h4>

  - numpy.split 函数沿特定的轴将数组分割为子数组
    ```python
    numpy.split(ary, indices_or_sections, axis)
    ```
    - indices_or_sections：果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置（左开右闭）
  - 举例
    ```python
    a = np.arange(9)
    print (np.split(a,3))
    # [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
    print (np.split(a,[4,7]))
    # [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]
    ```

<h3> 3.6 数组元素的添加与删除 </h3>
<h4> 常用函数 </h4>

  - 五个常用函数
    | 函数   | 元素及描述                             |
    | ------ | -------------------------------------- |
    | resize | 返回指定形状的新数组                   |
    | append | 将值添加到数组末尾                     |
    | insert | 沿指定轴将值插入到指定下表之前         |
    | delete | 删除某个轴子数组，并返回删除后的新数组 |
    | unique | 查找数组内的唯一元素                   |

<h4> np.resize </h4>

  - 返回指定大小的新数组，如果新数组大小大于原始大小，则包含原始数组中的元素的副本。
    ```python
    numpy.resize(arr, shape)
    ```
  - 举例
    ```python
    a = np.array([[1,2,3],[4,5,6]])
    print (np.resize(a,(3,3)))
    # [[1 2 3] [4 5 6] [1 2 3]]
    ```

<h4> np.append </h4>

  - 追加操作会分配整个数组，并把原来的数组复制到新数组中
    ```python
    numpy.append(arr, values, axis=None)
    ```
    - values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
  - 举例
    ```python
    a = np.array([[1,2,3],[4,5,6]])
    print (np.append(a, [7,8,9]))
    # [1 2 3 4 5 6 7 8 9]
    print (np.append(a, [[7,8,9]],axis = 0))
    # [[1 2 3] [4 5 6] [7 8 9]]
    print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))
    # [[1 2 3 5 5 5] [4 5 6 7 8 9]]
    ```

<h4> np.insert </h4>

  - 在给定索引之前，沿给定轴在输入数组中插入值
  - 如果值的类型转换为要插入，则它与输入数组不同。 插入没有原地的，函数会返回一个新数组。 此外，如果未提供轴，则输入数组会被展开。
    ```python
    numpy.insert(arr, index, values, axis)
    ```
    - axis：沿着它插入的轴，如果未提供，则输入数组会被展开
  - 举例
    ```python
    a = np.array([[1,2],[3,4],[5,6]])
    print (np.insert(a,3,[11,12]))
    # [ 1  2  3 11 12  4  5  6]
    print (np.insert(a,1,[11],axis = 0))
    # [[ 1  2] [11 11] [ 3  4] [ 5  6]]
    print (np.insert(a,1,11,axis = 1))
    # [[ 1 11  2] [ 3 11  4] [ 5 11  6]]
    ```

<h4> np.delete </h4>

  - 返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。
    ```python
    numpy.delete(arr, obj, axis)
    ```
    - obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
  - 举例
    ```python
    a = np.arange(12).reshape(3,4)
    print (np.delete(a,5))
    # [ 0  1  2  3  4  6  7  8  9 10 11]
    print (np.delete(a,1,axis = 1))
    # [[ 0  2  3] [ 4  6  7] [ 8 10 11]]
    a = np.array([1,2,3,4,5,6,7,8,9,10])
    print (np.delete(a, np.s_[::2]))
    # [ 2  4  6  8 10]
    ```

<h4> np.unique </h4>

  - 用于去除数组中的重复元素。
    ```python
    numpy.unique(arr, return_index, return_inverse, return_counts)
    ```
    - return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
    - return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式储
    - return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数
  - 举例
    ```python
    a = np.array([5,2,6,2,7,5,6,8,2,9])
    print (np.unique(a))
    # [2 5 6 7 8 9]
    ```