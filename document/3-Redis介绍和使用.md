## 1.  Redis 介绍



####              实现缓存的方式，有多种，本地内存缓存，数据库缓存，文件系统缓存。这里介绍使用Redis数据库进行缓存。



Redis是什么？

​      REmote DIctionary Server(Redis) 是一个由Salvatore Sanfilippo写的key-value存储系统。

​      Redis是一个开源的使用ANSI C语言编写、遵守BSD协议、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。

​      它通常被称为数据结构服务器，因为值（value）可以是 字符串(String), 哈希(Map), 列表(list), 集合(sets) 和 有序集合(sorted sets)等类型。



Redis 简介

Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。

Redis 与其他 key - value 缓存产品有以下三个特点：

- Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
- Redis不仅仅支持简单的key-value类型的数据(memcache)，同时还提供list，set，zset，hash等数据结构的存储。
- Redis支持数据的备份，即master-slave模式的数据备份。



## 2 Redis 优势

- 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
- 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
- 原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。
- 丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。





### 3 安装Redis

 wget http://download.redis.io/releases/redis-3.2.6.tar.gz

解压：

tar -zxvf redis-3.2.6.tar.gz

cd redis-3.2.6



编译：

cd redis-3.2.6  #进入目录
make   #编译



设置redis

mkdir /usr/local/redis #创建redis操作目录
cp src/redis-server src/redis-cli /usr/local/redis/bin/  #复制redis服务和命令
cp redis.conf /usr/local/redis/conf   #复制redis配置文件
cd /usr/local/redis
./bin/redis-server     conf/redis.conf    &    #后台启动redis



**创建快捷键**

vim  ~/.bashrc
alias redis='/usr/local/redis/bin/redis-cli'  #添加快捷键
source ~/.bashrc   #使生效





redis远程连接

**redis-cli  -h  172.16.245.xxx  -p 6379** 

redis 172.16.245.179:6379> 



安装验证成功！





### 4  配置文件

redis.conf 配置项说明如下：

\1. Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程

​    **daemonize no**

\2. 当Redis以守护进程方式运行时，Redis默认会把pid写入/var/run/redis.pid文件，可以通过pidfile指定

​    **pidfile /var/run/redis.pid**

\3. 指定Redis监听端口，默认端口为6379，作者在自己的一篇博文中解释了为什么选用6379作为默认端口，因为6379在手机按键上MERZ对应的号码，而MERZ取自意大利歌女Alessia Merz的名字

​    **port 6379**

\4. 绑定的主机地址

​    **bind 127.0.0.1**

5.当 客户端闲置多长时间后关闭连接，如果指定为0，表示关闭该功能

​    **timeout 300**

\6. 指定日志记录级别，Redis总共支持四个级别：debug、verbose、notice、warning，默认为verbose

​    **loglevel verbose**

\7. 日志记录方式，默认为标准输出，如果配置Redis为守护进程方式运行，而这里又配置为日志记录方式为标准输出，则日志将会发送给/dev/null

​    **logfile stdout**

\8. 设置数据库的数量，默认数据库为0，可以使用SELECT <dbid>命令在连接上指定数据库id

​    **databases 16**

\9. 指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合

​    **save <seconds> <changes>**

​    Redis默认配置文件中提供了三个条件：

​    **save 900 1**

**    save 300 10**

**    save 60 10000**

​    分别表示900秒（15分钟）内有1个更改，300秒（5分钟）内有10个更改以及60秒内有10000个更改。

 

\10. 指定存储至本地数据库时是否压缩数据，默认为yes，Redis采用LZF压缩，如果为了节省CPU时间，可以关闭该选项，但会导致数据库文件变的巨大

​    **rdbcompression yes**

\11. 指定本地数据库文件名，默认值为dump.rdb

​    **dbfilename dump.rdb**

\12. 指定本地数据库存放目录

