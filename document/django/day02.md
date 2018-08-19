#Day02 url和模板

##1. URL
	URL地址说明：
 ![](url.png)

```python
使用url给视图函数传参数
在url配置中将正则部分小括号括起来。比如：
	url(r'^time/plus/(\d{1,2})/$', views.hours_ahead)
如果有多个参数则用/隔开，参数需要用分组，比如：
	url(r'^time/plus/(\d{1,2})/(\d{1,2})/$', views.hours_ahead),
给参数命名，使用正则分组的别名，比如：
	url(r'^time/plus/(?P<time1>\d{1,2})/(?P<time2>\d{1,2})/$', views.hours_ahead)
使用分组别名之后，视图函数的参数必须用分组的别名，但是位置可以不固定。

给url取别名，那么在使用此url的地方可以使用别名。比如：
	url(r'^buy/$', views.buy, name='buy'),
	url(r'^login/$', views.login, name='login'),
	

```

## 2. 反向解析

```python
在视图函数中，反向解析url：
    from django.shortcuts import render, redirect
    from django.urls import reverse
    def buy(request):
        return redirect(reverse('index'))
        return redirect(reverse('detail', args=[2]))
        return redirect(reverse('detail', kwargs={"id": 2}))
	
在templates中，使用别名：
	{% url 'detail' stu.id %}

使用命名空间:
    在工程的urls.py文件中，在include时，可以指定命名空间，更加细化的划分url。比如： 
		url(r'^App/', include('App.urls', namespace='App')),
	指定命令空间后，使用反向解析时需要加上命名空间，比如：
		在视图函数中: return redirect(reverse('students:index'))
		在templates中: {% url 'students:detail' %}
```



##3. 模板

```python
在Django框架中，模板是可以帮助开发者快速生成呈现给用户页面的工具
模板的设计方式实现了我们MVT中VT的解耦，VT有着N:M的关系，一个V可以调用任意T，一个T可以供任意V使用
模板处理分为两个过程
	加载
	渲染
模板主要有两个部分
	HTML静态代码
	动态插入的代码段（挖坑，填坑）
模板中的动态代码段除了做基本的静态填充，还可以实现一些基本的运算，转换和逻辑

模板中的变量: 视图传递给模板的数据，遵守标识符规则
	语法： {{  var }}
	如果变量不存在，则插入空字符串
        
 	python manage.py shell: 进入Python环境, 且会自动导入Django配置，建议使用
        
    >>> python manage.py shell   # 进入python环境
	>>> from django import template
	>>> t = template.Template('My name is {{ name }}.')
	>>> c = template.Context({'name': 'Nige'})
	>>> print (t.render(c))
	My name is Nige.
	>>> c = template.Context({'name': 'Barry'})
	>>> print (t.render(c))
	My name is Barry.
	
模板中的点语法	
字典查询
	>>> from django.template import Template, Context
	>>> person = {'name': 'Sally', 'age': '43'}
	>>> t = Template('{{ person.name }} is {{ person.age }} years old.')
	>>> c = Context({'person': person})
	>>> t.render(c)
	'Sally is 43 years old.'		
    
属性或者方法	
	>>> from django.template import Template, Context
	>>> import datetime
	>>> d = datetime.date(2017, 5, 2)
	>>> d.year
	2017
	>>> d.month
	5
	>>> d.day
	2
	>>> t = Template('The month is {{ date.month }} and the year is {{ date.year }}.')
	>>> c = Context({'date': d})
	>>> t.render(c)
	'The month is 5 and the year is 2017.'
	
	>>> from django.template import Template, Context
	>>> class Person(object):
	...     def __init__(self, first_name, last_name):
	...         self.first_name, self.last_name = first_name, last_name
	>>> t = Template('Hello, {{ person.first_name }} {{ person.last_name }}.')
	>>> c = Context({'person': Person('John', 'Smith')})
	>>> t.render(c)
	'Hello, John Smith.'
	
方法不能有参数。
	>>> from django.template import Template, Context
	>>> t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}')
	>>> t.render(Context({'var': 'hello'}))
	'hello -- HELLO -- False'
	>>> t.render(Context({'var': '123'}))
	'123 -- 123 -- True'
	
列表，使用索引，不允许负索引	
	>>> from django.template import Template, Context
	>>> t = Template('Item 2 is {{ items.2 }}.')
	>>> c = Context({'items': ['apples', 'bananas', 'carrots']})
	>>> t.render(c)
	'Item 2 is carrots.'
	
模板中的小弊端，调用对象的方法，不能传递参数



模板中的标签
语法 {%  tag  %}
作用	
	1. 加载外部传入的变量  
	2. 在输出中创建文本
	3. 控制循环或逻辑
if 语句：
	格式:	
	if单分支
		{% if  表达式 %}
	    	语句
		{% endif  %}
	if双分支
		{%  if 表达式 %}
	    	语句
		{% else  %}
	    	语句
		{% endif %}
	if多分支
		{% if 表达式 %}
        	语句	
 		{% elif 表达式 %}
        	语句
        {% else  %}
	    	语句
		{% endif %}
	
	判断true或false
		{% if today_is_weekend %}
			<p>Welcome to the weekend!</p>
		{% endif %}
	使用and or not,可结合使用，and具有更高优先权。
		{% if athlete_list and coach_list %}
	    	<p>Both athletes and coaches are available.</p>
		{% endif %}
	
		{% if not athlete_list %}
	    	<p>There are no athletes.</p>
		{% endif %}
	
		{% if athlete_list or coach_list %}
	    	<p>There are some athletes or some coaches.</p>
		{% endif %}
		
		{% if not athlete_list or coach_list %}
			<p>There are no athletes or there are some coaches.</p>
		{% endif %}

		{% if athlete_list and not coach_list %}
			<p>There are some athletes and absolutely no coaches.</p>
		{% endif %}
		
	使用多个相同的逻辑操作关键字也是允许的，比如：
		{% if athlete_list or coach_list or parent_list or teacher_list %}
	使用in和not in，
		{% if "bc" in "abcdef" %}
			This appears since "bc" is a substring of "abcdef"
		{% endif %}
		{% if user not in users %}
			If users is a list, this will appear if user isn't an element of the list.
		{% endif %}
	使用is 和is not
		{% if somevar is True %}
			This appears if and only if somevar is True.
		{% endif %}

		{% if somevar is not None %}
			This appears if somevar isn't None.
		{% endif %}
```


