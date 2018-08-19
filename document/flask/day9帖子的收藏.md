## 帖子的收藏

## 一、创建多对多的中间表

```python
#创建一个关联帖子和用户的中间表
collections = db.Table('collections',
    db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
    db.Column('posts_id',db.Integer,db.ForeignKey('posts.id'))
)
```

user.py模型中的修改

```python
#参数1 为模型名称
    #参数2  secondary 在多对多关系模型中指定要选择的关联表名称
    #参数3  设置反向引用字段  加载时机
favorites= db.relationship('Posts',secondary='collections',backref=db.backref('users',lazy='dynamic'),lazy='dynamic')
```

## 二、表的多对多的操作

### (1) 添加收藏

```python
#1号用户 收藏了2号提诶
u = User.query.get(1)
p = Posts.query.get(2)
u.favorites.append(p) #1号用户收藏了1号帖子
```

### (2) 查看收藏

```python
#查看用户1 收藏了哪些帖子
u = User.query.get(1)
print(u.favorites.all()) #查询当前id为1的用户有哪些收藏的帖子
```

### (3) 查看帖子都被谁收藏了

```python
#查看2 号帖子都被谁收藏了
p = Posts.query.get(2)
print(p.users.all())  #获取帖子都被谁收藏了
```

### (4) 取消收藏

```python
#取消收藏
u = User.query.get(1)
p = Posts.query.get(2)
u.favorites.remove(p) #取消收藏 2号帖子
```



### 晚上：

1. 我收藏过的
2. 最近浏览
3. 搜索
4. 帖子的排序
5. 将轮播图变成活的
6. 我发布过的帖子
7. 将请求错误进行捕获（定义404等，的模板页面）





## restful

**概念：**

一个架构符合REST的约束条件和原则，我们就称它为RESTful架构。



## GET，DELETE，PUT和POST的典型用法:

| 方法     | 行为      | 例子                               |
| ------ | ------- | -------------------------------- |
| GET    | 获取所有的资源 | http://127.0.0.1:5000/source     |
| GET    | 获取指定的资源 | http://127.0.0.1:5000/source/250 |
| POST   | 创建新的资源  | http://127.0.0.1:5000/source     |
| PUT    | 更新指定的资源 | http://127.0.0.1:5000/source/250 |
| DELETE | 删除指定资源  | http://127.0.0.1:5000/source/250 |