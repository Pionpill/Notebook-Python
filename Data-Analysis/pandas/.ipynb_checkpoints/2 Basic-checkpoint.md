<link rel=stylesheet href=style.css>
<h1> pandas 基础操作 </h1>
<h2> 1 基础操作 </h2>
<h3> 1.1 快速预览 </h3>
<h4> head 与 tail </h4>

  - head() 与 tail() 用于快速预览 Series 和 DataFrame
  - 显示头部或尾部五条数据

<h3> 1.2 属性与底层操作 </h3>
<h4> 访问元数据 </h4>

  - 常用维度信息属性与方法
    | 方法        | 放回值                  |
    | ----------- | ----------------------- |
    | .shape      | 维度元组                |
    | .array      | 以一维数组形式返回      |
    | .to_numpy() | 返回 ndarray 类型的数组 |
    | .array()    | 与 .to_numpy() 类似     |

<h3> 1.3 匹配与广播机制 </h3>
<h4> 常用方法处理 </h4>

  - 常用运算方法
    | 方法      | 说明                 | 方法    | 说明   |
    | --------- | -------------------- | ------- | ------ |
    | .add()    | 加法                 | .div()  | 除法   |
    | .sub()    | 减法                 | .radd() | 不知道 |
    | .mul()    | 乘法                 | .rsub() | 不知道 |
    | .divmod() | 同时向下取整与模运算 |
  - 运算方法中的广播机制
    - 通过在第二个参数中指定运算维度的方式，对 DataFrame 对象进行广播运算
        ```py
        row = df.iloc[1]
        column = df['one']
        df.sub(row , axis = 'columns')
        df.sub(column, axis='index')
        ```
  - .divmod() 方法
    - 广播用法
      ```py
      s = pd.Series(np.arange(10))
      div, rem = divmod(s,3)  # div 为结果 rem 为余数
      ```

<h3> 1.4 缺失值操作 </h3>
<h4> 查询缺失值 </h4>

  - isnull() 方法
    ```py
    x = data.isnull()     # 返回一个 DataFrame 表, NaN 值为 True
    sum1 = x.sum()        # 返回一个 Series 对象，存储列上逻辑值 True 总数
    count = data.count()  # 返回一个 Series 对象，存储列上不为 NaN 总数
    sum2 = sum1.sum()     # 返回 NaN 值个数
    ```

<h4> 处理缺失值 </h4>

  - dropna() 方法：删除 NaN 所在行/列
    ```python
    data1 = data.dropna(axis = 0)   # 删除行,也可以 axis = 'index'
    data2 = data.dropna(axis = 1)   # 删除行,也可以 axis = 'column'
    data.dropna(axis = 'index',inplace = True)    # 原地删除
    ```
  - fillna() 方法：替换 na
    ```py
    data.fillna(0)   # 替换为 0
    data.fillna(method='ffill',axis=0) # 向前填充,类似的 method 还有很多
    ```
  - 运算过程中的处理
    ```py
    df.add(df2, fill_value=0) # 将 df 中的 NaN 替换为 0
    ```

<h3> 1.5 比较操作 </h3>
<h4> 比较运算方法 </h4>

  - 所有比较运算方法均返回一个 bool 值组成的 DataFrame
    | 方法 | 英文         | 中文 | 方法 | 英文                  | 中文     |
    | ---- | ------------ | ---- | ---- | --------------------- | -------- |
    | eq   | equal to     | 等于 | ne   | not equal             | 不等于   |
    | lt   | less than    | 小于 | le   | less than or equal    | 小于等于 |
    | gt   | greater than | 大于 | ge   | greater than or equal | 大于等于 |
  - 例子
    ```py
    df.gq(df2)    # 放回 DataFrame 布尔值表
    ```

<h4> 布尔简化 </h4>

  - empty(), any(), all(), bool()
  - 和比较运算方法类似，返回一个布尔值构成的表格

<h4> 比较对象 </h4>

  - DataFrame 对象的比较将返回对象中各个成员的结果
  - 若仅对某一个数据类型进行对比，将进行广播

<h3> 1.6 合并数据 </h3>
<h4> 合并缺失数据 </h4>

  - df1.combine_first(df2) 函数
    - 将 df1 在 df2 中缺失或没有的数据添入 df1
  - combine_first() 函数
    ```py
    def combiner(x, y):
        return np.where(pd.isna(x), y, x)
    ```

<h3> 1.7 统计函数 </h3>
<h4> 描述性统计 </h4>

  - 与 numpy 类似，pandas 也支持各种数据类型的统计函数
    ```py
    df.mean(axis = 0,skipna = False)
    ```
<h4> 常用统计函数 </h4> 

  - 常用函数汇总表
    | 函数     | 描述             | 函数       | 描述         |
    | -------- | ---------------- | ---------- | ------------ |
    | count()  | 统计非空值数量   | sum()      | 求和         |
    | mean()   | 平均值           | mad()      | 平均绝对偏差 |
    | median() | 算数中位数       | min()      | 最小值       |
    | max()    | 最大值           | mode()     | 众数         |
    | abs()    | 绝对值           | prod()     | 乘积         |
    | std()    | 标准偏差         | var()      | 无偏方差     |
    | sem()    | 平均值的标准误差 | skew()     | 样本偏度     |
    | kurt()   | 样本峰度         | quantile() | 样本分布数   |
    | cumsum() | 累加             | cumprod()  | 累乘         |
    | cummax() | 乘积最大值       | cummin()   | 乘积最小值   |
    | unique() | 不同值个数       |

<h4> 数据总结 </h4>

  - describe() 方法
    - 该方法将计算出数据的各种常用统计量

<h4> 最大值最小值索引 </h4>

  - Series 与 DataFrame 的 idxmax() 与 idxmin() 函数计算最大值与最小值对应的索引
    ```py
    df.idmax(axis = 0)
    ```
<h4> 值计数 </h4>

  - Series 的 value_counts() 方法及顶级函数计算一维数组中数据值的直方图，还可以用作常规数组的函数
    ```py
    pd.value_counts()
    ```

<h4> 多函数聚合 </h4>

  - 用列表形式传递多个聚合函数。每个函数在输出结果 DataFrame 里以行的形式显示
    ```py
    In [160]: tsdf.agg(['sum', 'mean'])
    Out[160]: 
                A         B         C
    sum   3.033606 -1.803879  1.575510
    mean  0.505601 -0.300647  0.262585

    In [161]: tsdf.A.agg(['sum', 'mean'])
    Out[161]: 
    sum     3.033606
    mean    0.505601

    In [165]: tsdf.agg({'A': ['mean', 'min'], 'B': 'sum'})
    Out[165]: 
    A    0.505601
    B   -1.803879
    ```

<h4> Transform API </h4>

  - transform() 支持 NumPy 函数、字符串函数及自定义函数
    ```py
    pd.transform(np.abs)  # 'abs'  lambda x:a.abs()
    pf.A.transform([np.abs, lambda x: x + 1])
    ```

<h3> 1.8 格式化 </h3>
<h4> 重置索引与对齐 </h4>

  - align 对齐，该方法支持 join 参数
    | 对象                    | 说明                         |
    | ----------------------- | ---------------------------- |
    | join='outer'            | 两个对象索引的合集，为默认值 |
    | join='left/right/inner' | 意会                         |
  - 重置索引后的两个 Series 元组
    ```py
    s1.align(s2, join='inner')
    ```