```python
for 语句：
	{% for 变量 in 列表 %}
		语句1 
	{% empty %}
		语句2
	{% endfor %}
	当列表为空或不存在时,执行empty之后的语句
	
	{{ forloop.counter }} 表示当前是第几次循环，从1数数
	{% for item in todo_list %}
	    <p>{{ forloop.counter }}: {{ item }}</p>
	{%endfor %}
	
	{{ forloop.counter0}}表示当前是第几次循环，从0数数
	{{ forloop.revcounter}}表示当前是第几次循环，倒着数数，到1停
	{{ forloop.revcounter0}}表示当前第几次循环，倒着数，到0停
	{{ forloop.first }} 是否是第一个  布尔值
	{% for object in objects %}
	    {% if forloop.first %}
	        <li class="first">
	    {% else %}
	        <li>
	    {% endif %}
	    {{ object }}</li>
	{% endfor %}
	
	{{ forloop.last }} 是否是最后一个 布尔值
	{% for link in links %}
		{{ link }}{% if not forloop.last %} | {% endif %}
	{% endfor %}
	
	forloop.parentloop
	{% for country in countries %}
	  <table>
	      {% for city in country.city_list %}
	      <tr>
	          <td>Country #{{ forloop.parentloop.counter }}</td>
	          <td>City #{{ forloop.counter }}</td>
	          <td>{{ city }}</td>
	      </tr>
	      {% endfor %}
	  </table>
	 {% endfor %}
	 
注释：
	单行注释
	{#  被注释掉的内容  #}

	多行注释
	{% comment %}
		内容
	{% endcomment %}
	
过滤器: 
	{{ var|过滤器 }}
	作用：在变量显示前修改
	
	add	{{ value|add:2 }}
	没有减法过滤器，但是加法里可以加负数
		{{ value|add:-2 }}
	lower 	
		{{ name|lower }}
	upper
		{{ my_list|first|upper }}
	截断：
		{{ bio|truncatechars:30 }}
	过滤器可以传递参数，参数需要使用引号引起来
	比如join：	{{ students|join:'=' }}
	
	默认值:default，格式 {{var|default:value}}
	如果变量没有被提供或者为False，空，会使用默认值

	根据指定格式转换日期为字符串，处理时间的
	就是针对date进行的转换	
		{{  dateVal | date:'y-m-d' }}
		
HTML转义
	将接收到的数据当成普通字符串处理还是当成HTML代码来渲染的一个问题

	渲染成html:{{ code|safe }}
	关闭自动转义
	{% autoescape off%}
		code
	{% endautoescape %}
	打开自动转义转义
	{% autoescape on%}
		code
	{% endautoescape %}
	
模板继承
	block:挖坑
		{% block XXX%}
			code
		{% endblock %}

	extends 继承，写在开头位置
		{% extends '父模板路径' %}

	include: 加载模板进行渲染
         {% include '模板文件' %}




    
```

