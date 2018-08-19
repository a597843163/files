## Django集成Celery到项目



​    本节将celery集成到Django项目中，实现异步任务处理和定时任务处理



#### 1  Celery安装与配置  

在虚拟环境中安装:

  pip install django-celery==3.2.2

  pip install  redis

  pip install flower

查看集成到Django中的celery版本， pip  freeze

 celery==3.1.26.post2      django-celery==3.2.2    flower==0.9.2



启动redis服务， 端口假设为6379

发现pip安装比较慢的情况

pip  install pillow  -i  https://pypi.douban.com/simple    



### 2  Django中配置

（1）在主工程的配置文件settings.py 中应用注册表INSTALLED_APPS中加入 djcelery

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'art',
    'xadmin',
    'crispy_forms',
    'DjangoUeditor',
    'djcelery',       #加入djcelery
]
```



(2) 在settings.py 中加入celery配置信息

```
#############################
# celery 配置信息 start
#############################
import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_IMPORTS = ('art.tasks')
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' 
from celery.schedules import crontab
from celery.schedules import timedelta

CELERYBEAT_SCHEDULE = {    #定时器策略
    #定时任务一：　每隔30s运行一次
    u'测试定时器1': {
        "task": "art.tasks.tsend_email",
        #"schedule": crontab(minute='*/2'),  # or 'schedule':   timedelta(seconds=3),
        "schedule":timedelta(seconds=30),
        "args": (),
    },
}
#############################
# celery 配置信息 end
#############################
```

​      当djcelery.setup_loader()运行时，Celery便会去查看INSTALLD_APPS下包含的所有app目录中的tasks.py文件，找到标记为task的方法，将它们注册为celery task

​     BROKER_URL：broker是代理人，它负责分发任务给worker去执行。我使用的是Redis作为broker

​    没有设置 CELERY_RESULT_BACKEND，默认没有配置，此时Django会使用默认的数据库(也是你指定的orm数据库)。

   CELERY_IMPORTS：是导入目标任务文件

   CELERYBEAT_SCHEDULER：使用了django-celery默认的数据库调度模型,任务执行周期都被存在默认指定的orm数据库中．

  CELERYBEAT_SCHEDULE：设置定时的时间配置， 可以精确到秒，分钟，小时，天，周等。



（3）创建应用实例

​      在主工程目录添加celery.py， 添加自动检索django工程tasks任务

​     vim  artproject/celery.py

```
#!/usr/bin/env python  
# encoding: utf-8  
#目的是拒绝隐士引入，celery.py和celery冲突。
from __future__ import absolute_import,unicode_literals 
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "artproject.settings")

#创建celery应用
app = Celery('art_project')
#You can pass the object directly here, but using a string is better since then the worker doesn’t have to serialize the object.
app.config_from_object('django.conf:settings')
#如果在工程的应用中创建了tasks.py模块，那么Celery应用就会自动去检索创建的任务。比如你添加了一个任#务，在django中会实时地检索出来。
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)
```



(4) 创建任务 tasks

每个任务本质上就是一个函数，在tasks.py中，写入你想要执行的函数即可。

在应用art中添加我们需要提供的异步服务和定时服务 

 vim art/tasks.py

```
#!/usr/bin/env python  
# encoding: utf-8  
from __future__ import absolute_import
import time
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from artproject.celery import app

from art.utils.send_mail import pack_html, send_email

@app.task
def tsend_email():
   url = "http://1000phone.com"
   receiver = 'diyuhuan@1000phone.com'
   content = pack_html(receiver, url)
   # content = 'this is email content.'
   send_email(receiver, content)
   print('send email ok!')


@app.task
def add(x, y):
   return x+y

