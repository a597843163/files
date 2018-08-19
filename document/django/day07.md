#day07 token&静态文件&媒体文件 
## 1. token

```python
1. 会话技术
2. 服务端会话技术
3. 它实际上就是手动实现的session
4. 实现token
	4.1 在models.py中User类中添加token字段
        class User(models.Model):
            name = models.CharField(max_length=30, unique=True)
            password = models.CharField(max_length=32)
            age = models.IntegerField(default=1)
            token = models.CharField(max_length=32, null=True, blank=True, default='')
    4.2 md5加密
         # md5加密
         def my_md5(password):
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            return md5.hexdigest()
        
   	4.3 注册用户时，随机生成唯一的token
     	token/usertoken,  用户唯一标识
        可以使用 时间+随机数+公司域名+ip信息 或 时间+随机数等方式生成token
        # 生成加密的token
        def generate_token():
            token = str(time.time()) + str(random.random())
            return my_md5(token)
    
    4.4 登录时使用cookie存储token
         # token
         d = datetime.datetime.now() + datetime.timedelta(days=7)  # 保存7天
         response.set_cookie('token', res.first().token, expires=d)
    
    4.5 根据token获取用户信息
    	token = request.COOKIES.get('token', '')
    	users = User.objects.filter(token=token)
    
    4.6 退出登录
    	response = HttpResponseRedirect(reverse('app:index'))
    	# 删除cookie: token
    	response.delete_cookie('token')
    	return response

```



## 2. 用户登录注册

```
1. 用户注册
	将用户名，用户密码，用户信息，存储到数据库中

2. 用户登陆
	使用用户名，用户密码进行数据库校验

3. 用户信息
	根据用户的唯一标识，去获取用户

4. 数据安全
	服务器的数据对任何人来说都应该是不可见的（不透明）
	可以使用常见的摘要算法对数据进行摘要(md5,sha)
	如果使用了数据安全，那么就需要在所有数据验证的地方都加上 数据安全
```



##3. 静态文件和媒体文件

	媒体文件：用户上传的文件，叫做media
	静态文件：存放在服务器的css,js，image等 叫做static
  ###3.1 在django中使用静态文件
```python
	1）首先确保django.contrib.staticfiles在 INSTALLED_APPS中
	2）在settings中定义 STATIC_URL
		STATIC_URL = '/static/'
	3）在你app的static目录中存放静态文件，比如： 	
		my_app/static/my_app/example.jpg.
	4）如果有别的静态资源文件，不在app下的static目录下，可以通过	
STATICFILES_DIRS来指定额外的静态文件搜索目录。
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static"),
            ...
        ]
    5）在模板中使用load标签去加载静态文件
		{% load static %}
		<img src="{% static "my_app/example.jpg" %}" alt="My image"/>
```
  ###3.2 在django中使用媒体文件
```python
	1）在settings中配置 MEDIA_ROOT
		MEDIA_ROOT = os.path.join(BASE_DIR, "media")
	
```



##4. 文件上传

```python
文件上传要求form表单存在enctype="multipart/form-data"属性，并且提交方法是post。
	<form enctype="multipart/form-data" action="/uploadFile/" method="post">  
	   <input type="file" name="myfile" />  
	   <br/>  
	   <input type="submit" value="upload"/>  
	</form>
    
最简单的文件上传：
	def file_upload(request):
        if request.method == 'POST':
            # 获取上传的文件，如果没有文件，则默认为None
            myFile = request.FILES.get('myfile', None)
            if not myFile:
                return HttpResponse("no files for upload")

            file_path = os.path.join(settings.MEDIA_ROOT, '1.jpg')
            with open(file_path, 'ab') as fp:
                for part in myFile.chunks():
                    fp.write(part)
            return HttpResponse("上传成功！")

        else:
            return render(request, 'index.html')
```



## 5. 多文件上传

```python
多文件上传和单文件上传类似
    1.需要在模板文件的form表单input中添加multiple
    2.后台获取时使用request.FILES.getlist('myfile', None)
def file_upload2(request):
    if request.method == 'POST':
        # 获取上传的文件，如果没有文件，则默认为None
        myFiles = request.FILES.getlist('myfile', None)
        for myFile in myFiles:
            if not myFile:
                return HttpResponse("no files for upload")
    
            file_path = os.path.join(settings.MEDIA_ROOT, myFile.name)
            with open(file_path, 'ab') as fp:
                for part in myFile.chunks():
                    fp.write(part)
                    
        return HttpResponse("上传成功！")

    else:
        return render(request, 'index.html')
```



## 6.分页

#### 6.1 分页工具

```python
django提供了分页的工具，存在于django.core中	
	Paginator : 数据分页工具
	Page	: 具体的某一页面

导入Paginator： 	
	from django.core.paginator import Paginator

Paginator:	
对象创建: 
	Paginator(数据集，每一页数据数)
属性:		
	count：对象总数
	num_pages：页面总数
	page_range: 页码列表，从1开始
方法:	
	page(整数): 获得一个page对象

常见错误:	
	InvalidPage：page()传递无效页码
	PageNotAnInteger：page()传递的不是整数
	Empty：page()传递的值有效，但是没有数据

    
Page:
	对象获得，通过Paginator的page()方法获得
属性:
	object_list：	当前页面上所有的数据对象
	number：	当前页的页码值
	paginator:	当前page关联的Paginator对象
方法：
	has_next()	:判断是否有下一页
	has_previous():判断是否有上一页
	has_other_pages():判断是否有上一页或下一页
	next_page_number():返回下一页的页码
	previous_page_number():返回上一页的页码	
	len()：返回当前页的数据的个数

```




作业： 1, 自己实现完整的登录注册功能

​	     2, 结合bootstrap实现分页功能 