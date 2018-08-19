#day 01 hello django
1. ##### **创建虚拟环境**(virtualenv 和virtualenvwrapper)

  1.1, virtualenv的概述

  ```python
  virtualenv是用来创建Python的虚拟环境的库，虚拟环境能够独立于真实环境存在，并且可以同时有多个互相独立的Python虚拟环境，每个虚拟环境都可以营造一个干净的开发环境，对于项目的依赖、版本的控制有着非常重要的作用。

  虚拟环境有什么意义？
  	如果我们要同时开发多个应用程序，应用A需要Django1.11，而应用B需要Django1.8怎么办？
  	这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。
  	virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。
  ```

  1.2, virtualenv 的安装和使用
  	1.2.1,安装和创建virtualenv
  		a,安装虚拟环境：安装virtualenv跟安装一般的Python库是一样的操作，直接使用pip命令就行了：
  				pip install virtualenv
  		b,创建虚拟环境：安装完成之后就可以使用virtualenv的命令来创建虚拟环境了，
  			  首先需要进入需要创建虚拟环境的文件夹，比如F盘的envs文件夹，
  			  然后使用以下命令创建一个虚拟环境，python版本的路径是可选的：
  				virtualenv 虚拟环境名称 [-p python版本的路径]
  				如：virtualenv env1 
  	1.2.2,启动虚拟环境:
  			env1\Scripts\activate
  		进入虚拟环境后：
  			使用pip安装numpy模块
  			创建test.py文件,并在文件中使用numpy模块
  			在cmd命令窗口使用python test.py执行文件
  			
  ```python
  1.2.3,退出虚拟环境(进入真实系统环境): 
  		deactivate  
  		(如果报错则使用:env1\Scripts\deactivate)
  	退出虚拟环境后再执行test.py：
  		在cmd命令窗口使用python test.py执行文件
  ```


  1.3, virtualenvwrapper 的安装和使用（virtualenvwrapper是virtualenv的包装版，以后用这个，更加方便）
  	Windows: pip install virtualenvwrapper-win
  	(Linux：pip install virtualenvwrapper)
  	
  	创建:mkvirtualenv    虚拟环境名称  -p  python的路径 
  	删除:rmvirtualenv    虚拟环境名称
  	(注意：创建的虚拟环境放在用户目录下的Envs中)
  	
  	进入:workon 虚拟环境名称
  	退出:deactivate 

  1.4, pip常用命令

  ```python
  	pip install xxx:安装xxx依赖包
  	pip list:查看所有依赖包
  	pip freeze:查看虚拟环境新安装的包
  	pip uninstall xxx ：卸载xxx包
  ```

  课堂练习：分别为python2.7和python3.6创建虚拟环境 。

  

2. ##### 安装django

  安装Django:  **pip install django**（也可指定某一版本 **pip install django==1.11**）

  测试Django是否安装成功

  进入python环境
  	import django
  	django.get_version()
  课堂练习：在上一步创建的虚拟环境中分别安装django。

  ​

3. ##### 创建一个Django项目

  进入到指定要存放项目的目录，执行 **django-admin startproject xxx**  来创建一个名字为xxx的工程

  查看默认目录结构

  ```python
  manage.py:是Django用于管理本项目的命令行工具，之后进行站点运行，数据库自动生成等都是通过本文件完成。
  HelloDjango/__init__.py告诉python该目录是一个python包，暂无内容，后期一些工具的初始化可能会用到
  HelloDjango/settings.py Django项目的配置文件，默认状态其中定义了本项目引用的组件，项目名，数据库，静态资源等。
  HelloDjango/urls.py 维护项目的URL路由映射，即定义当客户端访问时由哪个模块进行响应。
  HelloDjango/wsgi.py 定义WSGI的接口信息，主要用于服务器集成，通常本文件生成后无需改动。
  ```

  ​