```

   上述我们把异步处理任务add和定时器任务tsend_email都放在了tasks.py 中





（5）迁移生成celery需要的数据表

####    python   manage.py   migrate

  此时数据库表结构多出了几个

```
celery_taskmeta            |
| celery_tasksetmeta         |
| djcelery_crontabschedule   |
| djcelery_intervalschedule  |
| djcelery_periodictask      |
| djcelery_periodictasks     |
| djcelery_taskstate         |
| djcelery_workerstate 
```



### 3  启动服务，测试

  我们可以采用 python manage.py  help  发现多出了 celery 相关选项。 

（1）启动django celery 服务

  启动服务：

  python manage.py  celery   worker    --loglevel=info

  此时异步处理和定时处理服务都已经启动了



（2）web端接口触发异步任务处理

我们在web端加入一个入口，触发异步任务处理add函数 

在应用art的urls.py 中加入如下对应关系

```
from art.views import add_handler


url(r'^add', add_handler),
```



art/views.py 中加入处理逻辑

```
def add_handler(request):
   x = request.GET.get('x', '1')
   y = request.GET.get('y', '1')
   from .tasks import add
   add.delay(int(x), int(y))
   res = {'code':200, 'message':'ok', 'data':[{'x':x, 'y':y}]}
   return HttpResponse(json.dumps(res))
```



启动web服务，通过url传入的参数，通过handler的add.delay(x, y)计算并存入mysql



http://127.0.0.1:8000/art/add?x=188&y=22



(4)  测试定时器，发送邮件

在终端输入  python manage.py celerybeat -l info

会自动触发每隔30s执行一次tsend_email定时器函数，发送邮件：

```
CELERYBEAT_SCHEDULE = {    #定时器策略
    #定时任务一：　每隔30s运行一次
    u'测试定时器1': {
        "task": "art.tasks.tsend_email",
        #"schedule": crontab(minute='*/2'),  # or 'schedule': timedelta(seconds=3),
        "schedule":timedelta(seconds=30),
        "args": (),
    },
}
```

具体发送邮件服务程序见下面的第4节



### 4   邮件发送服务

项目中经常会有定时发送邮件的情形，比如发送数据报告，发送异常服务报告等。

可以编辑文件 art/utils/send_mail.py, 内容编辑如下：

```
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#written by diyuhuan
#发送邮件(wd_email_check123账号用于内部测试使用，不要用于其他用途)

import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage 
from email.header import Header
import time

sender = 'wd_email_check123@163.com'  
subject = u'api开放平台邮箱验证'
smtpserver = 'smtp.163.com'
username = 'wd_email_check123'
password = 'wandacheck1234'
mail_postfix="163.com"

def send_email(receiver, content):
    try:
        me = username+"<"+username+"@"+mail_postfix+">"
        msg = MIMEText(content, 'html', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        smtp = smtplib.SMTP()  
        smtp.connect(smtpserver)  
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())  
        smtp.quit()
        return True
    except Exception as e:
        print('send_email has error with : ' + str(e))
        return False


def pack_html(receiver, url):
    html_content = u"<html><div>尊敬的用户<font color='#0066FF'>%s</font> 您好！</div><br>" \
                   "<div>感谢您关注我们的平台 ，我们将为您提供最贴心的服务，祝您购物愉快。</div><br>" \
                   "<div>点击以下链接，即可完成邮箱安全验证：</div><br>"  \
                   "<div><a href='%s'>%s</a></div><br>"  \
                   "<div>为保障您的帐号安全，请在24小时内点击该链接; </div><br>" \
                   "<div>若您没有申请过验证邮箱 ，请您忽略此邮件，由此给您带来的不便请谅解。</div>" \
                   "</html>" % (receiver, url, url)
    html_content = html_content
    return html_content


if __name__ == "__main__":
    url = "http://1000phone.com"
    receiver = 'diyuhuan@1000phone.com'
    #content = pack_html(receiver, url)
    content = 'this is email content. at %s.'%int(time.time())
    send_email(receiver,  content)
```



至此，在celery ui界面可以看到两类，定时器处理和异步处理。





###  5   启动flower服务

​	python manager celery flower







