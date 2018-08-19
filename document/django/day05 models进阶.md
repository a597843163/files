#  day 05 models进阶

## 1.models基本操作

```python
django中遵循 Code Frist 的原则，即：根据代码中定义的类来自动生成数据库表。
对于ORM框架里：
	我们写的类表示数据库的表
	如果根据这个类创建的对象是数据库表里的一行数据
	那么对象.属性（对象.id 对象.value）就是每一行里的数据 
    
models基本操作
增：
	1）创建对象实例，然后调用save方法：
		obj = Author(first_name='zhang', last_name='san') 
		obj.save()
	2）使用create方法
		Author.objects.create(first_name='li', last_name='si')
    3）使用get_or_create方法，可以防止重复
    	Author.objects.get_or_create(first_name='zhang', last_name='san')
    
删：
	使用Queryset的delete方法：
	# 删除指定条件的数据
	Author.objects.filter(first_name='zhang').delete()
	# 删除所有数据
	Author.objects.all().delete() 
	注意： objects不能直接调用delete方法。
	使用模型对象的delete方法：
	obj = Author.objects.get(id=5)
	obj.delete()
    
改：
	Author.objects.filter(last_name='dfdf').update(last_name='san')
	模型没有定义update方法，直接给字段赋值，并调用save，能实现update的功能，比如：
	>>> obj = Author.objects.get(id=3)
	>>> obj.first_name = 'zhang'
	>>> obj.save()
	save更新时会更新所有字段。如果只想更新某个字段，减少数据库操作，可以这么做：
	obj.first_name = 'li'
	obj.save(update_fields=['first_name'])
	注意：更新操作不能更新关联表的属性，比如下面的语句是不起作用的。
		Author.objects.update(book__title='b')
        
查：
		获取单条数据：Author.objects.get(id=123)
			get()：返回一个满足条件的对象
	      如果没有找到符合条件的对象，会引发 模型类.DoesNotExist异常
	      如果找到多个，会引发  模型类.MultipleObjectsReturned 异常
		  first()：返回查询集中的第一个对象
		  last()：返回查询集中的最后一个对象
		  count()：返回当前查询集中的对象个数
		  exists()：判断查询集中是否有数据，如果有数据返回True没有反之
		Author.objects.all()               # 获取全部
		Author.objects.filter(name='seven') # 获取指定条件的数据
		Author.objects.all().values('password') # 获取指定列的值，可以传多个参数！返回包含字典的列表（保存了字段名和对应的值）
        Author.objects.all().values_list('password') # 获取指定列的值，可以传多个参数！返回包含元组列表（只保存值）
        
        
	进阶操作：
		# 获取个数
		Author.objects.filter(name='seven').count()
        	#select count(*) from Author where name='seven'
            
		Author.objects.filter(id__gt=1)              # 获取id大于1的值
		Author.objects.filter(id__gte=1)              # 获取id大于或等于1的值
        	#select * from Author where id>1
            
		Author.objects.filter(id__lt=10)             # 获取id小于10的值
		Author.objects.filter(id__lte=10)             # 获取id小于等于或d10的值
        	#select * from Author where id<10
            
		Author.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
        	#select * from Author where id<10 and id>1
            
		Author.objects.filter(id__in=[11, 22, 33])   # 获取id在11、22、33中的数据
        	#select * from Author where id in (11,22,33)
            
		Author.objects.exclude(id__in=[11, 22, 33])  # not in
            #select * from Author where id not in (11,22,33)

		Author.objects.filter(name__contains="ven") # contains（和数据中like语法相同）
            #select * from Author where name like '%ven%'
            #select * from Author where name like '%v\%n%'
            
		Author.objects.filter(name__icontains="ven") # icontains大小写不敏感
        
         Author.objects.filter(name__regex="^ven") # 正则匹配
         Author.objects.filter(name__iregex="^ven") # 正则匹配,忽略大小写
        
		Author.objects.filter(id__range=[1, 2])   # 范围bettwen and
        
           # startswith，istartswith, endswith, iendswith: 
           #  		以什么开始，以什么结束，和上面一样带i的是大小写不敏感的
        
		Author.objects.filter(name='seven').order_by('id')    # asc正序
		Author.objects.filter(name='seven').order_by('-id')   # desc反序
        
		Author.objects.all()[10:20]  #切片，取所有数据的10条到20条，分页的时候用的到，下标从0开始，不能为负数
        
        
# 聚合	
    使用aggregate()函数返回聚合函数的值
		Avg：平均值
		Count：数量
		Max：最大
		Min：最小
		Sum：求和
    from django.db.models import Count, Min, Max, Sum
	Author.objects.aggregate(Max('age'))

# 注解
	obj = Author.objects.annotate(num_books=Count('book'))
	obj[0].num_books
	
```



