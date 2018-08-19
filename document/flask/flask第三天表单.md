# Flask 表单

## 一、原生表单

#### (1) 表单路由

```python
@app.route('/login/')
def login():
    return render_template('pform.html')

#验证表单
@app.route('/check_form/',methods=['GET','POST'])
def checkForm():
    print(request.form)
    return '提交表单的地址'
```

#### (2) form表单

```python
<form action="{{ url_for('checkForm') }}" method="get">
        <p>用户名 <input type="text" name="username"></p>
        <p>密码 <input type="password" name="userpass"></p>
        <p>
            <input type="submit" value="submit">
            <input type="reset" value="reset">
        </p>
    </form>
```

#### (3) 将俩个路由合并为同一个

```python
#将表单的俩个路由合并为一个路由
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('pform.html')
    else:
        return 'name 为{} age为{}'.format(request.form.get('username'),request.form.get('userpass'))
```



##### 注意：

1. 表单提交 提交方式只能为 post 否则request.form获取不到数据
2. 如果使用get提交 name获取参数的方式 request.args
3. 如果提交方式改为post 则路由需要添加允许访问的post方式 methods=['GET','POST']





## 二、flask-wtf  flask第三方表单扩展库

**概述：** 是一个用于表单处理的扩展库 提供了csrf、校验等功能

#### (1) 安装

pip install flask-wtf

#### (2) 常见字段类型 和 验证器

#### 字段类型

| 字段类型          | 字段说明                      |
| ------------- | ------------------------- |
| StringField   | 文本字段                      |
| SubmitField   | 提交按钮                      |
| PasswordField | 密码字段                      |
| HiddenField   | 隐藏字段                      |
| TextAreaField | 多行文本域字段                   |
| DateField     | 文本字段 datetime.date 格式     |
| DatetimeField | 文本子弹 datetime.datetime 格式 |
| InterField    | 文本字段 整形                   |
| FloatField    | 文本字段 浮点型                  |
| BooleanFIeld  | 复选框  值为True或者False        |
| RadioField    | 单选框                       |
| SelectField   | 下拉框                       |
| FileField     | 文件上传                      |

####  验证器

| 验证器          | 说明                 |
| ------------ | ------------------ |
| DataRequired | 必填字段               |
| Email        | 验证邮箱               |
| URL          | 验证是否为正确的url地址      |
| IPAddress    | IP地址               |
| Length       | 限制内容的长度 有min 和 max |
| NumberRange  | 数值的范围              |
| EqualTo      | 验证俩个字段值是否一致性       |
| Regexp       | 正则验证               |

#### **实例**

manage.py

```python
from flask_wtf import FlaskForm #导入需要自定义表单类的基类
#导入表单字段
from wtforms import StringField,PasswordField,SubmitField
#导入验证器
from wtforms.validators import DataRequired,Length


class MyForm(FlaskForm):
    #用户名为 label内的内容作为显示 username为当前input 的name名称 validators为存放验证器的关键字
    username = StringField('用户名',validators=[DataRequired(message='此字段为必填字段')])
    userpass = PasswordField('密码',validators=[DataRequired(message='必填字段'),Length(min=6,max=12,message='输入内容的长度为6~12位')])
    submit = SubmitField('登录')
    
@app.route('/login/')
def login():
  form = MyForm() #实例化自定义表单类
    if form.validate_on_submit(): #进行表单数据正确性和csrf的校验  表单正确结果为真 否则为假
        print(request.form.get('username'))
        print(request.form.get('userpass'))
    return render_template('login.html',form=form)
```

##### login.html

```html
<form action="{{ url_for('login') }}" method="post">
        {{ form.csrf_token }}  {# csrf隐藏域 #}
        <p>{{ form.username.label() }}</p>  {# 输入wtf表单内的username的label #}
{#        <p>{{ form.username() }}</p> {# 输出input #}
        <p>{{ form.username(style="color:red;",placeholder="请输入用户名...") }}
            {% if form.userpass.errors %}
                <span style="color:red">{{ form.username.errors }}</span>
            {% endif %}
        </p> {# 给当前username字段的标签添加html属性和值 #}
        <p>{{ form.userpass.label() }}</p>
        <p>{{ form.userpass() }}
            {% if form.userpass.errors %}
                <span style="color:red">{{ form.userpass.errors }}</span>
            {% endif %}
        </p>
        {{ form.submit }} {# 输出submit #}
</form>
```

