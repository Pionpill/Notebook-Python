<link rel=stylesheet href=../../style.css>
<h1> re 包 </h1>
<h2> 1 Regex 对象与 Match 对象 </h2>
<h3> 1.1 Regex 对象 </h3>
<h4> re.compile() 函数 </h4>

  - 函数原型
    ```py
    re.compile(pattern: AnyStr, flags: Union[int, RegexFlag]) -> Pattern[AnyStr]
    ```
  - 基本用法
    - 传入一个正则表达式字符串，返回一个 Regex 模式对象。
  - 第二参数
    - re.DOTALL 参数匹配包括换行符的所有字符
      ```py
      newlineRegex = re.compile(".*",re.DOTALL)
      newlineRegex.search("Serve the public trust.\nProtect the innocent.").group()
      # "Serve the public trust.\nProtect the innocent."
      noNewlineRegex = re.compile(".*")
      noNlineRegex.search("Serve the public trust.\nProtect the innocent.").group()
      # "Serve the public trust."
      ```
    - re.IGNORECASE/re.I 不区分大小写
      ```py
      robocop = re.compile(r"robocop",re.I)
      robocop.search('RoboCop is part man,part machine').group()
      # 'RoboCop'
      ```
    - re.VERBOSE 书写参数
  - 复杂表达式
    - 使用 """...""" 描写多行正则表达式
    - 使用 | 传入多个第二参数
      ```py
      phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?    # area
        (\s|-|\.)?            # separator
        (\d{3})               # first 3 digits
      )''',re.VERBOSE|re.DOTALL)
      ```

<h4> Regex.search() 函数 </h4>

  - 函数原型
    ```py
    Regex.search(pattern: AnyStr, string: AnyStr, flags: Union[int, RegexFlag]) -> Optional[Match[AnyStr]]
    ```
  - 基本用法
    - 传入一个字符串，匹配 Regex 中的内容，输出为 Match 对象

<h4> Regex.findall() 函数 </h4>

  - 函数原型
    ```py
    Regex.findall(string: AnyStr)
    ```
  - 基本用法
    - 匹配样式所有的出现，返回一个字符串列表。
    - 若有分组，列表中嵌套元组

<h4> Regex.sub() 函数 </h4>

  - 函数原型
    ```py
    Regex.sub(string1: AnyStr, string2: AnyStr)
    ```
  - 基本用法: 将 Regex 对应的正则表达式匹配 string2 中内容替换为 string1
    ```py
    namesRegex = re.compile(r"Agent \w+")
    namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
    # 'CENSORED gave the secret documents to Agent Bob.'
    ```
  - 使用匹配的文本本身作为替换的一部分，再 sub() 方法的第一个参数中，输入 \1\2\3 表示"在替换中输入分组1，2，3的文本"
    ```py
    agentNamesRegex = re.compile(r"Agent (\w)\w*")
    agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that')
    # A**** told C**** that
    ```


<h3> 1.2 Match 对象 </h3>
<h4> Match.group() 函数 </h4>

  - 函数原型
    ```py
    Match.group()
    ```
  - 基本用法
    - 返回一个或者多个匹配的子组。如果只有一个参数，结果就是一个字符串，如果有多个参数，结果就是一个元组 (每个参数对应一个项)。

<h2> 2 匹配模式 </h2>
<h3> 2.1 括号分组 </h3>
<h4> 分组 </h4>

  - 创建分组，然后可以使用 group() 匹配对象方法，从分组中候区匹配文本
    ```py
    import re
    phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
    mo = phoneNumRegex.search("My number id 415-555-4242.")
    mo.group(1)     # '415'
    mo.group(2)     # '555-4242'
    mo.group(0)     # '415-555-4242'
    mo.group()      # '415-555-4242'
    ```

<h4> 管道匹配多个分组 </h4>

  - 关键字"|"称为管道，可以从多个表达式中匹配一个
    ```py
    import re
    heroRegex = re.compile(r"Batman|Tina Fey")
    mo1 = hereRegex.search('Batman and Tina Fey.')
    mo1.group()   # Batman
    mo2 = hereRegex.search('Tina Fey and Batman.')
    mo2.group()   # Tina Fey 
    ```

<h3> 2.2 次数匹配 </h3>
<h4> ?: 可选匹配 </h4>

  - ? 表示匹配模式可选，匹配 0或1 次
    ```py
    import re
    batRegex = re.compile(r"Bat(wo)?man")
    mo1 = batRegex.search("The Adventures of Batman")
    mo1.group()     # "Batman"
    mo2 = batRegex.search("The Adventures of Batwoman")
    mo2.group()     # "Batwoman"
    ```
  - 贪心与非贪心匹配
    ```py
    greedyHaRegex = re.compile(r"(Ha){3,5}")
    mo1 = greedyRegex.search("HaHaHaHaHa")
    mo1.group()   # "HaHaHaHaHa"
    nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
    mo2 = greedyRegex.search("HaHaHaHaHa")
    mo2.group()   # "HaHaHa"
    ```

