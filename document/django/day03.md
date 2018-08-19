#day03 mysql&admin后台系统

## 1. mysql的使用

```python
1,在windows安装mysql数据库， 安装方法参考《mysql安装.pdf》，记住安装过程中的设置的mysql数据库用户名和密码；
2,用管理员权限打开cmd.exe， 在cmd窗口输入命令：net start mysql57 来启动mysql；
3,安装Navicat；
4,打开navicat, 点击'连接'来创建与mysql的连接， 然后创建数据库test；

5,在Django中配置和使用mysql数据库
使用mysql数据库，settings中配置如下：
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'test',
	        'USER': 'root',
	        'PASSWORD': 'root',
	        'HOST': '127.0.0.1',
	        'PORT': '3306',
	    }
	}
安装mysql依赖包：
	pip install -i https://pypi.douban.com/simple mysqlclient
如安装该包出错。下载新包：https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
```



##2. django admin后台系统

```python
Django中默认集成了后台数据管理页面，通过简单的配置就可以实现模型后台的Web控制台。
管理界面通常是给系统管理员使用的，用来完成数据的输入，删除，查询等工作。
使用以下models来示范admin后台系统的用法。

创建一个项目。用来说明出版社，书籍和作者的关系。
1. 出版社，书籍，作者都有一个首页index.html
2. 在书籍的index.html中有一个"查看所有书籍"的超链接按钮，可以点击进入书籍列表list.html页面
3. 在书籍list.html中显示所有书名，点击书名可以进入书籍详情detail.html
4，在书籍detail.html中可以点击该书的作者和出版社，进入作者的detail.html和出版社的detail.html页面
 假定关系：书籍：作者 => n:n  （一本书可以由多个作者共同完成， 一个作者也可以创作多本书）
 	  	出版社：书籍 => 1:n  （一个出版社可以出版多本书， 一本书由一个出版社出版）

	from django.db import models

	class Publisher(models.Model):
	    name = models.CharField(max_length=30)
	    address = models.CharField(max_length=50)
	    city = models.CharField(max_length=60)
	    state_province = models.CharField(max_length=30)
	    country = models.CharField(max_length=50)
	    website = models.URLField()

	class Author(models.Model):
	    first_name = models.CharField(max_length=30)
	    last_name = models.CharField(max_length=40)
	    email = models.EmailField(null=True)

	class Book(models.Model):
	    title = models.CharField(max_length=100)
	    authors = models.ManyToManyField(Author)
	    publisher = models.ForeignKey(Publisher)
	    publication_date = models.DateField()

使用admin后台系统之前，需要先创建一个系统管理员,创建管理员之前需先同步数据库。
	python manager.py createsuperuser
设置为中文
	settings中LANGUAGE_CODE = 'zh-hans'
设置时间，时区
	TIME_ZONE='Asia/Shanghai'

添加自己的数据模型
	在admin.py中注册
	admin.site.register(Publisher)
	admin.site.register(Author)
	admin.site.register(Book))
在admin中给model添加数据。
给模型加上__str__函数，比如给Author模型添加str函数，让author的显示更加友好：
	def __str__(self):
    	return '%s %s' % (self.first_name, self.last_name)
        
希望控制admin中添加model数据时的动作，可以修改相应字段的属性。
比如author的email字段运行添加的时候为空，可以在email字段定义中加上 blank=True(可以空白),
比如book的publication_date添加 blank=True, null=True（可以为null）属性。
修改models属性之后记得及时做数据迁移。

使用verbose_name属性指定字段的别名:
    比如给publisher的name字段指定一个中文的别名verbose_name='出版社名称'。
	在models的修改页面，默认显示的是models定义的str函数返回的字符串。

通过定义MoldelAdmin来定制model在admin的表现。比如给Author定义AuthorAdmin。
	class AuthorAdmin(admin.ModelAdmin):
		list_display = ('first_name', 'last_name', 'email')
	相应的注册代码也要变化：
	admin.site.register(Author, AuthorAdmin)

给Author添加一个搜索框：
	search_fields = ('first_name', 'last_name')
给book添加一个过滤器
	list_filter = ('publication_date',)
	过滤器不光可以作用在日期字段上，还可以作用在boolean类型和外键上。
	另一种增加日期过滤的方式：
	date_hierarchy = 'publication_date'
字段排序：
	ordering = ('-publication_date',)
	
修改编辑页面显示的字段及显示顺序，默认按照models中字段的定义顺序显示：
	fields = ('title', 'authors', 'publisher', 'publication_date')
与fields相反的字段是exclude
	exclude = ['publication_date',] 
改善多对多关系中对象选择操作，比如给BookAdmin添加如下属性：
	filter_horizontal = ('authors',)
filter_horizontal和filter_vertical 选项只适用于多对多关系。

一对多的外键关系，admin使用select box下拉菜单来表示。如不想用select box，可添加如下属性，让原来一次性加载所有publisher的select box变成填写publisher的id：
	raw_id_fields = ('publisher',)

让字段分组显示，fieldsets和上面提到的field不能同时出现：
	fieldsets = (
    	('作者', {'fields': ('authors',)}),
    	('出版商', {'fields': ('publisher',)}),
	)


定制list_display字段的显示。比如给Author加一个布尔型gender字段，来表示性别。为了让显示更加人性化：
	# 定制显示属性
    def showgender(self):
        if self.gender:
            return '男'
        else:
            return '女'
    list_display = ('first_name', 'last_name', 'email', showgender)
给该函数设置简短描述，让显示更加友好：
	showgender.short_description = '性别'	

可以将modeladmin的属性简单划分为列表页属性和添加、修改页属性
# 列表页属性
	list_display,list_filter,search_fields,list_per_page等
# 添加、修改页属性
	fields ,fieldsets, filter_horizontal, raw_id_fields等
            
```