## 2. 模块关联关系

```python
关系
	·分类
		·ForeignKey：一对多，将字段定义在多的端中
		·ManyToManyField：多对多，将字段定义在两端中
		·OneToOneField：一对一，将字段定义在任意一端中
                
        
一对多关系，举例说明（一对一， 多对多类似）： 
    	一个班级可以有多个学生， 一个学生只能属于一个班级
   		class Grade(models.Model):
		    name = models.CharField(max_length=20)
    	class Student(models.Model):
             name = models.CharField(max_length=20)
             grade = models.ForeignKey(Grade)
     	
		对象的使用：
        	正向（在Student这边，有grade属性的这一边）：
            	获取学生所在班级（对象）: stu.grade
                获取学生所在班级的属性: stu.grade.name
    		反向（在Grade这边）：
            	获取班级的所有学生(获取Manager对象)：grade.student_set
			   获取班级的所有学生（获取QuerySet查询集）: grade.student_set.all()
                
        filter(),get()等操作中的使用：
        	正向（在Student这边，有grade属性的这一边）：
            	    Student.objects.filter(属性__name=1)
            	如：Student.objects.filter(grade__name=1)
        	反向（在Grade这边）：
            		Grade.objects.filter(类名小写__id=7)
            	如：Grade.objects.filter(student__id=7)
        
```



## 3. Model连表结构

