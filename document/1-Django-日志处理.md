### 1  Django中加入日志功能



​     Django 中使用python的 logging 模块记录log，在 Django 中使用 Django 提供的配制方法。就是在 settings 中通过变量 LOGGING，LOGGING 是一个字典，典型的配置如下：

​      logging模块为应用程序提供了灵活的手段记录事件、错误、警告和调试信息。对这些信息可以进行收集、筛选、写入文件、发送给系统日志等操作，甚至还可以通过网络发送给远程计算机。



（1）日志记录级别

​    logging模块的重点在于生成和处理日志消息。每条消息由一些文本和指示其严重性的相关级别组成。级别包含符号名称和数字值。

| 级别     | 值   | 描述          |
| -------- | ---- | ------------- |
| CRITICAL | 50   | 关键错误/消息 |
| ERROR    | 40   | 错误          |
| WARNING  | 30   | 警告消息      |
| INFO     | 20   | 通知消息      |
| DEBUG    | 10   | 调试          |
| NOTSET   | 0    | 无级别        |



（2）记录器

​    记录器负责管理日志消息的默认行为，包括日志记录级别、输出目标位置、消息格式以及其它基本细节。

| 关键字参数 | 描述                                       |
| ---------- | ------------------------------------------ |
| filename   | 将日志消息附加到指定文件名的文件           |
| filemode   | 指定用于打开文件模式                       |
| format     | 用于生成日志消息的格式字符串               |
| datefmt    | 用于输出日期和时间的格式字符串             |
| level      | 设置记录器的级别                           |
| stream     | 提供打开的文件，用于把日志消息发送到文件。 |



（3）format 日志消息格式

| 格式           | 描述                               |
| -------------- | ---------------------------------- |
| %(name)s       | 记录器的名称                       |
| %(levelno)s    | 数字形式的日志记录级别             |
| %(levelname)s  | 日志记录级别的文本名称             |
| %(filename)s   | 执行日志记录调用的源文件的文件名称 |
| %(pathname)s   | 执行日志记录调用的源文件的路径名称 |
| %(funcName)s   | 执行日志记录调用的函数名称         |
| %(module)s     | 执行日志记录调用的模块名称         |
| %(lineno)s     | 执行日志记录调用的行号             |
| %(created)s    | 执行日志记录的时间                 |
| %(asctime)s    | 日期和时间                         |
| %(msecs)s      | 毫秒部分                           |
| %(thread)d     | 线程ID                             |
| %(threadName)s | 线程名称                           |
| %(process)d    | 进程ID                             |
| %(message)s    | 记录的消息                         |



（4）内置处理器

​    logging模块提供了一些处理器，可以通过各种方式处理日志消息。使用addHandler()方法将这些处理器添加给Logger对象。另外还可以为每个处理器配置它自己的筛选和级别。

​      handlers.DatagramHandler(host，port):发送日志消息给位于制定host和port上的UDP服务器。

​      * handlers.FileHandler(filename): 将日志消息写入文件filename。

​      handlers.HTTPHandler(host, url):使用HTTP的GET或POST方法将日志消息上传到一台HTTP 服务器。

​      * handlers.RotatingFileHandler(filename):将日志消息写入文件filename。如果文件的大小超出maxBytes制定的值，那么它将被备份为filename1。

​    由于内置处理器还有很多，如果想更深入了解。可以查看官方手册。



### 2  Django中使用日志

在Django的配置文件settings.py 中加入如下LOGGING配置

```
#########################
## Django Logging  BEGIN
#########################

#LOGGING_DIR 日志文件存放目录
LOGGING_DIR = "/home/xxt/logs"
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)

import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s][%(funcName)s][%(lineno)d] > %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s]> %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file_handler': {
             'level': 'INFO',
             'class': 'logging.handlers.TimedRotatingFileHandler',
             'filename': '%s/django.log' % LOGGING_DIR,
             'formatter':'standard'
        }, # 用于文件输出
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
             'formatter':'standard'
        },
    },
    'loggers': {
        'mdjango': {
            'handlers': ['console','file_handler'],
            'level':'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
	
logger = logging.getLogger("mdjango")

#########################
## Django Logging  END
#########################
```



最新日志内容存入：  django.log

前一天：django.log.2018-05-29

前前一天：django.log.2018-05-28



django.log.2018-05-22



在具体的业务逻辑代码中加入日志记录

```
from Project.settings import  logger
logger.info("IndexHandler request Handler begin")
logger.debug('query total:' + str(total))
```



观察日志打印情况。



一般python使用日志功能（非django框架）

```
import logging

def logging_init():
   app_name = "AppName"
   log_file_name = "myapp_test.log"
   logger = logging.getLogger(app_name)
   format_str = "[%(asctime)s][%(levelname)s]> %(message)s"
   formatter = logging.Formatter(format_str)
   file_handler = logging.FileHandler(log_file_name)
   file_handler.setFormatter(formatter)
   logger.addHandler(file_handler)
   logger.setLevel(logging.INFO)
   return logger

```

单例模式

```
import logging

class Singleton(object):
   _instance = None

   def __new__(cls, *args, **kwargs):
      if not cls._instance:
         cls._instance = super(Singleton, cls).__new__(cls,
                                    *args, **kwargs)
      return cls._instance
   
 
   

app_name = "appName"
log_file = "test.log"

class SingletonLogger(Singleton):

   def __init__(self):
      super(SingletonLogger, self).__init__()
      self.logger = logging.getLogger(app_name)
      format_str = "[%(asctime)s][%(levelname)s]> %(message)s"
      formatter = logging.Formatter(format_str)
      file_handler = logging.FileHandler(log_file)
      file_handler.setFormatter(formatter)
      self.logger.addHandler(file_handler)
      self.logger.setLevel(logging.INFO)

   def debug(self, data):
      self.logger.debug(data)

   def info(self, data):
      self.logger.info(data)

   def warning(self, data):
      self.logger.warning(data)


   def error(self, data):
      self.logger.error(data)


def test_log():
   logger = SingletonLogger()
   #output the log msg
   logger.debug("this is the debug message")
   logger.info("this is the info message")
   logger.warning("this is the warning message")
   logger.error("this is the error message")


```





