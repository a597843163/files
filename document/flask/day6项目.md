## FLASK项目 博客

## 一、项目需求

1. 用户的登陆注册
2. 用户个人中心
3. 博客发表 评论 回复（回复要像去别的博客网站一样的回复） 无限极分类
4. 博客展示 分页
5. 收藏
6. 搜索 排序(按照评论最高，浏览量最高的，按照时间的...)



## 二、项目目录的结构

```python
bolg/
	app/
    	static/  #静态文件目录
        	css/ 
            js/
            img/
            upload/
        templates/	#模板目录
        forms/		#wtf表单目录
        models/		#模型目录
        views/		#视图目录
        config.py	#配置文件
        __init__.py #包文件必须的
        extensions.py	#包含所有用到的第三方扩展库的文件 并初始化
        email.py 	#发送邮件的模块
    venv/ #虚拟环境
    migrations/ #迁移目录
    manage.py/  #启动项文件
```



## 三、开发环境

一个不带任何第三方包的python环境

### (1) 在Windows下创建虚拟环境

1. 新建一个项目 进入到当前的项目的目录中

2. 安装

   ```python
   pip install virtualenv
   ```

3. 创建虚拟环境

   ```python
   virtualenv  venv
   ```

4. 启动虚拟环境

   ```python
   venv/Scripts/activate
   ```

5. 退出虚拟环境

   ```python
   venv/Scripts/deactivate.bat
   ```



### (2) 在Linux下创建虚拟环境

1. 安装

   ```python
   pip3 install virtualenv
   ```

2. 创建虚拟环境

   ```python
   virtualenv venv
   #如果使用上方的创建方式 进入使用pip list 发现有我们环境中的包 使用下面这种方式
   virtualenv --no-site-packages venv
   ```

3. 进入环境

   ```python
   source venv/bin/activate
   ```

   左侧出现venv证明进入成功

4. 退出环境

   ```python
   deactivate
   ```



##### 项目开发完以后 生成开发所用的依赖包文件

1. pip freeze > requirements.txt 到处依赖包文件
2. pip install -r requirements.txt  执行依赖包文件 



## 四、在虚拟环境中 安装所需要的第三方扩展包

1. pip install falsk
2. flask-script
3. flask-wtf
4. flask-moment
5. flask-bootstrap
6. pymysql
7. flask-sqlalchemy
8. flask-uploads
9. flask-migrate
10. flask-email



## 晚上

按照当前的配置的模式

自己创建 model中的user模型类

1. id
2. username
3. userpass
4. sex
5. age
6. email
7. icon

迁移文件的使用在当前的mvt中

登陆和注册



使用无限极分类表

1. 添加顶级分类
2. 添加子分类
3. 删除子分类（当前类别没有子类别）





