```python
ORM核心知识回顾：
	django根据代码中定义的类来自动生成数据库表。
	我们写的类表示数据库的表。
	根据这个类创建的对象是数据库表里的一行数据。
	对象.id 对象.value 是每一行里的数据

一对多：models.ForeignKey(其他表)
多对多：models.ManyToManyField(其他表)
一对一：models.OneToOneField(其他表)
应用场景：
	一对多：当一张表中创建一行数据时，有一个单选的下拉框（可以被重复选择）
		例如：创建用户信息时候，需要选择一个用户类型【普通用户】【金牌用户】【铂金用户】
	多对多：在某表中创建一行数据时，有一个可以多选的下拉框。
		例如：创建用户信息，需要为用户指定多个爱好。
	一对一：在某表中创建一行数据时，有一个单选的下拉框（下拉框中的内容被用过一次就消失了）
		例如：有个身份证表，有个person表。每个人只能有一张身份证，一张身份证也只能对应一个人，这就是一对一关系。
	
1.1 一对多关系，即外键
	为什么要用一对多。先来看一个例子。有一个用户信息表，其中有个用户类型字段，存储用户的用户类型。如下：
		class UserInfo(models.Model):
		    username = models.CharField(max_length=32)
		    age = models.IntegerField()
		    user_type = models.CharField(max_length=10)
	不使用外键时用户类型存储在每一行数据中。如使用外键则只需要存储关联表的id即可，能够节省大量的存储空间。同时使用外键有利于维持数据完整性和一致性。
	当然也有缺点，数据库设计变的更复杂了。每次做DELETE 或者UPDATE都必须考虑外键约束。
    
	刚才的例子使用外键的情况：单独定义一个用户类型表：
		class UserType(models.Model):
		    caption = models.CharField(max_length=32)
		
		class UserInfo(models.Model):
		    user_type = models.ForeignKey('UserType')
		    username = models.CharField(max_length=32)
		    age = models.IntegerField()
            
	我们约定：
		正向操作: ForeignKey在UserInfo表里，如果根据UserInfo去操作就是正向操作。
		反向操作: ForeignKey不在UserType里，如果根据UserType去操作就是反向操作。
        
	一对多的关系的增删改查：
		正向操作：
        	 增
            	1）创建对象实例，然后调用save方法：
                    obj = UserInfo(name='li', age=44, user_type_id=2)
                    obj.save()
                2）使用create方法
                    UserInfo.objects.create(name='li', age=44, user_type_id=2)
                3）使用get_or_create方法，可以防止重复
                    UserInfo.objects.get_or_create(name='li', age=55, user_type_id=2)
			   4）使用字典。
					dic = {'name':'zhangsan','age':18,'user_type_id':3}
					UserInfo.objects.create(**dic)
                5）通过对象添加 
					usertype = UserType.objects.get(id=1)
					UserInfo.objects.create(name='li', age=55, user_type=usertype)
                    
		 	删  
            	和普通模式一样删除即可。如：
					UserInfo.objects.filter(id=1).delete()
			
             改  
                和普通模式一样修改即可。如：
					UserInfo.objects.filter(id=2).update(user_type_id=4)
                    
             查 
            	正向查找所有用户类型为钻石用户的用户，使用双下划线：
					users = UserInfo.objects.filter(user_type__caption__contains='钻石')
					正向获取关联表中的属性可以直接使用点.语法，比如获取users查询集中第一个用户的caption：
					users[0].user_type.caption
                    
		反向操作：
        	增 (一般使用正向增即可)
            	通过usertype来创建userinfo
				1） 通过userinfo_set的create方法
					#获取usertype实例
					ut = UserType.objects.get(id=2)
					#创建userinfo
					ut.userinfo_set.create(name='smith',age=33)
				
        	 删 
				删除操作可以在定义外键关系的时候，通过on_delete参数来配置删除时做的操作。
				on_delete参数主要有以下几个可选值：
					models.CASCADE	默认值，表示级联删除，即删除UserType时，相关联的
                    				UserInfo也会被删除。
					models.PROTECT	保护模式， 阻止级联删除。
					models.SET_NULL	置空模式   设为null，null=True参数必须具备
					models.SET_DEFAULT 置默认值 设为默认值，default参数必须具备
					models.SET()	删除的时候重新动态指向一个实体访问对应元素 ，可传函数
					models.DO_NOTHING   什么也不做。
				注意: 修改on_delete参数之后需要重新同步数据库，如果使用
                       python manage.py shell进行models操作，需要退出shell重新进入。
            	
		 	改 
            	 和普通模式一样，不会影响级联表。
                
             查 
            	 通过usertype对象来查用户类型为1的用户有哪些
				obj=UserType.objects.get(id=1)
				obj.userinfo_set.all() 
				
                 可以通过在定义foreignkey时指定related_name来修改默认的userinfo_set，比如指定related_name为info
					user_type = models.ForeignKey('UserType'，related_name='info')
				指定related_name之后，反向查的时候就变成了：
					obj.info.all()
				获取用户类型为1且用户名为shuaige的用户
					obj.info.filter(username='shuaige')
				
                 外键关系中，django自动给usertype加了一个叫做userinfo的属性。使用双下划线，可以通过userinfo提供的信息来查usertype (了解)
					user_type_obj = UserType.objects.get(userinfo__username='zs')

1.2 多对多关系
		针对多对多关系django会自动创建第三张表。也可以通过through参数指定第三张表。
		用户和组是典型的多对多关系：
			class Group(models.Model):
			    name = models.CharField(max_length=20)
			
			    def __str__(self):
			        return self.name

			class User(models.Model):
			    name = models.CharField(max_length=64)
			    password = models.CharField(max_length=64)
			    groups = models.ManyToManyField(Group)
			
			    def __str__(self):
			        return self.name
		操作： 		
			增： 
            	先分别创建user和group, 再使用add关联
                	u = User(name='aa', password='123')
                	u.save()
			   	   g = UserGroup(name='g5')
			  	   g.save()
            	通过Manager对象使用add()方法
                    u.groups.add(g)  或  g.user_set.add(u)
             删： 
            	和一对多类似，删除user或group会级联删除user_groups表中的关联数据
             改：
            	和一对多类似，只修改当前表
             查：
            	正向：
                	查询id=2的用户所在的所有组group
                	u = User.objects.get(id=2)
                	u.groups.all()
                反向：
                	查询id=1的组中包含的所有用户
                	g = Group.objects.get(id=1)
                	g.user_set.all()
		

1.3 一对一关系
	一对一不是数据库的一个连表操作，而是Django独有的一个连表操作。一对一关系相当于是特殊的一对多关系，只是相当于加了unique=True。
	一个人只能有一张身份证，一张身份证对应一个人，是一个典型的一对一关系。
		class IdCard(models.Model):
	    	idnum = models.IntegerField()
	    	def __str__(self):
	        	return str(self.idnum)

		class Person(models.Model):
	    	idcard = models.OneToOneField(IdCard)
	    	name = models.CharField(max_length=20)
	   	 	def __str__(self):
	        	return self.name
            
	一对一关系比较简单。两种表互相都有对方。比如：
		>>> lisi = Person.objects.get(id=3)
		>>> lisi.idcard
		<IdCard: 123456>
		>>> ids = IdCard.objects.get(id=3)
		>>> ids.person
		<Person: lisi>

```



