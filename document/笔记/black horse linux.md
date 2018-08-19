### black horse

#### 基本命令

命令	选项	参数

ls		-a，显示隐藏文件

​		-l ,   以列表显示，文件的进程全显示

​		-h,   可以看到文件大小

ll 	相当于 ls -la

（*） 和 ？都表示通配符

重定向  >   比方ls > xxx.txt		>>  追加到xxx.txt上（不覆盖）

表示把ls的内容写入(定到)xxx.txt（先覆盖）

mkdir  -p  A/B/C/D  自动创建

find命令的使用

![QQ截图20180416163511](C:\Users\sdsd\Desktop\笔记\img\QQ截图20180416163511.jpg)

tar 命令  指定路径 -C

打包命令  tar -cvf 新文件名.tar  文件名   如 tar -cvf test.tar *.py

打包并压缩命令  

1.tar -zcvf 新文件名.tar.gz  文件名    

tar -zcvf  test.tar.gz  *.py

2.压缩方式(比gz更大)	tar -jcvf 新文件名.tar.bz2  文件名

如 	tar -jcvf  test.tar.bz2  *.py

解压   

1.tar -zxvf  文件名   如  tar-zxvf test.tar.gz

2.tar -jxvf  文件名   如  tar-jxvf test.tar.bz2

不常见的压缩    指定路径-d

zip压缩	zip  新文件名.zip 被压缩文件名 zip zzz.zip *.py

解压	unzip	文件名

which 	找使用命令在哪个路径  如 which  ls

cal	查当前日历

​	cal	-y	2008	查看2008年的日历

date 查看当前时间

​	打印特殊格式

date	“+%Y ------%m------%d”

ps	-aux	查看所有的进程

top   监测所有的进程

htop	

kill -9  pid  杀死程序

df	-h   显示硬盘使用情况

du	-h	显示当前路径使用情况

ifconfig	查看当前网络状态

ifconfig	网卡名(ens33)    ip  设置网络ip

whoami		查看现在登陆的用户名

新建终端	

ctrl   +shift  +T	

切换连接

alt	+ 1.....

useradd  gebilaowang -m  表示  创建完用户之后顺便创建home目录

userdel	-r gebilaowang	表示删除完用户顺便删除home目录

who   表示显示当前登陆的用户，带ip的是远程登陆

chmod  u =x 文件名    表示修改组的权限

#### VIM

![切换模式](C:\Users\sdsd\Desktop\笔记\img\切换模式.jpg)

##### 移动光标

h←  j↓  k→  l↑

M：当前屏幕的中间

H：当前屏幕的上方

L：当前屏幕的下方

w:向后跳一个单词的长度

b：像前跳一个单词的长度

20G：跳到20G

gg：跳到第一行

G：跳到末尾

ctrl+f  往下翻一页

ctrl+b 往上翻一页



##### 删除命令

dd:   剪切一行

3dd  剪切从光标开始向下3行

dw：删除一个单词

D：从当前的光标开始剪切，一直到行末

d0：从当前光标开始剪切，一直到行首

x：删除当前的光标，每次只会删除一个

X：删除光标前一个元素，每次只会删除一个



##### 撤销命令

u：撤销刚刚的操作

ctrl+r：反撤销

##### 重复命令

.：重复执行上一次的命令

##### 文本行移动

(>>):向右移动代码

(<<):向左移动代码

##### 复制粘贴

yy：复制光标所在的一行

4yy  复制光标所在行开始向下复制4行

p：粘贴

##### 查找操作

 /+查找字符串

##### 替换操作

r：替换一个字母

R：从当前光标开始往后替换

多行替换

![替换](C:\Users\sdsd\Desktop\笔记\img\替换.jpg)

##### 可视模式

###### 选中一片代码

​	v：

​	V：



#### 备份数据库

msqldump -uroot -p123  axf(库名) > axf_1.sql(生成的备份名)

加载sql文件

source     axf_1.sql (文件名)

看数据库的字符集

 show create database homework2;

修改数据库字符集

alter database homework2 default character set gbk;

查看表的结构,包括引擎

show create table people;