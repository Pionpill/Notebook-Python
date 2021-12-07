<link rel=stylesheet href=style.css>
<h1> pandas 数据结构 </h1>
<h2> 1 Series </h2>
<h3> 1.1 创建 Series </h3>
<h4> Series 用法 </h4>

  - Series 主要用于一维数组存储。
  - 相比于 ndarray，支持更多数据类型以及同一对象不同数据类型存储

<h4> pd.Series() 方法 </h4>

  - 方法原型
    ```py
    pd.Series(
        data=None,        # 数据，可以是数值，列表，字典，np数组等
        index=None,       # 标签，与数据一一对应，长度必须和data一致，默认为索引
        dtype=None,       # 数据类型
        name=None,        # pandas 特有的标签名
        copy=False,       # 拷贝输入数据
        fastpath=False,
    )
    ```
  - 几种创建 Series 方式
    ```py
    # 数组传入
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    # 字典传入
    d = {'b': 1, 'a': 0, 'c': 2}
    pd.Series(d)
    # 有缺失值的字典传入，缺失值对应为 NaN
    pd.Series(d, index=['b', 'c', 'd', 'a'])
    # 标量传入，所有数据值相同
    pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
    ```

<h3> 1.2 Series 对象 </h3>
<h4> 数据访问 </h4>

  - 类似数组：通过索引访问
    ```py
    series = pd.Series([-1,2,3,4,5],index=['a','b','c','d','e'])
    print(series[0])    # -1
    ```
  - 类使字典：通过 index 访问
    ```py
    series = pd.Series([-1,2,3,4,5],index=['a','b','c','d','e'])
    print(series.a)    # -1
    ```

<h4> 索引与切片 </h4>

  - Series 对象能实现与 ndarray 几乎一致的切片功能
    ```py
    series = pd.Series([-1,2,3,4,5],index=['a','b','c','d','e'])
    series[:3]            # a -1  b 2  c 3
    series[series>1]      # b 2  c 3  d 4  e 5
    series[[2,1]]         # b 2  a -1
    np.exp(series)        # e^-1 e^2 ...
    ```

<h4> 数据操作 </h4>

  - series 和 numpy 一样可以直接进行基本的数据运算
    ```py
    series = pd.Series([-1,2,3,4,5],index=['a','b','c','d','e'])
    series * 2
    series + 5
    ```

<h4> 常用属性 </h4>

  - 常用属性表
    | 属性         | 说明         |
    | ------------ | ------------ |
    | series.index | 获取标签列表 |
    | series.array | 获取数组列表 |

<h3> 1.3 Series 函数 </h3>
<h4> s.to_numpy() </h4>

  - 作用：将 series 数组转换为 numpy 数组
  - 可以加入参数，指定数据类型
    ```py
    ser.to_numpy(dtype="datetime64[ns]")
    ```

<h4> s.rename() </h4>

  - 作用：对 series 对象重命名

<h2> 2 DataFrame </h2>
<h3> 2.1 创建 DataFrame </h3>
<h4> DataFrame 简介 </h4>

  - DataFrame 是由多种的列构成的二维标签数据结构
  - DataFrame 有用两个基本属性，默认生成为 [0,len(data)-1]
    - index: 行标签
    - column: 列标签
  - DataFrame 和 Series 一样，在指定索引时，会丢弃不被包含的所有数据

<h4> pd.DataFrame() 方法 </h4>

  - 方法原型
    ```py
    pd.DataFrame(data, index, columns, dtype, copy)
    ```
  - 几种创建 DataFrame 的方法
    ```py
    # 通过字典创建
    d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    df = pf.DataFrame(d,index=['a','b','c'],column=['two','three'])
    # 其他构造方式与 Series 类型，不再赘述
    ```
  - 备选构造器
    - pd.DataFrame.from_dict()
      - 接收字典组成的字典或数组序列组成的字典
      - 参数 orient='index' 时，键是行标签。
        ```py
        pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),orient='index', columns=['one', 'two', 'three'])
        # 输出
          one  two  three
        A    1    2      3
        B    4    5      6
        ```
    - pd.DataFrame.from_records()
      - 支持元组列表或结构数据类型
      - 生成的 DataFrame 索引是结构数据类型指定的字段

<h3> 2.2 DataFrame 对象 </h3>
<h4> 列数据访问与修改 </h4>

  - 使用索引提取数据
    ```py
    df['one']  # 以字典形式访问
    # a 1.0    b 2.0    c 3.0    d NaN
    df.one     # 以面向对象方式访问
    # a 1.0    b 2.0    c 3.0    d NaN
    df['three'] = df['one'] + df['two']
    df['four'] = df['one'] > 1
    # 对 DataFrame 进行类似数据库操作，结果保留在新列中
    df['five'] = 'bar'
    # 对列进行广播
    df['six'] = df['one'][:2]
    # 指定行赋值
    ```
  - DataFrame 常用的三个操作
    ```py
    del df['two']             # 删除列
    three = df.pop('three')   # 弹栈(列)
    df.insert(1,'bar',df['one'])    # 插入新列
    ```

<h4> 用方法链分配新列 </h4>

  - .assign() 方法
    ```py
    df2 = df.assign(three = df['one']+df['two'])
    # .assign() 函数返回的是副本，原 DataFrame 不变
    # 该方法通常结合 lambda 表达式使用
    ```

<h4> 索引与选择 </h4>

  - 索引的基础操作
    | 操作             | 句法          | 返回值类型 |
    | ---------------- | ------------- | ---------- |
    | 选择列           | df[col]       | Series     |
    | 用标签选择行     | df.loc[label] | Series     |
    | 用整数索引选择行 | df.iloc[loc]  | Series     |
    | 行切片           | df[5:10]      | DataFrame  |
    | 布尔向量选择行   | df[bool_vec]  | DataFrame  |

<h4> 数据对齐和运算 </h4>

  - DataFrame 可以自动对齐列和索引数据
  - 生成的结果是列和行标签的并集
  - DataFrame 与 Series 运算时按索引进行广播

<h3> 2.3 控制台显示 </h3>
<h4> 显示控制方法 </h4>

  - 常用的显示控制方法
    | 方法         | 作用                    |
    | ------------ | ----------------------- |
    | .info()      | 查看 DataFrame 信息摘要 |
    | .to_string() | 返回字符串形式          |
  - .set_option() 方法
    | 参数                 | 作用                           | 举例                              |
    | -------------------- | ------------------------------ | --------------------------------- |
    | display.width        | 设置输出宽度                   | pd.set_option('display.width',40) |
    | display.max_colwidth | 设置最大列宽, 多余以省略号显示 | pd.set_option('max_colwidth',30)  |