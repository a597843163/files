#### 字段类型

数字:int    

decimal(5,2) 一共包含5位数，小数包含2位   表示浮点数

tinyint

字符串：char（8）    固定大小8，不够补空格

varchar（8）   最多8，不够不补空格

text 大文本

日期：datetime

布尔：bit   如0,1   male  female

#### 约束

主键 primary key

非空not null

唯一 unique

默认default

外键foreign key

外键创建的方式

foreign key(A表字段)  references(引用)  表名(B主键)

一般先建立关系，再创建外键，进行约束

#### 数据库操作

创建数据库：create database 数据库名   charset=utf8；

删除数据库：drop database  数据库；

切换：           use  数据库；

查看当前所有的数据库 ：show database;

#### 表操作

显示当前数据库所有的表：show tables；

创建表： create table students(

​	id int auto_increment primary key not null,

​	name varchar(10) not null;

)

查看表: desc students；

修改表： alter table 表名 add|change|drop 列名  类型；

更改表名：rename table 原表名 to 新表名；

清空表:  truncate table 表名;  auto_increment也清空;（千万别这么做）

引用外部sql文件

source  文件名



#### 数据（字段）操作

查询

select  * from 表名；

全列插入：insert into 表名 values（...）  注意，添加顺序一致，且数量一致；

缺省插入：insert into 表名(列1，...) values(值1..)，(...),(...);

修改

一个表更新

update 表名 set 列1=值1  where  条件

两个表同时更新

update 表1,表2 set 字段1=值1, …, 字段n=值n where 条件

删除

delete from 表名   where   条件





#### ※查询

消除重复行 ：select distinct 语句 

##### 条件

比较运算符   >  大于   >=  大于等于

​		      <  小于   <=  小鱼等于

​		      ！= 或者<>    不等于

逻辑运算符

​		and  且

​		or    或

​		not  不是

###### 模糊查询like

​		like   

​		% 表示任意多个字符

​		_   表示一个任意字符

where name like  '_静%'

###### 范围查询in,betwenn,null

​		in  表示在一个非连续的范围内

​		查询编号是1或者3或者8

where id in(1,3,8);

​		between ...and...表示一个连续范围内

​		查询编号3至8的信息

where id  between 3  and 8;

​		null  判断空字段

where address is null  判断没有填地址的信息

##### 聚合

​	count(*) 计算总行数

​	max(id)   计算id最大值

​	min(id)    计算id最小值

​	sum(id)    计算id的和

​	avg(id)    计算id的平均值

###### 分组

select 列1,列2,聚合 ...from 表名 group by 列1,列2

where筛选和having筛选![微信图片编辑_20180418202905](C:\Users\sdsd\Desktop\笔记\img\微信图片编辑_20180418202905.jpg)

###### 排序

order by   

select * from 表名 order by 列1 asc(默升)|desc ，列2 asc|desc,....

##### 分页

limit  start ,count    从索引start 开始，拿count数量

已知每页显示m条数据，当前在第n页

拿的数据为

limit (n-1)*m , m

##### 完整select语句

select distinct *

from   表名

where ...

group by  ... having ...

order by  ...

limit  star，count

select顺序

![微信图片编辑_20180418202905](C:\Users\sdsd\Desktop\笔记\img\微信图片编辑_20180418202905.jpg)



##### 关系链接

###### join外链接

1.select * from 表名1   inner join 需链接的表名2 on  关系

如select  Star.name ,  Car.name  from Star innner jonin  Car on Star.car_id=Car.id

innner匹配两者都有的

2.select * from 表名   left join 需链接的表名 on  关系

left匹配以左边·	为主的，第一部分为两者都有，第二部分为左边独有的

3.2.select * from 表名   right  join 需链接的表名 on  关系

right匹配以右边为主的，第一部分为两者都有，第二部分为右边独有的

###### where显示外链接

select * from 表1,表2   where  关系

select  *  from Star,Car where Star.car_id=Car.id;

##### 两个表联合

select *from Star union select  *  from MovieStar;

##### 自引用/自关联

![QQ截图20180419193605](C:\Users\sdsd\Desktop\笔记\img\QQ截图20180419193605.jpg)

![QQ图片20180419193539](C:\Users\sdsd\Desktop\笔记\img\QQ图片20180419193539.png)



#### 视图

封装表结果,快照,不能修改,类似把查询结果拍了个照

create  view  视图名    语句

create view v_1 as

select students.*,scores.score,subjects.title from scores 

inner join students on scores.stuid=students.id

inner join subjects on scores.subid=subjects.id;

使用视图

select * from v_1

#### 事务

begin;   开始事务   或者(start   transaction)

rollback;  回滚  放弃操作

commit;   提交  成功操作

#### 索引

create index 索引名字 on 表名 (字段名字1(长度)，....)

删除索引

drop   index   [索引名字]  on  表名



#### 用户操作

创建

 Create user ‘用户名’@‘用户地址’ identified by ‘密码’;

 如：create user 'laixin'@'127.0.0.1' identified by '123';

删除

drop user 'test'@'127.0.0.1';

修改权限

grant 权限  on 表对应字段(全部表示*   .  *)  to 'laixin'@'127.0.0.1';

收回权限

 revoke 权限 on *.*  from ‘用户名’@‘用户地址’;

![6ABE829CF8A50F644BD74DA4AA35C9F5](C:\Users\sdsd\Desktop\笔记\img\6ABE829CF8A50F644BD74DA4AA35C9F5.png)

![27342F38D8997C6EDB810A13461D8717](C:\Users\sdsd\Desktop\笔记\img\27342F38D8997C6EDB810A13461D8717.png)

#### 安全模式打开

SET SQL_SAFE_UPDATES = 0;

#### 备份与恢复

1.超级管理员权限

2.cd /var/lib/mysql

3.运行命令

备份:mysqldump -uroot -p密码  数据库名 > 位置/*.sql

恢复:mysqldump -uroot -p密码  数据库名 < 位置/*.sql



