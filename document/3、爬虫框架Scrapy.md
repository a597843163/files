### Scrapy 框架安装

pip install scrapy   (工具有链接)

如果出错:

error:Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools

则再执行：

下载twisted对应版本的whl文件（如我的Twisted-17.5.0-cp36-cp36m-win_amd64.whl），cp后面是python版本，amd64代表64位，运行命令：

pip install  twisted   路径 (工具有链接)

### Scrapy框架图解

![scrapy框架](C:\Users\sdsd\Desktop\笔记\img\scrapy框架.png)

![微信截图_20180609103021](C:\Users\sdsd\Desktop\笔记\img\微信截图_20180609103021.png)

### Scrapy的简单使用:

#### 1.创建项目：

scrpay  startproject   项目名

#### 2.创建爬虫文件：

①cd 目标文件

② scrapy	 genspider 	爬虫名 	爬虫链接

如： scrapy genspider qiubai "www.qiushibaike.com"

​	爬虫文件说明:

​	name: 爬虫的名字，启动的时候根据爬虫的名字启动项目

​	allowed_domains：允许的域名，当爬虫时判断是否是这个域名下的url

​	start_urls：爬虫起始url，里面可以写多个，一般只写一个

#### 3.item.py	

要爬取内容字段

如:  name = Scrapy.Field()

#### 4.打印response对象  

第一次使用需安装 pywin32（工具）

scrapy  crawl  qiubai 

​	根据response  获取网页内容
​	text    字符串类型
​	body    二进制类型

​	url：所请求的url
​	status：响应的状态码

#### 5.保存爬取内容到文件

​	scrapy crawl xxx -o data.json

​	如果需要定制保存格式，或者保存到数据库，在pipelines.py下写代码即可

### Scrapy Shell

说明:可以用来调试代码，在还未开始爬虫之前

使用：

1.进入shell  模式

scrapy shell  "网页url"  此处要用双引号

加头部信息 加上  -s USER_AGENT.....  即可

### 爬取电影天堂实例:

主文件   dytt.py

```python
# -*- coding: utf-8 -*-
import re
import scrapy
from movie.items import MovieItem
import os

class DyttSpider(scrapy.Spider):
    name = 'dytt'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        table_list = response.xpath('//table[contains(@class, "tbspan")]')
        for table in table_list:
            title = table.xpath('.//a/text()').extract_first()
            brief = table.xpath('.//tr[last()]/td/text()').extract_first()
            link = "http://www.ygdy8.net" + table.xpath('.//a/@href').extract_first()
            #  使用之前要在item注册
            item = MovieItem()
            item['title'] = title
            item['brief'] = brief
            item['link'] = link
            # 每一个link点进去，然后获取下载资源的url
            # 最大页码
            pattern = re.compile(r'共(\d+)页')
            max_page = int(pattern.findall(response.text)[0])
            # 这里面涉及到一个传递item的问题，我们要学习如何传参,加上一个meta参数，meta参数是一个字典，过去之后，通过字典的键获取其值
            yield scrapy.Request(url=link, callback=self.movie_url, meta={'item': item})

        for page in range(2, max_page+1):
            url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_%d.html' % page
            # 回调函数parse
            yield scrapy.Request(url, callback=self.parse)

    def movie_url(self,response):
        item = response.meta['item']
        movie_url = response.xpath('//td[@bgcolor="#fdfddf"]/a/text()').extract_first()
        if not movie_url:
            movie_url = response.xpath('//td[@bgcolor="#fdfddf"]/font/a/@href').extract_first()
            if not movie_url:
                movie_url = response.xpath('//td[@bgcolor="#fdfddf"]/span/a/@href').extract_first()
        item['movie_url'] = movie_url
        yield item
```

items.py代码

```python
class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 下面注册的字段都是需要爬取的内容字段
    title = scrapy.Field()
    brief = scrapy.Field()
    link = scrapy.Field()
    movie_url = scrapy.Field()
```

pipelines.py  

将爬取的内容输出到dytt.txt文件上

```python
class MoviePipeline(object):
    def open_spider(self, spider):
        self.f = open('./dytt.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()
```

setting.py修改

```python
# 设置头部信息
(18)USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'

(22)使爬虫不遵守robots.txt规则
ROBOTSTXT_OBEY = False

# 默认请求头添加上
(42)DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}
# 使用pipelines上的类
(66)ITEM_PIPELINES = {
   'movie.pipelines.MoviePipeline': 300,
}
```

#### 存入mysql中：

修改保存路径和setting就可以了

pipelines.py代码:

```python
class DushuMySqlPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.host = settings.get('DB_HOST')
        self.port = settings.get('DB_PORT')
        self.user = settings.get('DB_USER')
        self.password = settings.get('DB_PASSWORD')
        self.db = settings.get('DB_DB')
        self.charset = settings.get('DB_CHARSET')
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into novels(name, author, brief) values("%s", "%s", "%s")' % (item['name'], item['author'], item['brief'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
```

​	settings代码:

```python
ITEM_PIPELINES = {
    'dushu.pipelines.DushuMySqlPipeline': 200,
}

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_DB = 'books'
DB_CHARSET = 'utf8'
```

