<link rel=stylesheet href=style.css>
<h1> NumPy IO 和 Plot </h1>
<h2> 1 NumPy IO </h2>
<h3> 1.1 .npy 文件 </h3>

> 详细说明：[菜鸟](https://www.runoob.com/numpy/numpy-io.html)

<h4> npy文件简介 </h4>

  - .npy 文件用于存储重建 ndarray 所需的数据、图形、dtype 和其他信息。
  - .npy 文件是乱码的，因为它们是 Numpy 专用的二进制格式后的数据
  - 常见的 IO 函数
    | 函数                 | 作用                        |
    | -------------------- | --------------------------- |
    | load()/save()        | 读写 .npy 文件              |
    | savez()              | 将多个数组写入文件          |
    | loadtxt(),savetext() | 处理正常的文本文件(.txt 等) |

<h4> numpy.save() </h4>

  - 数组保存到以 .npy 为扩展名的文件中
    ```py
    numpy.save(file, arr, allow_pickle=True, fix_imports=True)
    ```
    - file：要保存的文件，扩展名为 .npy，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上。
    - arr: 要保存的数组
    - allow_pickle: 可选，布尔值，允许使用 Python pickles 保存对象数组，Python 中的 pickle 用于在保存到磁盘文件或从磁盘文件读取之前，对对象进行序列化和反序列化。
    - fix_imports: 可选，为了方便 Pyhton2 中读取 Python3 保存的数据。

<h4> np.savez </h4>

  - 将多个数组保存到以 npz 为扩展名的文件中
    ```py
    numpy.savez(file, *args, **kwds)
    ```
    - file：要保存的文件，扩展名为 .npz，如果文件路径末尾没有扩展名 .npz，该扩展名会被自动加上。
    - args: 要保存的数组，可以使用关键字参数为数组起一个名字，非关键字参数传递的数组会自动起名为 arr_0, arr_1, …　。
    - kwds: 要保存的数组使用关键字名称。

<h3> 1.2 txt文件读取 </h3>
<h4> np.savetxt() </h4>

  - 以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据
    ```py
    np.loadtxt(FILENAME, dtype=int, delimiter=' ')
    np.savetxt(FILENAME, a, fmt="%d", delimiter=",")
    ```
    - delimiter: 指定各种分隔符、针对特定列的转换器函数、需要跳过的行数等