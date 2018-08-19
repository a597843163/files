## FLASK模板引擎

##### 说明：

模板文件就是按照一定的规则 书写的一个负责展示的html页面  模板引擎就是提供特定规则的解释和替换工具

##### Jinja2

在flask中使用的模板引擎就是Jinja2   是由flask核心开发组成员开发的

## 一、模板的使用

#### (1) 准备工作

```python
project/
	manage.py   #项目启动控制文件
    /templates  #装有模板文件的文件夹
```

#### (2) 导入渲染模板文件的方法

##### render_template()

##### render_template_string()

**实例**

```python
@app.route('/')
def index():
    return render_template('index.html',title='首页')
	return render_template('public/demo.html',title='首页') #渲染templates下的public文件夹中的nav.html的模板
    return render_template_string('<span style="color:red;font-size:20px;">首页</span>') #直接渲染字符串响应给浏览
```

#### (3) 传递变量给模板

1. 变量遵循标识符规则
2. {{变量名}}
3. 在模板中都是对象 使用变量.名称  去调用  如：var = {'name':'张三'}   var.name
4. 如果在模板中给定的变量不存在 则插入的为空字符

## 二、过滤器

过滤器是通过管道符|来实现的  例如{{ name|length }}

1. abs   返回数值的绝对值   `{{ var|abs }}`

2. default  默认值  当值为undefined才会走默认值

   ```python
   var|default('默认值')
   var|default('默认值',boolean=True) #此刻var的值为undefined和False都会执行默认值
   ```

3. first   取出变量中的第一个值

4. last    取出变量中的最后一个值

5. join(value)  将值按照value拼凑成字符串

   ```python
   {{ var.list|join('x') }}
   ```

6. format(value)  格式化

   ```python
   {{ "%s说 我是%s 我今年%d岁了 存款为%.2f"|format('大朗','潘金莲',18,2) }}
   {{name}}说 我是{{}} 我今年{{}}岁了 存款为{{}}
   ```

7. length  计算变量的长度

8. safe      将变量中的html代码不在进行转义

9. int      转换为整形

10. float   转换为浮点型

11. list      转换为list类型

12. lower   转换为小写

13. upper   转换为大写

14. replace  替换

15. trim   删除俩侧多余的空格

16. striptagse  删除html中标签




## 三、标签

**语法：**{% 标签名 %}

**作用：**

1. 在输出中创建文本
2. 控制逻辑和循环

#### (1) if

可以使用 `> < >= <= ==  !=` 进行判断   也可以通过`and or  not  in  not in` 来组合使用

##### 主体结构

```python
{% if %}
	...
{% elif %}
	...
{% else %}
	...
{% endif %}
```



#### (2) for in 遍历

**主体结构**

```python
{% for xxx in 序列 %}
	...
{% else %}
    <h1>当迭代或者遍历的遍历不存在时 则走else</h1>
{% endfor %}
```

**遍历字典**

```python
{% for k,v in var.dict.items() %}
    {{ k }}=>{{ v }}<br />
{% endfor %}
```



#### (3) 获取遍历时的状态

| 变量            | 描述             |
| ------------- | -------------- |
| loop.index()  | 获取当前迭代的索引 从1开始 |
| loop.index0() | 获取当前迭代的索引 从0开始 |
| loop.first    | 是否为第一次迭代       |
| loop.last     | 是否为最后一次迭代      |
| loop.length   | 迭代的长度          |

**实例**

```python
{% for k,v in var.dict.items() %}
{#    {% if loop.first %}#}
    {% if loop.last %}
        <h2>{{ k }}=>{{ v }} 迭代从1开始的索引值{{ loop.index }} 迭代从0开始的索引值{{ loop.index0 }}  遍历的次数{{ loop.length }}</h2>
    {% endif %}
{% endfor %}
```

**注意：**

不可以使用 break或者continue来控制循环的执行



## 四、注释

