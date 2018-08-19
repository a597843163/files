## Flask课程介绍

flask第一天  flask入门

安装flask   完整的跑一下 cookie和session   蓝本   钩子函数

flask第二天

模板引擎   jinja2

flask第三天

表单

flask第4天

文件上传 与邮件发送

flask第5天

模型

flask第6-9天项目的开始   博客

flask第10天复习



## flask第一天

## 一、MVT的介绍

M         模型

V           视图

C	    控制器

T	   模板



## 二、WEB工作原理

1. B/S 架构    
2. C/S架构



## 三、flask框架

#### (1)  概念

flask是一个非常小的Python Web框架，被称为微型框架  只提供了一个强健的核心  其它功能都是通过第三方的扩展模块来实现   

#### (2) 组成

1. 调试  路由 WSGI
2. 模板引擎  jinja2

#### (3)  安装

pip install flask

pip3   install flask

sudo pip3 install flask

#### (4) 路由格式

@flask对象.route('/url地址/')

def 函数名([参数]):

​	pass

#### (5) 完整flask的运行

```python
from flask import Flask
#创建flask的应用
app = Flask(__name__)

#路由
@app.route('/')   #在请求当前路由的时候  如果当前路由需要/的时候 浏览器会自动将它补全
def index():
    print('<h1>Hello World</h1>')
    return 'FLask' #必须有相应给浏览器

if __name__ == '__main__':
    # print(app)
    app.run() #将当前的flask运行起来
```

> 浏览器测试  http://127.0.0.1:5000

#### (6) 启动参数

| 参数       | 说明                |
| -------- | ----------------- |
| host     | 指定主机名             |
| port     | 指定端口号             |
| debug    | 是否开启调试模式 默认是False |
| threaded | 是否开启多线程  默认False  |

**实例**

```python
if __name__ == '__main__':
    # print(app)
    app.run(host='0.0.0.0',port=5001,debug=True,threaded=True) #将当前的flask运行起来
```



## 四、视图函数

#### (1) 无参路由

**实例**

```python
@app.route('/test/')
def test():
    return '这是一个测试的视图函数'
```

>路由地址和视图函数名称   是否同名都没关系

#### (2) 带参路由

**实例**

```python
#带参路由   http://127.0.0.1:5001/welcome/lisi
@app.route('/welcome/<name>')
def welcome(name):
    print(type(name)) #接收的参数 name都为字符串类型
    return '欢迎{}'.format(name)
```

#### (3) 指定参数类型

**指定类型的种类**

1. str(默认)  字符串类型
2. int            整形
3. float        浮点型
4. path        路径

**实例**

```python
#int
@app.route('/argtype/<int:uid>')
@app.route('/argtype/<float:uid>')
@app.route('/argtype/<path:uid>')
def argtype(uid):
    print(type(uid))
    print(uid)
    return '参数类型'
```

#### (4) 多个参数

**实例**

````python
@app.route('/manyarg/<a>_<b>/')
@app.route('/manyarg/<a>/<b>/')
def manyarg(a,b):
    print(a,b)
    return '接收多个参数'
````

> `http://127.0.0.1:5001/manyarg/1_2`
>
> `http://127.0.0.1:5001/manyarg/1/2`

**注意**

1.  路由地址和视图函数名称   是否同名都没关系
2.  参数的类型默认都是字符串类型
3.  路由末尾的/建议都加上 因为在如果需要的时候 浏览器会自动帮你加上
4.  在参数限制类型的时候  path,int,float: 接收参数的名称
5.  路由中的参数类型限制path  其实也是字符串类型 只是将路由后面的/ 当成字符串  而不再是路由



## 五、路由响应

#### (1) 响应404状态码

```python
@app.route('/res/')
def res():
    return 'page not found',404 #可以指定返回请求的状态码
```

> 请求是成功的 但是你可以指定返回的请求状态码

#### (2) 通过make_response 构造响应

from flask import make_response

```python
@app.route('/res/')
def res():
    # return 'page not found',404 #可以指定返回请求的状态码
    # response = make_response('通过make_response进行的响应')
    response = make_response('通过make_response进行的响应',404)
    print(response)
    return response
```



## 六、redirect 重定向

**作用:** 可以直接通过通过重定向跳转到另外的路由

**导入:**

from flask import redirect

**实例**

```python
@app.route('/test/') #路由地址和视图函数 是否同名都没关系
def test():
    return redirect('/')  #通过redirect重定向给定的路由直接跳转
    return redirect('/welcome/lisi') #带参的重定向    @app.route('/welcome/<name>')
```

#### 使用url_for和redirect结合使用

url_for 通过视图函数反向构造出路由地址

##### 导入

from flask import url_for

**实例**

```python
@app.route('/test/') #路由地址和视图函数 是否同名都没关系
def test():
	print(url_for('index')) #url_for 通过视图函数名称 反向构造出路由
    print(url_for('argtype',uid='abc'))   #通过url_for反向构造出参数路由
    return redirect(url_for('argtype',uid='abc')) #redirect和url_for完整使用
    # return '这是一个测试的视图函数'
```



