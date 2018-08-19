## flask-cache缓存

**作用：** 提高用户的体验度，减少数据库和服务器的压力

### (1) 安装

pip install flask-cache

### (2) 导入进行实例化

```python
from flask_cache import Cache
cache = Cache()

cache.init_app(app=app)
```

### (3) 设置缓存类型

```python
cache = Cache(config={"CACHE_TYPE":'simple'}) #简单的缓存

#缓存在redis中
cache = Cache(config={"CACHE_TYPE":'redis','CACHE_KEK_PREFIX':'python','CACHE_REDIS_PASSWORD':'123456'})
```

### (4) 使用

```python
from app.extensions import cache
@main.route('/')
@cache.cached(timeout=3600,key_prefix='标识符') #添加缓存的装饰器  timeout 为 过期时间
def index():
    print('我是缓存的视图函数-------------')
    pass
```

使用@cache.cached(timeout=3600)装饰器 给当前的视图函数 添加缓存  

**注意：**

##### 但是 当页面通过参数改变数据的时候  此刻是存在问题的

### (5) 通过传递不同的参数进行缓存

```python
@main.route('/show/<int:page>')
@cache.memoize(timeout=3600) #添加缓存的装饰器  timeout 为 过期时间 此缓存是可以通过传递 不同的参数 进行缓存
def show(page):
    pass
```

### (6) 清除缓存

1. 给当前缓存的路由提供timeout参数 进行缓存

2. CACHE_DEFAULT_TIMEOUT  配置过期时间

3. 手动删除缓存

   ```python
   cache.delete('index') #删除缓存 index为设置的缓存前缀
   ```

4. 清除所有缓存

   ```python
   ccache.clear()
   ```

5. memoize删除缓存

   ```python
   cache.delete_memoized(缓存的视图函数的名称)
   cache.delete_memoized(缓存的视图函数的名称，参数)
   cache.delete_memoized(show，5)
   ```

   ​