### Scrapy CrawlSpider（分页）

说明:当多页爬取时，最好使用这个框架

规则使用：

```python
链接提取器，在这里就可以写规则提取指定链接
scrapy.linkextractors.LinkExtractor(
	 allow = (),    # 正则表达式  提取符合正则的链接
	 deny = (),     # (不用)正则表达式  不提取符合正则的链接
	 allow_domains = (),  # （不用）允许的域名
	 deny_domains = (),   # （不用）不允许的域名
	 restrict_xpaths = (), # xpath，提取符合xpath规则的链接
	 restrict_css = ()  # 提取符合选择器规则的链接)
	 
# 例子：
正则用法：links1 = LinkExtractor(allow=r'list_23_\d+\.html')
xpath用法：links2 = LinkExtractor(restrict_xpaths=r'//div[@class="x"]')
css用法：links3 = LinkExtractor(restrict_css='.x')

!!!使用!!!:
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
class  spider(CrawlSpider):
  rules = (
         Rule(LinkExtractor(allow=r'/book/1163_\d+\.html'), callback='parse_item', follow=False),
  )
   注意：callback回调函数，不能为parse！！！！
```

### Scrapy-Post请求:

#### 访问百度:

```python
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']

    # 必须是start_request  函数！！！！
    def start_requests(self):
        post_url = 'http://fanyi.baidu.com/sug'
        formdata = {
            'kw':'hello'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
        }
        yield scrapy.FormRequest(url=post_url, formdata=formdata, headers=headers)

    def parse(self, response):
        with open('./baidu.txt', 'w', encoding='utf-8') as fp:
            fp.write(json.dumps(json.loads(response.text), ensure_ascii=False))
        # print(response.text)
```

#### 代理设置:

​	spider.py:

访问百度ip，可以看到是否成功设置代理

```python
class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=ip']

    def parse(self, response):
        with open('./baidu.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)
        return []
```

middlewares.py

！！！需要在访问之前设置中间件

```python
class ProxyMiddleware(object):
    def process_request(self, request, spider):
      # 设置代理
        request.meta['proxy'] = 'https://118.212.137.135:31288'
        return None
```

settings.py

打开这个,使用中间件

```python
 DOWNLOADER_MIDDLEWARES = {
    'postproject.middlewares.ProxyMiddleware': 543,
 }
```

#### 携带cookie访问:

不再需要创建cookiejar

spider.py:

```python
import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = ['https://weibo.cn/']

    def start_requests(self):
        headers = {
            'Host': 'weibo.cn',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'https://weibo.cn/',
            'Accept-Language': 'zh-CN,zh;q=0.8',

        }

        data = {
            'username': '18676689715',
            'password': 'xuke666',
            'savestate': '1',
            'r': 'http://weibo.cn/',
            'ec': '0',
            'pagerefer': '',
            'entry': 'mweibo',
            'wentry': '',
            'loginfrom': '',
            'client_id': '',
            'code': '',
            'qq': '',
            'mainpageflag': '1',
            'hff': '',
            'hfp': ''
        }
        post_url = 'https://passport.weibo.cn/sso/login'

        yield scrapy.FormRequest(url=post_url, headers=headers, formdata=data, callback=self.user_info)

    def user_info(self, response):
        url = 'https://weibo.cn/2952685222/info'

        yield scrapy.Request(url=url, callback=self.save_info)

    def save_info(self, response):
        with open('./weibo.html', 'w', encoding='gbk') as fp:
            fp.write(response.text)
```

settings.py

```python
COOKIES_ENABLED = True
```

### Scrapy-redis

#### 存数据到数据库

图解：

![scrapy-redis](C:\Users\sdsd\Desktop\笔记\img\scrapy-redis.png)

做完配置，就可以存数据到redis了

settings.py：

```python
# 调度器使用是scrapy_redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用的是scrapy_redis的去重类
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 爬取的过程中是否允许暂停
SCHEDULER_PERSIST = True

# 说明使用redis来存储数据
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 100,
}

# 配置存储的redis服务器
REDIS_HOST = '10.36.137.6'
REDIS_PORT = 6379

```

#### 分布式爬虫

当爬取数据量大的时候，使用分布式爬虫

```
from scrapy_redis.spiders import RedisCrawlSpider
```

1.  spider中 下面代码不能再有

    allowed_domains = ['weibo.cn']
    start_urls = ['https://weibo.cn/']

2.替换成

意味着start_urls  由redis来发放

```
redis_key = 'novel_redis:start_urls'    novel_redis是爬虫名字
```

3.启动分布式爬虫命令

​	启动redis并且关掉保护模式

​	redis-server --protected-mode no

cd  spider 文件夹下

命令:scrapy runspider novel_redis.py

完成！！！

等待redis发放url

在redis中加入key-value

lpush   novel_redis:start_urls  'https://www.dushu.com/book/1078.html'

![微信图片编辑_20180609125554](C:\Users\sdsd\Desktop\笔记\img\微信图片编辑_20180609125554.jpg)