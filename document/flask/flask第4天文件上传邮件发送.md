# 文件上传 与 邮件发送

## 一、文件上传

#### (1) 原生文件上传 

manage.py 

```python
from flask import send_from_directory
import os,string,random

#当前文件是否允许
def allowedFile(shuffix):
    extensions = shuffix.strip('.')
    return extensions in ALLOWED_EXTENSIONS

#生成随机的图片名称 数字+字母随机数
#shuffix 为图片的后缀
#length 为当前图片的名字的长度
def randomName(shuffix,length=32):
    myStr = string.ascii_letters+'0123456789'
    # print(myStr)
    newName = ''.join(random.choices(myStr,k=length))+shuffix
    return newName

#自定义路由 获取图片的显示
@app.route('/get_url/<filename>')
def getUrl(filename):
    return send_from_directory(app.config['UPLOAD_FLODER'],filename)

#文件上传的路由
@app.route('/upload/',methods=['GET','POST'])
def upload():
    # print(request.files)
    img_url = None
    if request.method == 'POST':
        file = request.files.get('file') #获取上传的文件
        shuffix = os.path.splitext(file.filename)[-1] #获取文件的后缀
        if allowedFile(shuffix):
            newName = randomName(shuffix) #生成随机图片名
            #拼凑出保存的路径
            newPath = os.path.join(app.config['UPLOAD_FLODER'],newName) #获取图片生成的新的图片名称
            # print(newName)
            file.save(newPath) #图片保存
            img_url = url_for('getUrl',filename=newName) #获取图片的地址
    return render_template('upload.html',img_url=img_url)
```

upload.html

```html
    {% if img_url %}
        <img src="{{ img_url }}" alt="">
    {% endif %}
    <form action="{{ url_for('upload') }}" method="post" enctype="multipart/form-data">
        <p>选择文件:</p>
        <p><input type="file" name="file"></p>
        <p><input type="submit" value="submit"></p>
    </form>
```

**注意事项：**

1. 表单的设置  是否为post  input type=file 是否有name名称  enctype的值是否修改
2. 视图函数 methods是否设置为POST  
3. 上传文件的大小是否超出范围

### (2) flask-uploade   文件上传第三方扩展库

**安装:** pip install flask-uploads

#### 安装图片处理模块 pillow

##### pip install pillow

使用 from PIL import Image



**实例**

manage.py

```python
from flask import Flask,render_template,request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
import os
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*64
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+'/static/upload'

file = UploadSet('photos',IMAGES)
configure_uploads(app,file)
patch_request_class(app,size=None) #将第三方上传大写设置为 app.config['MAX_CONTENT_LENGTH']的大小
manager = Manager(app)


@app.route('/upload/',methods=['GET','POST'])
def upload():
    img_url = None
    #判断是否为表单提交 并且是点击图片并且上传的提交
    if request.method == 'POST' and 'file' in request.files:
        print(request.files)
        fileName = file.save(request.files.get('file')) #文件保存
        print(fileName)
        img_url = file.url(fileName)
    return render_template('upload.html',img_url=img_url)


if __name__ == '__main__':
    manager.run()
```

**在manage.py中处理图片缩放**

```python
fileName = file.save(request.files.get('file')) #文件保存
# print(fileName)

#进行图片缩放处理
imgPath = os.path.join(app.config['UPLOADED_PHOTOS_DEST'],fileName)
img = Image.open(imgPath) #打开图片
img.thumbnail((300,300)) #生成缩略图
# img.save(imgPath) #保存并覆盖原图
img.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'],'s_'+fileName)) #保存并覆盖原图
# print(fileName)
#需求 大图和小图都需要 但是数据库存储图片只有一个字段 应该怎样存储或者操作？
img_url = file.url('s_'+fileName) #获取图片的地址
```

### (3) 完整的文件上传

```python
from flask import Flask,render_template,request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
import string, random,os
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import SubmitField

from PIL import Image #导入图片处理模块
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*64
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+'/static/upload'
app.config['SECRET_KEY'] = 'abcdef'
file = UploadSet('photos',IMAGES)
configure_uploads(app,file)
patch_request_class(app,size=None) #将第三方上传大写设置为 app.config['MAX_CONTENT_LENGTH']的大小
manager = Manager(app)

class fileUpload(FlaskForm):
    file = FileField('头像上传',validators=[FileRequired(message='您还没有选择文件'),FileAllowed(file,message='只允许上传图片')])
    submit = SubmitField('开始上传')

def randomName(shuffix,length=32):
    myStr = string.ascii_letters+'0123456789'
    # print(myStr)
    newName = ''.join(random.choices(myStr,k=length))+shuffix
    return newName

@app.route('/upload/',methods=['GET','POST'])
def upload():
    form = fileUpload()
    img_url = None
    if form.validate_on_submit():
        print('请求过来了')
        # 1. 获取文件名字 并拿到文件扩展名
        shuffix = os.path.splitext(form.file.data.filename)[-1]
        #2. 生成文件的随机名称
        newName = randomName(shuffix)
        #3. 保存上传文件
        # file.save(app.config['UPLOADED_PHOTOS_DEST'],newName)
        file.save(form.file.data,name=newName)
        #4. 生成文件缩略图
        img = Image.open(os.path.join(app.config['UPLOADED_PHOTOS_DEST'],newName))
        img.thumbnail((300,300))
        img.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'],'s_'+newName))
        #5. 获取图片url 传递并显示
        img_url = file.url(newName)
    return render_template('wtform.html',form=form,img_url=img_url)
```

#### form表单

```html
{% import 'bootstrap/wtf.html' as wtf %}
{% block page_content %}
    <img src="{{ img_url }}" alt="">
    {{ wtf.quick_form(form) }}
{% endblock %}
```





## 二、邮件发送 flask-mail

**安装:**  pip install flask-mail

### (1) 单线程的邮件发送

```python
from flask import Flask
from flask_script import Manager
from flask_mail import Mail,Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.1000phone.com')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','xialigang@1000phone.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','123456')

mail = Mail(app)
manager = Manager(app)

@app.route('/')
def index():
    msg = Message(subject='学校通知下午不上课',recipients=['793390457@qq.com'],sender=app.config['MAIL_USERNAME'])
    msg.html = '<h1>今天是一个号节日 愚人节</h1>'
    mail.send(message=msg)
    return '邮件发送'

if __name__ == '__main__':
    manager.run()
```

### (2) 多线程的邮件发送

```python
from flask import Flask,render_template
from flask_script import Manager
from flask_mail import Mail,Message
from threading import Thread #导入线程模块
import os
app = Flask(__name__)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.1000phone.com')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','xialigang@1000phone.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','123456')

mail = Mail(app)
manager = Manager(app)
#线程执行干的活
def async_send_mail(app,msg):
    #程序上下文
    with app.app_context():
        mail.send(message=msg)

def send_mail(subject,to,username):
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])
    msg.html = render_template('active.html',username=username)
    # 第一个参数为 让当前线程干活的函数  第二个为传参 需要元组形式
    send = Thread(target=async_send_mail,args=(app,msg))
    send.start() #开启线程

@app.route('/')
def index():
    send_mail('邮件激活','793390457@qq.com','张三')
    return '邮件发送成功'


if __name__ == '__main__':
    manager.run()
```

active.html

```html
<h1>{{username}}你好 邮件激活</h1>
<h2>请点击右侧的激活码 进行当前激活的操作...</h2>
```