## 七、abort 终止

**概念：** abort函数可以返回一个http标准的状态码   表示出现的错误信息  abort后面的代码将不会在继续执行 类似于python中的raise

**实例**

```python
@app.route('/test/')
def test():
    abort(404) #抛出404的状态码  下面代码不会再执行
    return '不会再执行'
```

#### 错误页面的定制（捕获特定的状态码进行处理）

```python
@app.errorhandler(404) #捕获404的状态码的错误  可以捕获手动的abort和用户请求的404
def serverError(e): #接收flask传递给我当前的错误信息
    # return '<h1>Not Found</h1>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again'
    return e
```



## 八、请求与响应

#### (1)对象或者变量

| 对象/变量       | 上下文   | 说明                  |
| ----------- | ----- | ------------------- |
| current_app | 程序上下文 | 当前的应用实例             |
| g           | 程序上下文 | 处理请求的临时变量  每次请求都会重置 |
| request     | 请求上下文 | 请求对象 保存了所有的请求信息     |
| session     | 请求上下文 | 会话控制  保存会话信息        |

#### (2) app对象

全局应用对象

作用：可以将全局的配置添加到app对象上

```python
app.secret_key = '加密的字符'
```

#### (3) current_app对象

在视图的任何位置 都能够访问到全局对象 app  

通过current_app 访问或者获取app上的公共配置信息

```python
from flask import current_app
@app.route('/test/')
def test():
    return current_app.secret_key
```

#### (4) request  对象

作用：获取用户请求传递过来的数据

##### 概述：

浏览器发送到服务器所有数据 被flask接收后，会创建出request对象，request对象用在视图函数中 获取请求过来的数据

**导入：**

from flask import request

##### request的属性

1. url 请求的完整url
2. base_url    去掉get传参的路由
3. host_url    获取只有主机IP和端口号的url
4. path   获取路由地址
5. method    获取请求方法
6. args          获取通过get传递过来的参数
7. form        获取通过post  表单传递过来的数据
8. files          用于文件上传
9. cookies     存储请求的cookie
10. Json           获取传递过来的Json数据
11. headers    获取请求过来的头信息

**实例**

```python
@app.route('/request/')
def req():
    #http://127.0.0.1:5001/request/?name=lisi&age=18
    print('请求的完整url',request.url)
    print('去掉get传参的路由',request.base_url)
    print(' 获取只有主机IP和端口号的url',request.host_url)
    print(' 获取路由地址',request.path)
    print(' 获取请求方法',request.method)
    print(' 获取通过get传递过来的参数',request.args)
    print(' 获取通过get传递过来的参数',request.args['name'])
    print(' 用于文件上传',request.files)
    print(' 获取请求过来的头信息',request.headers['User-Agent'])
    return 'request对象的使用'
```

**注意：**

当传递过来的get传参出现了同名的key的时候 使用get只能获取到第一个值  需要使用getlist(key) 来获取当前同名的key的所有值

**实例**

```python
@app.route('/getarg/')
def getarg():
    #http://127.0.0.1:5001/getarg/?name=lisi&name=18
    print('name的值为:',request.args.get('name'))
    print('age的值为',request.args.get('age','你是不是傻？有age吗'))
    print('age的值为',request.args.getlist('name')) #[lisi,18]
    return '获取get传参'
```



## 九、会话控制 cookie和session

会话控制出现的原因

因为http是无状态的协议  需要每次都告诉服务器我是谁  使用cookie以后 每次拿着信息去像服务器进行请求

用来维护一个用户请求的状态

## cookie操作

### (1)设置cookie

```python
Response.set_cookie(
key, #设置cookie的键
value='', #设置当前键的存储值
max_age=None,  #以秒为单位的过期时间 单位都是秒 
expires=None,  #失效时间  单位都是秒
path='/' 	   #cookie的有效路径
)
```

**实例**

```python
#设置cookie的路由
@app.route('/set_cookie/')
def set_cookie():
    response = make_response('设置cookie') #创建response对象
    response.set_cookie('name','zhangsan') #设置cookie 过期为 当前会话结束（关闭浏览器就清除）
    # 一小时后过期
    expires = time.time()+3600
    response.set_cookie('name','zhangsan',expires=expires)
    response.set_cookie('age','18',max_age=3600) #
    return response
```

**注意：**

设置cookie的时候 如果没有设置过期时间 那么过期为 当前会话结束（关闭浏览器就清除）



### (2) 获取cookie

**实例**

```python
@app.route('/get_cookie/')
def get_cookie():
    return request.cookies.get('name','没有值')
```



### (3) 删除cookie

```python
@app.route('/del_cookie/')
def del_cookie():
    response = make_response('删除cookie')
    response.delete_cookie('age') #删除key为age的cookie
    return response 
```



