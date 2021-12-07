<link rel=stylesheet href=../style.css>
<h1> pip 命令 </h1>
<h2> 1 pip 基本操作 </h2>
<h3> 1.1 pip 安装 </h3>
<h4> Windows </h4>

  - 使用 `easy_install` ,但该插件已逐渐不被 Python 支持
    - `easy_install pip`
<h4> Ubuntu </h4>

  - `sudo apt install python3-pip`

<h4> Mac </h4>

  - `neo@MacBook-Pro ~ % brew install python3`
  - `neo@MacBook-Pro ~ % pip3 install scrapy`

<h3> 1.2 pip 版本 </h3>

<h4> 查询 pip 版本 </h4>

  - `pip --version`

<h4> 升级 pip 命令 </h4>

  - 新版本需要使用 --user 参数，否则会安装失败，并且删除原版本 pip 
    - 旧：~~`pip install --upgrade pip`~~
    - 新：`pip install --upgrade --user pip`

<h4> 获取帮助 </h4>

  - `pip --help`

<h2> 2 包操作 </h2>
<h3> 2.1 查询包 </h3>
<h4> 显示已安装所有包 </h4>

  - `pip list`
    - `pip list -o` 显示可升级的包
<h4> 查询指定包 </h4>

  - `pip search package` : 查询包基础信息
  - `pip show package` : 显示包的详细信息

<h3> 2.2 安装包 </h3>
<h4> 安装包 </h4>

  - `pip install package`
    - 安装特定版本的包可以使用 `==,>,<,<=,>=` 进行限定
    - `pip install 'Markdown>2.0,<2.0.3'`
  - `pip install -r list.txt` 将 txt 文件中所写的所有包批量安装

<h4> 卸载包 </h4>

  - `pip uninstall package`

<h4> 升级包 </h4>

  - `pip install -U package`
  - `pip install package --upgrade`

<h2> 3 镜像 </h2>
<h3> 3.1 镜像安装 </h3>
<h4> 指定镜像 </h3>

  - `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  matplotlib`

<h4> 设定默认镜像 </h4>

  - `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`

<h3> 3.2 常用镜像 </h3>
<h4> 国内镜像 </h4>

  - 清华：https://pypi.tuna.tsinghua.edu.cn/simple
  - 阿里：https://mirrors.aliyun.com/pypi/simple
  - 中科大：https://mirrors.bfsu.edu.cn/pypi/web/simple
  - 豆瓣：https://pypi.doubanio.com/simple