#### 使用flask-bootstrap快速渲染

manage.py

```python
class MyForm(FlaskForm):
    #用户名为 label内的内容作为显示 username为当前input 的name名称 validators为存放验证器的关键字
    username = StringField('用户名',validators=[DataRequired(message='此字段为必填字段')],render_kw={'placeholder':'请输入用户名...'})
    
render_kw 给bootstrap渲染模板时 给标签添加属性和值的 
```

login.html

```html
{% extends 'common/base.html' %}
{% block title %}原生表单{% endblock %}
{% import 'bootstrap/wtf.html' as wtf %}
{% block page_content %}
    {{ wtf.quick_form(form,action=url_for('login')) }}
{% endblock %}
```

#### (3) 自定义验证器

```python
class MyForm(FlaskForm):
    #用户名为 label内的内容作为显示 username为当前input 的name名称 validators为存放验证器的关键字
    username = StringField('用户名',validators=[DataRequired(message='此字段为必填字段')],render_kw={'placeholder':'请输入用户名...'})

    # userpass = PasswordField('密码',validators=[DataRequired(message='必填字段'),Length(min=6,max=12,message='输入内容的长度为6~12位')])
    userpass = PasswordField('密码',validators=[DataRequired(message='必填字段')])
    submit = SubmitField('登录')

    #自定义验证器
    def validate_userpass(self,field):
        length = len(field.data)
        if length<6 or length>12:
            raise ValidationError('密码的内容在6-12位之间！！！')
```

#### (4) 在视图函数中获取表单中值的方式

```python
@app.route('/login/',methods=['GET','POST'])
def login():
    form = MyForm() #实例化自定义表单类
    if form.validate_on_submit(): #进行表单的校验  表单正确结果为真 否则为假
        # print(request.form.get('username'))
        # print(request.form.get('userpass'))
        print(form.username.data)
        print(form.userpass.data)
    # return render_template('login.html',form=form)
    return render_template('bootstrapLogin.html',form=form)
```



## 三、flash消息的显示

#### (1) 说明

当用户进行请求后，需要给出用户的提示或者警示信息的时候通过flash进行消息的传递   当然也可以通过手动来传递

#### (2) 用到的方法

1. flash 传入消息
2. get_flashed_messages()  获取消息（列表）

#### (3) 实例

manage.py

```python
@app.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data != 'zhangsan':
            flash('请输入正确的用户名')
        elif form.userpass.data != '123456':
            flash('密码不正确')
        else:
            flash('登录成功 欢迎{}'.format(form.username.data))
            return redirect(url_for('index')) #登录成功 跳转到首页
    return render_template('login.html',form=form)
```

login.html

```html
{#    {% if get_flashed_messages() %}#}
{#  get_flashed_messages().0 取出列表中的第一条数据 #}
    {% for message in  get_flashed_messages() %}
    <div class="alert alert-danger alert-dismissible" role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                aria-hidden="true">&times;</span></button>
        <strong>Warning!</strong>     {{ message }}
    </div>
    {% endfor %}

    {{ wtf.quick_form(form) }}
```



## 四、flask-moment  时间的显示

**说明：** 负责本地时间的格式化显示

**安装：** pip install flask-moment

**使用**

manage.py

```python
from flask_moment import Moment #导入格式化时间的扩展库
from datetime import datetime,timedelta
@app.route('/')
def index():
    current_time = datetime.utcnow()+timedelta(seconds=-3600)
    return render_template('index.html',current_time=current_time)
```

index.html

```html
    <p>LLLL时间: {{ moment(current_time).format('LLLL') }}</p>
    <p>LLL时间: {{ moment(current_time).format('LLL') }}</p>
    <p>LL时间: {{ moment(current_time).format('LL') }}</p>
    <p>L时间: {{ moment(current_time).format('L') }}</p>
    <p>自定义格式化: {{ moment(current_time).format('YYYY-MM-DD') }}</p>
    <p>发布于: {{ moment(current_time).fromNow() }}</p>
        {#  加载moment jquery代码  #}
    {{ moment.include_jquery() }}
        {#  加载moment js代码  #}
    {{ moment.include_moment() }}
    {#    格式化成中文#}
    {{ moment.locale('zh-CN') }}
```

格式化时间的网址：http://momentjs.com/（不需要记 但是要回找到答案）





