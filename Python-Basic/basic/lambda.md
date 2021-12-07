<link rel=stylesheet href=../style.css>
<h1> lambda 表达式 </h1>
<h2> 1 lambda 基础 </h2>
<h3> 1.1 lambda 关键字 </h3>
<h4> 语法格式 </h4>

  - 语法
    ```python
    lambda argument_list: expression
    ```
    - argument_list: 参数列表，与方法形参相似
    - expression: 表达式，只能是单行

<h4> lambda 表达式的特征 </h4>

  - 三个特征
    - lambda 函数是匿名的
    - 输入输出：输入传到 argument_list 的值，输出根据 expression 计算得到的值
    - 功能简单

<h4> lambda 表达式的用法 </h4>

  - 将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数
    ```python
    add = lambda x, y: x+y
    add(1,2)  # 3
    ```
  - 将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换
  - 将lambda函数作为其他函数的返回值，返回给调用者
  - 将lambda函数作为参数传递给其他函数(部分Python内置函数接收函数作为参数)
    - filter函数: 指定过滤列表元素的条件
      ```py
      filter(lambda x: x % 3 == 0,[1,2,3])
      # [3]
      ```
    - sorted函数: 指定对列表中所有元素进行排序的准则
      ```py
      sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))
      # [5, 4, 6, 3, 7, 2, 8, 1, 9]
      ```
    - map 函数: 指定对列表中每一个元素的共同操作
      ```py
      map(lambda x: x+1, [1,2,3])
      # [2, 3, 4]
      ```
    - reduce函数: 指定列表中两两相邻元素的结合条件
      ```py
      reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
      # '1, 2, 3, 4, 5, 6, 7, 8, 9'
      ```