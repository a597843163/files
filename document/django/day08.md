#day08 中间件&验证码&富文本&缓存 
##1. 中间件&AOP
```python
中间件：是一个轻量级的，底层的插件，可以介入Django的请求和相应过程（面向切面编程）

中间件的本质就是一个python类

面向切面编程（Aspect Oriented Programming）简称AOP。AOP的主要实现目的是针对业务处理过程中的切面进行提取，它所面对的是处理过程中的某个步骤或阶段，以获得逻辑过程中各部分之间低耦合的隔离效果。

中间件可实现功能
   - 统计
   - 黑名单
   - 白名单
   - 反爬
   - 界面友好化（捕获异常）
```
#### 1.1 中间件的可切入点

![1525190616689](F:\pythonStudy\Django\day08\doc\1525190616689.png)

#### 1.2 切入函数

```python
__init__:
    没有参数，服务器响应第一个请求的时候自动调用，用户确定是否启用该中间件
process_request(self,request):
    在执行视图前被调用，每个请求上都会调用，不主动进行返回或返回HttpResponse对象
process_view(self,request,view_func,view_args,view_kwargs)：
	调用视图之前执行，每个请求都会调用，不主动进行返回或返回HttpResponse对象
process_template_response(self,request,response):
    在视图刚好执行完后进行调用，每个请求都会调用，不主动进行返回或返回HttpResponse对象
process_response(self,request,response):
    所有响应返回浏览器之前调用，每个请求都会调用，不主动进行返回或返回HttpResponse对象
process_exception(self,request,exception):
    当视图抛出异常时调用，不主动进行返回或返回HttpResponse对象
```

#### 1.3 自定义中间件

```python
自定义中间件流程
	1.在工程目录下创建middleware目录
	2.目录中创建一个python文件
	3.在python文件中导入中间件的基类
		from django.utils.deprecation import MiddlewareMixin
	4.在类中根据功能需求，创建切入需求类，重写切入点方法
        class LearnAOP(MiddlewareMixin):
            def process_request(self,request):
                print('request的路径',request.GET.path)
	5.启用中间件，在settings中进行配置，MIDDLEWARE中添加middleware.文件名.类名
   
```



## 2.验证码

```python
在用户登录，注册以及一些敏感操作的时候，我们为了防止服务器被暴力请求，或爬虫爬取，我们可以使用验证码进行过滤，减轻服务器的压力。

验证码需要使用绘图 Pillow
	pip install Pillow

核心
	Image,ImageDraw,ImageFont

绘制流程
	backgroundcolor = (10,20,30)   RGB颜色
	初始化画布 
    	image = Image.new('RGB',(100,50),backgroundcolor)
	获取画布中画笔对象
		draw = ImageDraw.Draw(image)
	绘制验证码，随机四个
        font = ImageFont.truetype('path',size)
        fontcolor = (20,40,60)
        draw.text((x,y),'R',font,fontcolor)
	最后扫尾
		del draw 
	
        import io
        buf = io.BytesIO()
        Image.save(buf, 'png')
        return HttpResponse(buf.getvalue(),'image/png')

```



## 3.富文本

```python
富文本:Rich Text Format（RTF），是有微软开发的跨平台文档格式，大多数的文字处理软件都能读取和保存RTF文档，其实就是可以添加样式的文档，和HTML有很多相似的地方

tinymce 插件

django的插件
	pip install django-tinymce

用处大约有两种
	1. 在后台管理中使用
	2. 在页面中使用，通常用来作博客

1.后台中使用:
	配置settings.py文件
		INSTALLED_APPS 添加  tinymce 应用
		添加默认配置
			TINYMCE_DEFAULT_CONFIG = {
				'theme':'advanced',
				'width':600,
				'height':400,
			}
	创建模型类
        from tinymce.models import HTMLField
        class Blog(models.Model):
            sBlog = HTMLField()
	配置站点
		admin.site.register

        
2.在视图中使用:
	使用文本域盛放内容
	<form>
		<textarea></textarea>
	</form>
	
    在head中添加script
    <script src='/static/tiny_mce/tiny_mce.js'></script>
    <script>
        tinyMCE.init({
            'mode':'textareas', 'theme':'advanced',
            'width':800,'height':600,
        })
    </script>
    
```



## 4. Cache

[https://docs.djangoproject.com/zh-hans/2.0/topics/cache/](https://docs.djangoproject.com/zh-hans/2.0/topics/cache/)

#### 缓存框架的核心目标

- 较少的代码
  - 缓存应该尽可能快
  - 因此围绕缓存后端的所有框架代码应该保持在绝对最小值，特别是对于获取操作
- 一致性
  - 缓存API应该是提供跨越不同缓存后端的一致接口
- 可扩展性
  - 基于开发人员的需求，缓存API应该可以在应用程序级别扩展

#### 缓存

- django内置了缓存框架，并提供了几种常用的缓存
  - 基于Memcached缓存
  - 使用数据库进行缓存
  - 使用文件系统进行缓存
  - 使用本地内存进行缓存
  - 提供缓存扩展接口

#### 缓存配置

1. 创建缓存表

   ```python
   python manage.py createcachetable [table_name]
   ```

2. 缓存配置

   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
           'LOCATION': 'my_cache_table',
           'TIMEOUT': '60',
           'OPTIONS': {
               'MAX_ENTRIES': '300',
           },
           'KEY_PREFIX': 'jack',
           'VERSION': '1',
       }
   }
   ```

#### 缓存使用

- 在视图中使用（使用最多的场景）
- @cache\_page\(\)
  - time 秒  60\*5 缓存五分钟
  - cache 缓存配置, 默认default，
  - key\_prefix 前置字符串

#### 缓存底层

获取cache 

```python
from django.core.cache import cache
cache = cache['cache_name'] 或 cache = cache.get('cache_name')
```

设置cache

```python
from django.core.cache import cache
cache.set(key, value, timeout)
```

使用原生缓存来实现

```python
def get_user_list(request):

    # 每次从缓存中获取
    user_cache = cache.get('user_cache')

    # 如果有缓存，则从缓存中直接取
    if user_cache:
        result = user_cache

    # 如果没有缓存，则从数据库中获取
    else:
        # 模拟长时间的数据操作
        user_list = User.objects.all()
        time.sleep(5)
		
        data = {
            'users': user_list,
        }
		
        # 使用模板渲染，得到result文本
        template = loader.get_template('App/stu_list.html')
        result = template.render(data)
                
        # 设置缓存
        cache.set('user_cache', result, 10)

    return HttpResponse(result)
```