{# 注释的内容 #}





## 五、文件包含  include

include语句 可以把一个模板的代码 导入到另外的一个模板中  把到如的模板中代码 copy到当前模板中的某个位置

**作用：**将模板中公共的部分提取出来 进行导入

**主体结构**

```python
{% include 'xxx.html' %}
{% include 'dir/xxx.html' %}
```

**实例** 

demo.html

```python
{% include 'public/nav.html' %}
<div>我是中间的内容部分</div>
{% include 'public/footer.html' %}
```

nav.html

```html
<nav>导航栏</nav>
```

footer.html

```html
<footer>底部栏</footer>
```

**目录层级**

```python
project/
	templates/
    	public/
        	nav.html
            footer.html
       	demo.html
```



## 六、在模板中创建变量

**(1) 主体结构**

```python
{% set 变量名=值 %}
```

**注意：**

当前设置模板变量为全局 在整个模板中都能够获取到

**(2) with**

```python
{% with %}
	{% set var='xxx' %}
{% endwith %}

{% with  set var='xxx'  %}
{% endwith %}
```

**注意：**

只能够在 with内部使用变量 设置为局部变量



## 七、macro 宏的使用

#### (1) 宏的定义 并设置参数默认值（使用python和函数一样）

```python
{% macro input(type,name='',value='') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}
```

#### (2) 宏的调用

```python
<p>用户名{{ input('text','username') }}</p>
<p>密码{{ input('password','userpass') }}</p>
<p>{{ input(type='submit',value='提交') }}</p>
```

**注意**

1. 只能在宏的定义下方去调用
2. 宏如果存在参数且没有默认值 则在调用的时候不传参也不会报错
3. 宏可以像函数的关键字参数一样去调用
4. 正常情况宏会将常用的特定功能的代码块封装成宏 并且放在单独的文件中 在需要的时候 去导入并调用 类似于python的模块

#### (3) 宏的导入

1. import ... as ...

   ```python
   {% import 'form.html' as forms %}
   {#  使用 #}
   {{ forms.input('text') }}
   ```

2. from ... import ... 

   ```python
   {% from 'form.html' import input %}
   <p>{{ input(type='submit',value='提交') }}</p>
   ```

3. from ... import ... as ...

   ```python
   {% from 'form.html' import input as f %}
   <p>{{ f(type='submit',value='提交') }}</p>
   ```



## 八、模板的继承

**作用：**  继承是将模板中很多公共的部分 提取出来  放在父模板中 通过继承 将自己需要改变的位置进行改变 减少了很多的重复代码

##### 标签

1. {% extends %}
2. {% block %}

**实例**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
        <meta charset="UTF-8">
        <title>{% block title %}标题{% endblock %}</title>
        <style>
            {% block style %}
                *{color:red;padding:0;margin:0;font-size: 16px;text-decoration: none;}
            {% endblock %}
        </style>
        {% block linkcss %}
        {% endblock %}
        {% block js %}
        {% endblock %}
    {% endblock %}
</head>
<body>
{% include 'public/nav.html' %}
<div id="content">
    {% block con %}
        中间的内容部分
    {% endblock %}
</div>
{% include 'public/footer.html' %}
</body>
</html>
```

child.html

```python
{% extends 'base.html' %}
{% block title %}子模板{% endblock %}
{% block style %}
    {{ super() }}
    li{width:200px;height:30px;line-height:30px;border-bottom:1px solid red;margin-bottom:5px;}
{% endblock %}

{% block con %}
    <ul>
        {% for i in range(6) %}
            <li>{{ i }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

**注意：**

当重写了一个方法以后  父类的所有样式全部消失 查看 有没有调用super() 



## 九、加载静态资源

在flask中 静态资源文件夹默认为 static   

**目录结构**

```python
project/
	manage.py	#启动文件
    templates/  #模板文件目录
    static/ 	#静态资源目录
    	img/
        	17.jpg
        2.jpg
     Flask(__name__,static_floder='myStatic') #不建议  需要遵守命名规则
```

实例

```python
<img src="{{ url_for('static',filename='2.jpg') }}" alt="">
<img src="{{ url_for('static',filename='img/17.jpg') }}" alt="">
```



## 十、flask-bootstrap

#### (1) 安装

##### pip install flask-bootstrap

#### (2) 使用

```python
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True #加载本地的bootstrap样式
bootstrap = Bootstrap(app)
```

#### (3) 继承bootstrap的base模板

```html
{% extends 'bootstrap/base.html' %}
{% block title %}首页{% endblock title %}
```

#### (4) 定制自己的bootstrap的base模板页面

```html
{% extends 'bootstrap/base.html' %}
{% block navbar %}
<nav class="navbar navbar-inverse" style="border-radius: 0px;">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#"><span class="glyphicon glyphicon-flag" aria-hidden="true"></span></a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">首页 <span class="sr-only">(current)</span></a></li>
        <li><a href="#">发帖子</a></li>
      </ul>

      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">注册</a></li>
        <li><a href="#">登录</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">个人中心 <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">修改头像</a></li>
            <li><a href="#">修改信息</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">修改密码</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
{% endblock %}

{% block content %}
    <div class="container">
      {% block page_content %}
        我是页面的内容
      {% endblock %}
    </div>
{% endblock %}
```

#### (5) 定制错误页面

```python
@app.errorhandler(404)
def getFourError(e):
    return render_template('error.html',errorCode=404,errorInfo=e)

@app.errorhandler(500)
def getFiveError(e):
    return render_template('error.html',errorCode=500,errorInfo=e)
```

error.html

```html
{% extends 'common/base.html' %}
{% block title %}{{ errorCode }}{% endblock %}
{% block page_content %}
    <div class="alert alert-danger" role="alert">{{ errorInfo }}</div>
{% endblock %}
```



## 十一、视图传递参数

#### (1) 使用全局变量g

manage.py

```python
@app.route('/test/')
def test():
    g.name = '张三'
    g.age = 18
    return render_template('test.html')
```

test.htmls

```html
<li>{{ g.name }}</li>
<li>{{ g.age }}</li>
```



#### (2) 使用 **locals()

manage.py

```python
def test():
    name = 'zhangsan'
    age = 18
    print(locals())
    return render_template('test.html',**locals())
```

test.html

```html
<li>{{ name }}</li>
<li>{{ age }}</li>
```

#### (3) 将传入字典

manage.py

```python
def test():
    myDict = {'name':'zhangsan','age':18}
    return render_template('test.html',**myDict)
```

test.html

```html
<li>{{ name }}</li>
<li>{{ age }}</li>
```

#### (4) 原始传参

```python
def test():
    return render_template('test.html',name='zhangsan',age=18)
```



## 十二、回顾url_for

```python
url_for('index') #只构造路由
url_for('index',_external=True) #构造完整的url链接地址
```

















 
