## 4.F和Q

```python
Q查询——对对象的复杂查询
F查询——专门取对象中某列值的操作

导入Q,F对象 :
    from django.db.models import Q,F

F:主要作用
	1）和models自身的字段进行对比。比如：
		Student.objects.filter(age__gt=F('age2'))
	2） 对字段进行数学运算。比如：
		Student.objects.filter(age__gt=F('age2') * 2)
		
Q:	
    且操作:
		默认情况下Django的查询只是且操作如下：
         找到用户为zhangsan并且age=18的数据
			UserInfo.objects.filter(username='zhangsan',age='18')
	或操作： 
		如果需要执行或操作 ，就需要使用到Q对象了
		Q对象可以用 & | ~  (与，或，非)去连接
			UserInfo.objects.filter(Q(age__gt=20) & Q(age__lt=50))
             UserInfo.objects.filter(Q(age__gt=20) | Q(age__lt=50))
             UserInfo.objects.filter(~Q(age__lt=50))
		等于： WHERE question LIKE 'Who%' OR question LIKE 'What%'
		如果Q和关键字参数一起使用的话，Q必须放在关键字参数前面：
		Student.objects.get(Q(age__gt=20) | Q(age__lt=50), name__contains='zhang')
        
```



## 5.models的Manager

```python
django通过models的manager来执行数据库操作。
每个django model至少有一个manager。
可以自定义manager。
自定义manager必须继承自models.Manager

给默认的manager改名：
	class Person(models.Model):
     	...
     	people = models.Manager()
        
定制manager
1）增加额外的方法：
	class BookManager(models.Manager):
	    def title_count(self, keyword):
	        return self.filter(title__icontains=keyword).count()

	class Book(models.Model):
	    title = models.CharField(max_length=100)
	    authors = models.ManyToManyField(Author)
	    publisher = models.ForeignKey(Publisher)
	    publication_date = models.DateField()
	    num_pages = models.IntegerField(blank=True, null=True)
	    objects = BookManager()
	
	    def __str__(self):
	        return self.title

2）修改默认manager的查询集
	class DahlBookManager(models.Manager):
    	def get_queryset(self):
        	return super(DahlBookManager, self).get_queryset().filter(author='Roa')

	class Book(models.Model):
	    title = models.CharField(max_length=100)
	    author = models.CharField(max_length=50)

	    objects = models.Manager() # The default manager.
	    dahl_objects = DahlBookManager() # The Dahl-specific manager.
        
3）使用多个manager		
	class MaleManager(models.Manager):
	    def get_queryset(self):
	        return super(MaleManager, self).get_queryset().filter(sex='M')
	
	class FemaleManager(models.Manager):
	    def get_queryset(self):
	        return super(FemaleManager, self).get_queryset().filter(sex='F')
	
	class Person(models.Model):
	    first_name = models.CharField(max_length=50)
	    last_name = models.CharField(max_length=50)
	    sex = models.CharField(max_length=1, 
	                           choices=( ('M', 'Male'),  
	                                    ('F', 'Female') )
	                           )
	    people = models.Manager()
	    men = MaleManager()
	    women = FemaleManager()
        
        
```

