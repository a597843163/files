## 用户注册登陆

## 一、注册

1. 路由视图函数
2. wtf注册表单
3. models 模型
4. 生成迁移文件
5. 配置email

#### (1) 在将base模板导入进来 放在 templates下的common目录中 将注册 修改为当前的路由

```python
<li><a href="{{ url_for('user.register') }}">注册</a></li>
```

#### (2) 配置wtf的注册表单 在forms下创建一个user.py

```python
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,EqualTo
class Register(FlaskForm):
    """
    用户名   密码 确认密码 输入邮箱 点击注册
    """
    username = StringField('用户名',validators=[DataRequired(message='用户名不能为空'),Length(min=6,max=12,message='用户名长度为6-12位')])
    password = PasswordField('密码',validators=[DataRequired(message='密码不能为空'),Length(min=6,max=10,message='密码长度为6-10位')])
    confirm = PasswordField('确认密码',validators=[DataRequired(message='确认密码不能为为空'),EqualTo('password',message='密码和确认密码不一致')])
    #如果想让密码 或者用户名 输入多大的长度就不能在输入了 去查一下input属性 size
    email = StringField('邮箱',validators=[DataRequired(message="邮箱不能为空"),Email(message='请输入正确的邮箱')])
    submit = SubmitField('注册')
```

在forms目录下创建init文件作为当前form包的初始化

```python
from .user import Register
```

#### (3) 配置路由 在views 下创建user.py 创建register视图

```python
from flask import Blueprint,render_template,flash,get_flashed_messages
from app.forms import Register #导入表单注册wtf
from app.models import User #导入用户模型
from app.extensions import db
from app.email import send_mail

user = Blueprint('user',__name__)
@user.route('/register/',methods=['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        """
        1.导入用户的model 实例化
        2.保存数据到表 #在user模型中 写一个装饰器 直接将密码机密成hash写入到表中
        3.发送激活账户的邮件
        4.使用flash 提醒激活成功
        5.写一个路由 处理激活的操作
        6.跳转到登陆页
        """
        u = User(username=form.username.data,password=form.password.data,email=form.email.data)
        db.session.add(u)
        #只有当前视图执行完毕才会去提交添加 我下面的邮件的token验证 需要用户当前的id  所以要立即添加成功 并发挥获取到当前用户的id
        db.session.commit()
        token = u.generate_activate_token()#生成激活邮件的token
        send_mail('邮件激活',u.email,username=u.username,token=token) #发送激活邮件
        flash("账户注册成功 请前往邮箱中点击最后一步的操作 激活")
        return render_template('user/login.html')
    return render_template('user/register.html',form=form)
```

#### (4) 创建用户 model 在models目录下创建user.py

```python
from app.extensions import db
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serialize
from flask import current_app
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),unique=True)
    password_hash = db.Column(db.String(128))
    age = db.Column(db.Integer)
    sex = db.Column(db.Boolean,default=True)
    email = db.Column(db.String(50))
    icon = db.Column(db.String(80),default='default.jpg')
    confirm = db.Column(db.Boolean,default=False) #激活的字段 默认False没激活
    #密码的处理
    @property
    def password(self):
        raise AttributeError('password属性不可读')
    @password.setter
    def password(self,password):
        #将传入进来的密码直接变成加密的 传给密码属性
        self.password_hash = generate_password_hash(password)
    #生成激活的token
    def generate_activate_token(self):
        s = Serialize(current_app.config['SECRET_KEY'])
        return s.dumps({'id':self.id})
```

### (5) 激活

models中的代码

```python
#定义一个方法 去验证 并实现激活的方法
    @staticmethod
    def check_token(token):
        s = Serialize(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token) #反向序列化出字典
        except:
            return False
        u = User.query.get(data['id']) #通过字典拿到要激活的用户对象
        if not u: #判断用户是否存在
            return False

        if not u.confirm: #判断是否已经激活过  如果没有则激活
            u.confirm = True
            db.session.add(u)
        return True
```

激活的路由

```python
@user.route('/activate/<token>')
def activate(token):
    #完成 路由的激活
    if User.check_token(token):
        flash('账户激活成功')
        return redirect(url_for('user.login'))
    else:
        flash('账户激活失败')
        return redirect(url_for('main.index'))
```



## 二、登陆

### (1) 登录的表单

```python
#用户登陆的表单
class Login(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(message='用户名不能为空')])
    password = StringField('密码',validators=[DataRequired(message='密码不能为空')])
    submit = SubmitField('登录')
```

### (2) 登录在 user.model中 验证密码的方法

```python
 #验证密码
 def check_password(self,password):
     return check_password_hash(self.password_hash,password)
```

### (3) 登录的路由

```python
from flask_login import login_user,logout_user,login_required,current_user
@user.route('/login/',methods=["GET","POST"])
def login():
    #pip install flask-login
    form = Login()
    if form.validate_on_submit():
        u = User.query.filter(User.username==form.username.data).first()
        if not u:
            flash('当前用户不存在')
        elif not u.confirm:
            flash('当前用户未激活 请前去激活')
        elif  u.check_password(form.password.data):
            flash('欢迎{} 登录成功！'.format(u.username))
            login_user(u)
            return redirect(url_for('main.index'))
    return render_template('user/login.html',form=form)
```

### (4) flask-login的配置

extension.py中的配置

```python
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
#指定登陆的端点
login_manager.login_view = 'user.login'
#指定登录的提示信息
login_manager.login_message = '您还没有登录 请先登录在访问'
#设置session的保护级别  None,basic基本的  strong 只要当前的服务 登录状态时 出现任何的问题或者异常 都会自动退出当前的用户
login_manager.session_protection = 'strong'
```

在user.model中的配置

```python
from flask_login import UserMixin
class User(UserMixin,db.Model):
    pass

#登录认证的回掉函数  必须存在  不在 直接运行就报错
@login_manager.user_loader
def user_loader(uid):
    return User.query.get(int(uid))
```

### (5) 退出登录

```python
#退出
@user.route('/logout/')
def logout():
    logout_user()
    flash('退出成功')
    return redirect(url_for("main.index"))
```



**作业**

1. 显示用户的信息
2. 修改密码（使用邮箱）
3. 添加如果用户 注册了但是 没有激活的入口
4. 修改邮箱
5. 上传头像