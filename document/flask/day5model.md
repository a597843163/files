## flask  model

flask 作为一款mvc 也提供了 ORM功能

**ORM:**  对象关系的映射  通过ORM类去操作 数据库  类中属性 就是表的字段名  类名就是表名  我们就可以通过类的方式 去操作数据库  而不是在写原生SQL   将大量的重复的SQL简化



**安装:**

pip install flask-sqlalchemy



## 一、原生SQL

### (1) 在数据库中创建一个库 flaskdatabase

create database if not exists flaskdatabase character set utf8

### (2) 安装 pymysql

pip install pymysql

### (3) 配置数据库

DB_URL = 'mysql+pymysq://root:password@host:port/database'

**实例**

```python
from sqlalchemy import create_engine

#数据库的配置
USER_NAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'flaskdatabase'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USER_NAME,PASSWORD,HOST,PORT,DATABASE)
# print(DB_URI)

#创建操作数据库的引擎
db = create_engine(DB_URI)

#链接数据库
with db.connect() as con:
    # print(con)
    # con.execute('create table user(id int unsigned primary key auto_increment,username varchar(20))')
    # con.execute('insert into user values(null,"zhangsan")')
    pass
#     con.execute(sql语句)
```





## 二、使用ORM

#### (1) 导入

from flask_sqlalchemy import SQLAlchemy #导入ORM

#### (2) 配置数据库的链接地址和设置数据追踪

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flaskdatabase'

\#检测数据是否发生改变 数据追踪 额外消耗资源 设置False 关闭追踪

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#### (3) 实例化ORM

db = SQLAlchemy(app)

**注意：** 所有数据库的配置都要放在实例化之前 否则不会加载

**实例**

```python
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy #导入ORM

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flaskdatabase'
#检测数据是否发生改变 数据追踪 额外消耗资源 设置False 关闭追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#实例化ORM模型
db = SQLAlchemy(app)
manager = Manager(app)

@app.route('/')
def index():
    return 'sqlalchemy'


if __name__ == '__main__':
    manager.run()
```



## 三、设计模型

### (1) 常见字段

| 类型名          | python类型          | 说明           |
| ------------ | ----------------- | ------------ |
| Integer      | int               | 存储整形         |
| Smallinteger | int               | 存储小整形        |
| BigInteger   | int               | 长整形          |
| Float        | float             | 浮点数          |
| String       | str               | 不定长度 varchar |
| Text         | str               | 大型文本 用于文章    |
| Boolean      | bool              | tinyint      |
| Date         | datetime.date     | 日期           |
| time         | datetime.time     | 时间           |
| DateTime     | datetime.datetime | 日期和时间        |

### (2) 可选

| 选项          | 说明             |
| ----------- | -------------- |
| primary_key | 主键索引           |
| unique      | 唯一索引           |
| index       | 常规索引           |
| nullable    | 是否可以为空 默认为True |
| default     | 设置默认值          |

**注意：**

default默认值 并不是将表的字段设置为 default  而是在插入数据的时候 将orm中的默认值插入进去



## 三、创建模型

```python
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy #导入ORM

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flaskdatabase'
#检测数据是否发生改变 数据追踪 额外消耗资源 设置False 关闭追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#实例化ORM模型
db = SQLAlchemy(app)
manager = Manager(app)



#创建一个学生的表
class Students(db.Model):
    #不起名 默认为类名
    __tablename__ = 'stu'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10),index=True)
    sex = db.Column(db.Boolean,default=True)
    age = db.Column(db.Integer)
```

##### 表的创建

```python
@app.route('/create_table/')
def create_table():
    db.create_all()
    return '创建表'
```

**表的删除**

```python
@app.route('/drop_table/')
def create_table():
    db.drop_all()
    return '删除表'
```



## 四、flask MVT的拆分

**目录结构**

```python
project/
	manage.py   #启动文件
    settings.py	#配置文件
    ext.py		#扩展文件
    templates/	#模板文件
    app/
    	models.py  #模型
        view.py 	#视图
```



## 五、数据的增删改查  add add_all delete

**注意：** sqlalchemy默认开启了事物 所以在操作的时候 需要 commit 或者 rollback

### (1) 添加一条数据

```python
#添加一条数据
@view.route('/insert_one/')
def insertOne():
    try:
        stu = Stu(name='张三',sex=False,age=18,info='张三的个人信息')
        db.session.add(stu)
        db.session.commit()#提交
    except:
        db.session.rollback()
    return '数据添加成功'
```

### (2) 添加多条数据