4. ##### 测试服务器的启动

  **python manage.py runserver [ip:port]**

  ```python
  可以直接进行服务运行 默认执行起来的端口是8000
  也可以自己指定ip和端口：
  监听机器所有可用 ip （电脑可能有多个内网ip或多个外网ip）：python manage.py runserver 0.0.0.0:8000 
  如果是外网或者局域网电脑上可以用其它电脑查看开发服务器，访问对应的 ip加端口，比如 10.36.132.2:8000
  浏览器访问:http://localhost:8000 可以看到服务器启动成功
  ```

5. **数据迁移**
  迁移的概念:就是将模型映射到数据库的过程

  生成迁移:**python manage.py makemigrations**

  执行迁移:**python manage.py migrate**

  ​

6. **创建应用**
  **python manage.py startapp XXX**
  创建名称为XXX的应用
  使用应用前需要将应用配置到项目中，在settings.py中将应用加入到INSTALLED_APPS选项中

  应用目录介绍

  ```python
  __init__.py:其中暂无内容，使得app成为一个包
  admin.py:管理站点模型的声明文件，默认为空
  apps.py:应用信息定义文件，在其中生成了AppConfig，该类用于定义应用名等数据
  models.py:添加模型层数据类文件
  views.py:定义URL相应函数（路由规则）
  migrations包:自动生成，生成迁移文件的
  tests.py:测试代码文件
  ```

  ​

7. **基本视图**
  首先我们在views.py中建立一个路由响应函数
  from django.http import HttpResponse

  def welcome(request):
  	return HttpResponse('HelloDjango');

  接着我们在urls中进行注册
  from App import views
  url(r'^welcome/',views.welcome)

  基于模块化的设计，我们通常会在每个app中定义自己的urls

  在项目的urls中将app的urls包含进来
  from django.conf.urls import include
   url(r'^welcome/',include('App.urls'))

  课堂练习：新建一个django项目，访问http://localhost:8000/时每次刷新页面显示不同的时间。

  ​

8. **基本模板**
  模板实际上就是我们用HTML写好的页面

  创建模板文件夹templates, 在模板文件夹中创建模板文件

  在views中去加载渲染模板, 使用render函数: return render(request,'xxx')

  课堂练习：在上一个课堂练习中，使用template显示页面内容。

  ​

9. **定义模型**
  在models.py 中引入models
  from django.db import models

  创建自己的模型类，但切记要继承自 models.Model

  案例驱动，使用模型定义班级，并在模板上显示班级列表

  ```python
  班级: table : grades
   	columns: 	
  			班级名称 - name
  			成立时间 - date
  			女生个数 - girlnum
  			男生个数 - boynum
  			是否删除 - is_elete
  ```


  10. **Admin 后台管理**

        在admin.py中将model加入后台管理：

        admin.site.register(Grade)

        创建超级用户：**python manage.py createsuperuser**

        访问admin后台：http://127.0.0.1:8000/admin/


11. **展示班级列表**

		在views.py文件中编写班级的视图函数：

```python
	def grade_list(request):
    	g_list = Grade.objects.all()  # 获取班级所有数据
    	return render(request, 'grade/grade_list.html', {'g_list': g_list})
```

​	模板文件：

```python
	{% for grade in g_list %}
        {{ grade.sname }}
	{% endfor %}
```

12. **配置url**

		在grade App中新建urls.py文件，输入如下代码：

```python
from django.conf.urls import url
from .views import grade_list
urlpatterns = [
	url(r'^grade/$', grade_list),
]
```
​	在工程的urls.py文件中添加如下代码：

```python
url(r'^', include('grade.urls')),
```





#### 练习：

​	1， 从创建虚拟环境到显示出所有班级再操作至少2次

​	2，在班级Grade所在项目中创建学生students应用，在模板显示学生列表

​	学生table：students
		columns:	

​			学生姓名 - name
			学生性别 - gender
			学生年龄 - age
			学生简介 - info	
			是否删除 - is_delete 

 	定义学生类
  		class Students(models.Model):
  			name = models.CharField(max_length=20)
  	  		gender = models.BooleanField(default=True)
  	  		age = models.IntegerField()
  	  		info = models.CharField(max_length=20)
  	  		is_delete = models.BooleanField(default=False)



​	3，学会查看官网: https://docs.djangoproject.com/en/1.11/intro/tutorial01/