​    **dir ./**

\13. 设置当本机为slav服务时，设置master服务的IP地址及端口，在Redis启动时，它会自动从master进行数据同步

​    **slaveof <masterip> <masterport>**

\14. 当master服务设置了密码保护时，slav服务连接master的密码

​    **masterauth <master-password>**

\15. 设置Redis连接密码，如果配置了连接密码，客户端在连接Redis时需要通过AUTH <password>命令提供密码，默认关闭

​    **requirepass foobared**

\16. 设置同一时间最大客户端连接数，默认无限制，Redis可以同时打开的客户端连接数为Redis进程可以打开的最大文件描述符数，如果设置 maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis会关闭新的连接并向客户端返回max number of clients reached错误信息

​    **maxclients 128**

\17. 指定Redis最大内存限制，Redis在启动时会把数据加载到内存中，达到最大内存后，Redis会先尝试清除已到期或即将到期的Key，当此方法处理 后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。Redis新的vm机制，会把Key存放内存，Value会存放在swap区

​    **maxmemory <bytes>**

\18. 指定是否在每次更新操作后进行日志记录，Redis在默认情况下是异步的把数据写入磁盘，如果不开启，可能会在断电时导致一段时间内的数据丢失。因为 redis本身同步数据文件是按上面save条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认为no

​    **appendonly no**

\19. 指定更新日志文件名，默认为appendonly.aof

​     **appendfilename appendonly.aof**

\20. 指定更新日志条件，共有3个可选值： 
​    **no**：表示等操作系统进行数据缓存同步到磁盘（快） 
​    **always**：表示每次更新操作后手动调用fsync()将数据写到磁盘（慢，安全） 
​    **everysec**：表示每秒同步一次（折衷，默认值）

​    **appendfsync everysec**

 

\21. 指定是否启用虚拟内存机制，默认值为no，简单的介绍一下，VM机制将数据分页存放，由Redis将访问量较少的页即冷数据swap到磁盘上，访问多的页面由磁盘自动换出到内存中（在后面的文章我会仔细分析Redis的VM机制）

​     **vm-enabled no**

\22. 虚拟内存文件路径，默认值为/tmp/redis.swap，不可多个Redis实例共享

​     **vm-swap-file /tmp/redis.swap**

\23. 将所有大于vm-max-memory的数据存入虚拟内存,无论vm-max-memory设置多小,所有索引数据都是内存存储的(Redis的索引数据 就是keys),也就是说,当vm-max-memory设置为0的时候,其实是所有value都存在于磁盘。默认值为0

​     **vm-max-memory 0**

\24. Redis swap文件分成了很多的page，一个对象可以保存在多个page上面，但一个page上不能被多个对象共享，vm-page-size是要根据存储的 数据大小来设定的，作者建议如果存储很多小对象，page大小最好设置为32或者64bytes；如果存储很大大对象，则可以使用更大的page，如果不 确定，就使用默认值

​     **vm-page-size 32**

\25. 设置swap文件中的page数量，由于页表（一种表示页面空闲或使用的bitmap）是在放在内存中的，，在磁盘上每8个pages将消耗1byte的内存。

​     **vm-pages 134217728**

\26. 设置访问swap文件的线程数,最好不要超过机器的核数,如果设置为0,那么所有对swap文件的操作都是串行的，可能会造成比较长时间的延迟。默认值为4

​     **vm-max-threads 4**

\27. 设置在向客户端应答时，是否把较小的包合并为一个包发送，默认为开启

​    **glueoutputbuf yes**

\28. 指定在超过一定的数量或者最大的元素超过某一临界值时，采用一种特殊的哈希算法

​    **hash-max-zipmap-entries 64**

**    hash-max-zipmap-value 512**

\29. 指定是否激活重置哈希，默认为开启（后面在介绍Redis的哈希算法时具体介绍）

​    **activerehashing yes**

\30. 指定包含其它的配置文件，可以在同一主机上多个Redis实例之间使用同一份配置文件，而同时各个实例又拥有自己的特定配置文件

​    **include /path/to/local.conf**

查看配置信息

```
redis 127.0.0.1:6379> CONFIG GET *
```



### 5  Redis数据类型

## String（字符串）

​     string是redis最基本的类型，你可以理解成与Memcached一模一样的类型，一个key对应一个value。

string类型是二进制安全的。意思是redis的string可以包含任何数据。比如jpg图片或者序列化的对象 。

string类型是Redis最基本的数据类型，一个键最大能存储512MB。

### 实例

```
redis 127.0.0.1:6379> SET name "1000phone"
OK
redis 127.0.0.1:6379> GET name
"1000phone"
```



## Hash（哈希）

Redis hash 是一个键值(key=>value)对集合。

Redis hash是一个string类型的field和value的映射表，hash特别适合用于存储对象。

### 实例

```
redis> HMSET myhash field1 "Hello" field2 "World"
"OK"
redis> HGET myhash field1
"Hello"
redis> HGET myhash field2
"World"
```

redis 172.16.245.179:6379> hgetall myhash
1) "fd1"
2) "value1"
3) "fd2"
4) "value2"
5) "fd3"
6) "value2"



fd1                   fd2               fd3

value1            value2          value3



## List（列表）

Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。

### 实例

```
redis 127.0.0.1:6379> lpush name  redis
(integer) 1
redis 127.0.0.1:6379> lpush name mongodb
(integer) 2
redis 127.0.0.1:6379> lpush name rabitmq
(integer) 3
redis 127.0.0.1:6379> lrange name 0 10
1) "rabitmq"
2) "mongodb"
3) "redis"
redis 127.0.0.1:6379> rpop name
```



## Set（集合）

Redis的Set是string类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。

### sadd 命令

添加一个 string 元素到 key 对应的 set 集合中，成功返回1，如果元素已经在集合中返回 0，如果 key 对应的 set 不存在则返回错误。

```
sadd key member
```

### 实例

```
redis 127.0.0.1:6379> sadd name redis
(integer) 1
redis 127.0.0.1:6379> sadd name mongodb
(integer) 1
redis 127.0.0.1:6379> sadd name rabitmq
(integer) 1
redis 127.0.0.1:6379> sadd name rabitmq
(integer) 0
redis 127.0.0.1:6379> smembers name

1) "redis"
2) "rabitmq"
3) "mongodb"
```



## zset(sorted set：有序集合)

Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

zset的成员是唯一的,但分数(score)却可以重复。

### zadd 命令

添加元素到集合，元素在集合中存在则更新对应score

```
zadd key score member 
```

### 实例

```
redis 127.0.0.1:6379> zadd runoob 0 redis
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 mongodb
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabitmq
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabitmq
(integer) 0
redis 127.0.0.1:6379> > ZRANGEBYSCORE runoob 0 1000
1) "mongodb"
2) "rabitmq"
3) "redis"
```



### 6  Redis 发布订阅

​      Redis 发布订阅(pub/sub)是一种消息通信模式：发送者(pub)发送消息，订阅者(sub)接收消息。

Redis 客户端可以订阅任意数量的频道。

​     下图展示了频道 channel1 ， 以及订阅这个频道的三个客户端 —— client2 、 client5 和 client1 之间的关系：

![pubsub1](pubsub1.png)



当有新消息通过 PUBLISH 命令发送给频道 channel1 时， 这个消息就会被发送给订阅它的三个客户端：



![pubsub2](pubsub2.png)

------

## 实例

以下实例演示了发布订阅是如何工作的。在我们实例中我们创建了订阅频道名为 **redisChat**:

```
redis 127.0.0.1:6379> SUBSCRIBE redisChat

Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "redisChat"
3) (integer) 1
```

现在，我们先重新开启个 redis 客户端，然后在同一个频道 redisChat 发布两次消息，订阅者就能接收到消息。

```
redis 127.0.0.1:6379> PUBLISH redisChat "Redis is a great caching technique"

(integer) 1

redis 127.0.0.1:6379> PUBLISH redisChat "Learn redis by runoob.com"

(integer) 1

# 订阅者的客户端会显示如下消息
1) "message"
2) "redisChat"
3) "Redis is a great caching technique"
1) "message"
2) "redisChat"
3) "Learn redis by runoob.com"
```





## 7  Python操作Redis

### **安装redis-py**

```
pip install redis
```

redis-py 的API的使用可以分类为：

- 连接方式

- 连接池

- 操作

  - String 操作
  - Hash 操作
  - List 操作
  - Set 操作
  - Sort Set 操作

- 管道

  redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类

  ​

```
import redis
 
r = redis.Redis(host='192.168.49.130', port=6379)
r.set('foo', 'Bar')
print r.get('foo')
```



**创建连接池**:

　　redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
import redis
 
pool = redis.ConnectionPool(host='192.168.49.130', port=6379)
 
r = redis.Redis(connection_pool=pool)
#r = redis.StrictRedis(connection_pool=pool) #StrictRedis也是支持的
r.set('foo', 'Bar')
print r.get('foo')
```



MySQL数据有两种存储引擎：

MyISAM   — 表锁

INONDB   — 表行锁   ———这种存储方式推荐使用， 支持事务



### 8  应用场景案例



（1）页面点击数

​     假定我们对一系列页面需要记录点击次数。例如论坛的每个帖子都要记录点击次数，而点击次数比回帖的次数的多得多。如果使用关系数据库来存储点击，可能存在大量的行级锁争用。所以，点击数的增加使用redis的INCR命令最好不过了。

​     当redis服务器启动时，可以从关系数据库读入点击数的初始值（1237这个页面被访问了34634次）

```
>>> r.set("visit:1237:totals",34634)

True
```

每当有一个页面点击，则使用INCR增加点击数即可。

```
>>> r.incr("visit:1237:totals")

34635

>>> r.incr("visit:1237:totals")

34636

页面载入的时候则可直接获取这个值

>>> r.get ("visit:1237:totals")

'34636'
```



（2）使用hash类型保存多样化对象，类似二维表结构

当有大量类型文档的对象，文档的内容都不一样时，（即“表”没有固定的列），可以使用hash来表达。

```
>>> r.hset('users:jdoe',  'name', "John Doe")

1L

>>> r.hset('users:jdoe', 'email', 'John@test.com')

1L

>>> r.hset('users:jdoe',  'phone', '1555313940')

1L

>>> r.hincrby('users:jdoe', 'visits', 1)

1L

>>> r.hgetall('users:jdoe')

{'phone': '1555313940', 'name': 'John Doe', 'visits': '1', 'email': 'John@test.com'}

>>> r.hkeys('users:jdoe')

['name', 'email', 'phone', 'visits']
```



（3）社交圈子数据

​      在社交网站中，每一个圈子(circle)都有自己的用户群。通过圈子可以找到有共同特征（比如某一体育活动、游戏、电影等爱好者）的人。当一个用户加入一个或几个圈子后，系统可以向这个用户推荐圈子中的人。
​     我们定义这样两个圈子,并加入一些圈子成员。

```
>>> r.sadd('circle:game:lol','user:debugo')
1
>>> r.sadd('circle:game:lol','user:leo')
1
>>> r.sadd('circle:game:lol','user:Guo')
1
>>> r.sadd('circle:soccer:InterMilan','user:Guo')
1
>>> r.sadd('circle:soccer:InterMilan','user:Levis')
1
>>> r.sadd('circle:soccer:InterMilan','user:leo')
1
```



获取一个圈子的成员

```
>>> r.smembers('circle:game:lol')
set(['user:Guo', 'user:debugo', 'user:leo'])
```



可以使用集合运算来得到几个圈子的共同成员：

```
>>> r.sinter('circle:game:lol', 'circle:soccer:InterMilan')
set(['user:Guo', 'user:leo'])
>>> r.sunion('circle:game:lol', 'circle:soccer:InterMilan')
set(['user:Levis', 'user:Guo', 'user:debugo', 'user:leo'])

```