```python
#添加多条数据
@view.route('/insert_many/')
def insertMany():
    stu1 = Stu(name='李'+str(random.randrange(10000,99999)),sex=[True,False][random.randint(0,1)],age=random.randint(10,30),info=str(random.randrange(10000,99999))+'个人简介')
    stu2 = Stu(name='张'+str(random.randrange(10000,99999)),sex=[True,False][random.randint(0,1)],age=random.randint(10,30),info=str(random.randrange(10000,99999))+'个人简介')
    db.session.add_all([stu1,stu2]) #将创建多个数据的对象 放到列表中 执行添加多条数据
    db.session.commit()
    return '添加多条数据'
```

### (3) 数据的修改

```python
#修改数据
@view.route('/update/')
def update():
    s = Stu.query.get(7) #拿到id为7 的数据 返回对象
    # print(s.name)
    # print(s.info)
    s.name = '新的名字'
    db.session.add(s)
    db.session.commit()
    return '修改数据'
```

### (4) 数据的删除

```python
@view.route('/delete/')
def delete():
    #删除id为 6的数据
    s = Stu.query.get(6)
    name = s.name
    db.session.delete(s)
    db.session.commit()
    return '删除数据为{}'.format(name)
```



## 六、自定义修改删除添加的基础类

**实例**

```python
from ext import db

#添加1
#添加多条
#修改
#删除
class NewModel():
    #你认为在保存的时候传入当前对象方便 还是不传参数方便
    #重新定义 add 方法
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    #重新定义 add_all 方法
    @staticmethod
    def save_all(dataList):
        try:
            db.session.add_all(dataList)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    #自定义删除 方法
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()

class Stu(db.Model,NewModel):
    __tablename__ = 'stu'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    sex = db.Column(db.Boolean,default=True)
    age = db.Column(db.Integer)
    info = db.Column(db.String(50))
    def __init__(self,name,sex,age,info):
        self.name = name
        self.age = age
        self.sex = sex
        self.info = info
```

**使用**

##### 添加一条数据

```python
stu = Stu('赵六',False,28,'赵六的个人信息')
stu.save()
```

##### 添加多条数据

```python
stu1 = Stu(name='李'+str(random.randrange(10000,99999)),sex=[True,False][random.randint(0,1)],age=random.randint(10,30),info=str(random.randrange(10000,99999))+'个人简介')
stu2 = Stu(name='张'+str(random.randrange(10000,99999)),sex=[True,False][random.randint(0,1)],age=random.randint(10,30),info=str(random.randrange(10000,99999))+'个人简介')

#使用自定义的添加多条数据的方法
Stu.save_all([stu1,stu2])
return '添加多条数据'
```

##### 删除数据

```python
#删除id为14的数据
s = Stu.query.get(14)
name = s.name
s.delete()
```



## 七、数据库的操作 过滤器

##### 查询集

查询数据的集合

##### 分类

1. 原始查询集

   使用类名.query得到的就是原始查询集

2. 数据查询集

   通过过滤器 过滤后的数据



### (1) all()  得到所有的数据查询集

以列表形式反会所有数据的对象

```python
 data = Stu.query.all()
```

### (2) filter()  添加条件过滤 默认返回所有

条件添加: 类名.query.filter([类名.属性名 条件 值])

```python
@view.route('/filter/')
def myFilter():
    # data = Stu.query.filter()
    # data = Stu.query.filter(Stu.id<10) #查询id小于10的 
    data = Stu.query.filter(Stu.id<10,Stu.sex==False) #查询id小于10 并且为女的
    data = Stu.query.filter(Stu.id<10,Stu).filter(sex==False)
    return render_template('showdata.html',data=data)
```

### (3) filter_by()  只支持单条件查询

**格式:**  类名.query.filter_by(属性名=值[属性名=值...])

默认查询所有

```python
@view.route('/filter_by/')
def filter_by():
    data = Stu.query.filter_by(id=1)
    data = Stu.query.filter_by(sex=False)
    data = Stu.query.filter_by(sex=False,id=10)
    #只能支持关键字参数的形式 名=值  不能存在其他符号 以下为错误的写法
    data = Stu.query.filter_by(sex=False,id>10)
```

### (4) offset(num)  偏移量

**实例**

```python
#取出偏移5条的数据
data = Stu.query.offset(5)
```

### (5) limit(num)  取出num条数据  通常offset和limit配合来使用

**实例**

```python
data = Stu.query.limit(5)
#配合offset使用 过滤5条取5条
data = Stu.query.offset(5).limit(5)
```

### (6) order_by(类名.属性名)  排序

分类：

1. 升序   类名.属性名
2. 降序  -类名.属性名