## session

由于cookie对于存储信息不安全 所以重要的数据存储在 session  cookie只用来存储不重要的数据

使用session  存储于服务器端 在客户端的cookie中存储session的唯一ID  用来区分不同的请求者的所有存储数据

### (1) 设置session

导入session

from flask import session

**实例**

```python
@app.route('/set_session/')
def set_session():
    session['uid'] = 1
    return 'session设置成功'
```

### (2) 设置session并设置过期时间

```python
from datetime import timedelta
#设置session并设置过期时间
@app.route('/set_session/')
def set_session():
    session.permanent = True #设置session持久化
    app.permanent_session_lifetime = timedelta(minutes=5) #设置session的过期时间为5分钟    timedelta表示时间的差值
    session['key'] = 'value'
    return '设置了session的过期时间'
```

### (3) 获取session

```python
@app.route('/get_session/')
def get_session():
    # return '获取session的值为{}'.format(session['uid']) #获取key为uid的值
    # return '获取session的值为{}'.format(session['xxx']) #获取不存在的key keyError
    return '获取session的值为{}'.format(session.get('xxx'))
```

### (4) 删除session

```python
#删除session
@app.route('/del_session/')
def del_session():
    # session.pop('key') #删除某一个key的值
    # session.clear() #删除所有的session
    return '删除session键为key的值'
```



## 十、flask-script

**简介：** 是flask终端运行的解析器，因为在代码完成以后 就不应该对其有任何的修改，否则会带来风险 所以借助扩展库进行运行  通过传递参数 进行不同的启动项

**安装**

pip install flask-script

**实例**

```python
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)
if __name__ == '__main__':
    manager.run()
```

> 启动 python manage.py runserver

##### 启动参数

```python
-h  #帮助
-h  --host		#指定主机名
-p	--port		#端口号
--threaded		#开启多线程
-r				#代码修改后自动加载
-d				#调试模式
```

>python manage.py runserver -d -r
>
>python manage.py runserver -h127.0.0.1 -p5001 -d -r --threaded



## 十一、蓝本(蓝图)

**作用**: 将试图函数 进行按照功能的划分  存储在不同的文件中

**实例**

manage.py

```python
app = Flask(__name__)
manager = Manager(app)
from user import user
# app.register_blueprint(user) #注册蓝本 访问 127.0.0.1:5000/login
app.register_blueprint(user,url_prefix='/user') #注册蓝本 并添加当前蓝本的前缀  127.0.0.1:5000/user/login
```

user.py

```python
from flask import Blueprint
#实例化蓝本
# Blueprint('user',__name__) 中的user为当前蓝本的名称 在跳转的时候 需要指定是哪个蓝本的视图函数或者路由 那么当前的user就是起到这样的作用
user = Blueprint('user',__name__)
@user.route('/login/')
def login():
    return '登录处理'
```

##### manage.py与user.py中的重定向跳转

manage.py

```python
@app.route('/')
def index():
    return redirect(url_for('user.login'))
@app.route('/test/')
def test():
    return 'test函数'
```

user.py

```python
@user.route('/login/')
def login():
    return '登录处理'

@user.route('/register/')
def register():
    # return '注册处理'
    return redirect("/test/") #跳转到manage.py的test路由
```



## 十二、请求钩子函数

就是Django中的中间件

**主程序中使用(manage.py)** 以下都为装饰器 配合app来使用

| 钩子函数                 | 功能描述           |
| -------------------- | -------------- |
| before_first_request | 第一次请求之前        |
| before_request       | 每次请求之前         |
| after_request        | 每次请求之后 前提是没有异常 |
| teardown_request     | 每次请求之后 即使有异常   |

**蓝本中使用** 以下都为装饰器

| 钩子函数                     | 功能描述           |
| ------------------------ | -------------- |
| before_app_first_request | 第一次请求之前        |
| before_app_request       | 每次请求之前         |
| after_app_request        | 每次请求之后 前提是没有异常 |
| teardown_app_request     | 每次请求之后 即使有异常   |




**在主程序中实例**

```python
@app.route('/form/')
def form():
    return 'form表单'


from user import user
# app.register_blueprint(user) #注册蓝本
app.register_blueprint(user,url_prefix='/user') #注册蓝本 并添加当前蓝本的前缀


@app.before_first_request
def before_first_request():
    print('before_first_request')

@app.before_request
def before_request():
    if request.method == 'GET' and request.path == '/form/':
        abort(404)
    print(request.path)
    # print('before_request')

@app.after_request
def after_request(response):
    print('after_request')
    return response
@app.teardown_request
def teardown_request(response):
    print('teardown_request')
```

**在蓝本中实例**

```python
user = Blueprint('user',__name__)
@user.before_app_request
def before_request():
    if request.method == 'GET' and request.path == '/form/':
        abort(404)
    print(request.path)
    # print('before_request')
```





























