<h4> *: 匹配 </h4>

  - *: 匹配零次或多次
    ```py
    import re
    batRegex = re.compile(r"Bat(wo)*man")
    mo = batRegex.search("The Adventures of Batwowowowoman")
    mo.group()     # "Batwowowowoman"
    ```

<h4> +: 存在匹配 </h4>

  - +: 匹配一次或多次
    ```py
    import re
    batRegex = re.compile(r"Bat(wo)+man")
    mo = batRegex.search("The Adventures of Batman")
    mo == None     # True
    ```

<h4> {}: 指定匹配 </h4>

  - {}: 指定匹配次数
    ```py
    (Ha){3}       # (Ha)(Ha)(Ha)
    (Ha){3,4}     # ((Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha))
    (Ha){,5}      # 匹配 0~5 次 Ha
    ```
  - 贪心与非贪心匹配
    ```py
    greedyHaRegex = re.compile(r"(Ha){3,5}")
    mo1 = greedyRegex.search("HaHaHaHaHa")
    mo1.group()   # "HaHaHaHaHa"
    nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
    mo2 = greedyRegex.search("HaHaHaHaHa")
    mo2.group()   # "HaHaHa"
    ```
    ```py
    greedyRegex = re.compile(r"<.*>")
    mo1 = greedyRegex.search("<To serve man> for dinner.>")
    mo1.group()      # "<To serve man> for dinner,>"
    nongreedyRegex = re.compile(r"<.*>")
    mo2 = nongreedyRegex.search("<To serve man> for dinner.>")
    mo2.group()      # "<To serve man>"
    ```

<h2> 3 匹配字符 </h2>
<h3> 3.1 字符分类 </h3>
<h4> 缩写字符分类 </h4>

  - 常用缩写字符分类
    | 缩写字符分类 |          表示          |
    | :----------: | :--------------------: |
    |      \d      |       0-9的数字        |
    |      \D      |         非 \d          |
    |      \w      |   字母，数字和下划线   |
    |      \W      |         非 \w          |
    |      \s      |  空格，制表符，换行符  |
    |      \S      | 非空格，制表符，换行符 |

<h4> []: 自定义字符分类 </h4>

  - []: 字符匹配括号内字符
    ```py
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    vowelRegex.finall("RoboCop eats Appale")
    # ['o','o','o','e','a','A','a','e']
    ```
  - ^: 非
    ```py
    vowelRegex = re.compile(r'[^aeiouAEIOU]')
    vowelRegex.finall("RoboCop eats Appale")
    # ['R','b','C','p','t','s','p','p','l']
    ```

<h3> 3.2 匹配字符 </h3>
<h4> ^,$: 匹配开始与结束 </h4>

  - ^: 匹配开始
    ```py
    beginRegex = re.compile(r"^Hello")
    mo = beginRegex.search("Hello world!")
    mo.group()      # "Hello"
    ```
  - $: 匹配结束
    ```py
    endsRegex = re.compile(r"\d$")
    mo = endsRegex.search("Your number is 42")
    mo.group()      # 2
    ```

<h4> .: 通配字符 </h4>

  - .: 匹配换行符之外的所有字符
    ```py
    atRegex = re.compile(r'.at')
    atRegex.findall("The cat in the hat sat on the flay mat.")
    # ['cat','hat','sat','lat','mat']
    ```

<h4> .*: 匹配所有字符 </h4>

  - .*: 匹配任意长个任意个字符(换行符除外)
    ```py
    nameRegex = re.compile(r"First Name:(.*)Last Name(.*)")
    mo = nameRegex.search("First Name: Pionpill Last Name: Brandon")
    mo.group(1)     # 'Pionpill'
    mo.group(2)     # 'Brandon'
    ```
  - 贪心与非贪心
    ```py
    greedyRegex = re.compile(r"<.*>")
    mo1 = greedyRegex.search("<To serve man> for dinner.>")
    mo1.group()      # "<To serve man> for dinner,>"
    nongreedyRegex = re.compile(r"<.*>")
    mo2 = nongreedyRegex.search("<To serve man> for dinner.>")
    mo2.group()      # "<To serve man>"
    ```
  - re.DOTALL 参数匹配包括换行符的所有字符
    ```py
    newlineRegex = re.compile(".*",re.DOTALL)
    newlineRegex.search("Serve the public trust.\nProtect the innocent.").group()
    # "Serve the public trust.\nProtect the innocent."
    noNewlineRegex = re.compile(".*")
    noNlineRegex.search("Serve the public trust.\nProtect the innocent.").group()
    # "Serve the public trust."
    ```