**实例**

```python
#按照id升序
data = Stu.query.order_by(Stu.id)
#按照id降序
data = Stu.query.order_by(-Stu.id)
#取出id最大的对象
data = Stu.query.order_by(-Stu.id).limit(1)
```

### (7) first()  第一条

```python
#取出查询集中的第一条数据
data = Stu.query.first()
```

### (8) get(id值)查询成功返回查询的对象  失败返回None

```python
data = Stu.query.get(1) #== Stu.query.first()
data = Stu.query.get(100) # 返回  None TypeError: 'NoneType' object is not iterable
```

### (9) contains()  包含关系

**实例**

```python
#select * from stu where name like '%张%'
data = Stu.query.filter(Stu.name.contains('张'))
```

### (10) like(类名.属性名.like('%val%'))  模糊查询

##### 实例

```python
#name包含张的数据
data = Stu.query.filter(Stu.name.like('%张%'))
#以张作为开头
data = Stu.query.filter(Stu.name.like('张%'))
#以张作为结尾
data = Stu.query.filter(Stu.name.like('%张'))
```

### (11) startswith    endswith  以...开头和以...结尾

```python
#以张作为开头
data = Stu.query.filter(Stu.name.startswith('张'))
#以张作为结尾
data = Stu.query.filter(Stu.name.endswith('张'))
```

### (12) 比较运算符

1. `>`
2. `<`
3. `>=`
4. `<=`
5. `==`
6. `!=`
7. `__gt__`  大于
8. `__ge__` 大于等于
9. `__lt__` 小于
10. `__le__` 小于等于

**实例**

```python
#大于18
data = Stu.query.filter(Stu.age.__gt__(18))
data = Stu.query.filter(Stu.age>18)

#大于等于18
data = Stu.query.filter(Stu.age.__ge__(18))
data = Stu.query.filter(Stu.age>=18)

#小于18
data = Stu.query.filter(Stu.age.__lt__(18))
data = Stu.query.filter(Stu.age<18)

#小于等于18
data = Stu.query.filter(Stu.age.__le__(18))
data = Stu.query.filter(Stu.age<=18)
```



### (13) in_ 和 not in  是否在某个范围内

```python
#查询id在 1，3，5的数据
data = Stu.query.filter(Stu.id.in_([1,3,5]))
# 查询id不为 1，3，5的数据
data = Stu.query.filter(~Stu.id.in_([1,3,5]))
```



### (14) is_   isnot  查询为null或者 不为null的数据

```python
#查询 name为null 的数据
# data = Stu.query.filter(Stu.name==None)
# data = Stu.query.filter(Stu.name.is_(None))

#查询 name 不为null 的数据
# data = Stu.query.filter(Stu.name!=None)
# data = Stu.query.filter(~Stu.name.is_(None))
data = Stu.query.filter(Stu.name.isnot(None))
```

## 三、数据库的逻辑查询

### (1) 逻辑与

**导入**

```
from sqlalchemy import and_
```

**实例**

```python
data = Stu.query.filter(Stu.sex==False,Stu.age>18)
data = Stu.query.filter(Stu.sex==False).filter(Stu.age>18)
data = Stu.query.filter(and_(Stu.sex==False,Stu.age>18))
```

### (2) 逻辑或

**导入**

```
from sqlalchemy import or_
```

**实例**

```python
#逻辑或
data = Stu.query.filter(or_(Stu.sex==False,Stu.age>18))
```

### (3) and_ 和 or_的合并写法

```python
data = Stu.query.filter(or_(Stu.sex==False,Stu.age>18),Stu.name.isnot(None))
```

### (4) 逻辑非 not_

```python
data = Stu.query.filter(~Stu.sex==True)
#下面为错误的写法
data = Stu.query.filter(not_(Stu.sex==True,Stu.name.is_(None)))
```

### (5) count()  统计函数

```python
Stu.query.filter(~Stu.sex==True).count()
```



## 四、文件迁移

### (1) 安装

pip  install flask-script

pip install flask-migrate

### (2) 创建迁移对象

```python
from flask_migrate import MigrateCommand,Migrate
migrate = Migrate(app,db) #实例化迁移对象
manager = Manager(app)
manager.add_command('db',MigrateCommand) #添加迁移命令
```

### (3) 创建迁移目录

python manage.py db init

### (4) 生成迁移文件

python manage.py db migrate

### (5) 执行迁移文件（更新数据库）

python manage.py db upgrade

##### 注意:

在创建新的模型类以后 需要先导入再生成迁移文件 否则生成迁移失败





















