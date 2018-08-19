周三

1. 文件上传
2. 发表博客（一对多的关系）
3. 分页
4. 无限极分类（类别的添加删除展示 后期的楼层的评论）

周四

1. restful
2. flask-cache
3. 帖子的收藏（多对多）
4. 自己将flask上线或者复习

周五     考试



# 博客管理

## 一、文件上传

1. 修改密码 （输入密码问题/输入原密码 输入新密码）
2. 修改邮箱
3. 激活入口
4. 个人信息的显示

#### 上传的表单

```python

class UploadForm(FlaskForm):
    icon = FileField('修改头像',validators=[FileRequired('请选择文件'),FileAllowed(file,message='只能上传图片')])
    submit = SubmitField('上传图片')
```

#### 修改头像的路由

```python
#生成随机的图片名称
def random_picname(shuffix):
    Str = string.ascii_letters+'0123456789'
    newName = ''.join(random.choices(Str,k=32))+shuffix
    return newName

@user.route('change_icon',methods=['GET','POST'])
def change_icon():
    """
    1. 上传的表单
    2.渲染模板
    3.拿到后缀
    4.导入生成随机图片名称的函数
    5. 生成缩略图
    6.如果该文件已经上传成功 判断之前的头像是其他图片还是 default.jpg 如果是其它图片 则将其删除
    7.将上传成功后的图片在模板中显示
    :return:
    """
    form = UploadForm()
    if form.validate_on_submit():
        #获取文件后缀
        shuffix = os.path.splitext(form.icon.data.filename)[-1]
        #生成随机的图片名称
        newName = random_picname(shuffix)
        #自己将判断该名称是否存在的while循环添加上
        file.save(form.icon.data,name=newName)
        #生成缩略图
        filePath = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],newName)
        f = Image.open(filePath)
        print(f.size) #获取图片的大小
        f.thumbnail((300,300))
        f.save(filePath)
        #判断 之前的图片是否为default.jpg 不是的话则删除
        if current_user.icon != 'default.jpg':
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon))
        current_user.icon = newName
        db.session.add(current_user)
        flash('头像修改成功')
    img_url = file.url(current_user.icon)
    # print(current_user.icon)
    return render_template('user/change_icon.html',form=form,img_url=img_url)
```



## 二、发表帖子

### (1) 帖子模型

一对多的关系

一的一方 使用 relationship 关联到多的一方    

多的一方使用ForeignKey关联到一的一方

**参数说明**

```python
一的一方
#参数1 为模型名称
#backref 反向引用的字段名  Post.query.get(1).user
#lazy 加载世家  dynamic 懒加载在使用的时候 返回的是查询的对象
posts = db.relationship('Posts',backref='user',lazy='dynamic')
多的一方
#创建外键  关联的 user表的id
uid = db.Column(db.Integer,db.ForeignKey('user.id'))
```

**使用方法**

```python
p = Posts.query.get(1)
print(p.user.username)
u = User.query.get(1)
for i in u.posts:
    print(i.content)
```

### 将图片缩放1份显示的  还有一份是前台显示帖子的时候显示的



### (2) 分页对象

```python
paginate: 分页类  返回pagination对象
    参数：
    page:  指定当前的页码
    per_page:每页显示数据的条数 默认20条
    error_out:当分页查询 出循错误 抛出错误 默认为True
        
pagination对象的属性
	属性：
    items:当前页的所有数据
    page:当前的页码
    pages:总页码数
    total:总记录数 
    per_page:每页多少条
    prev_num:上一页的页码
    next_num:下一页的页码
    has_prev:是否有上一页
    has_next:是否有下一页
    方法：
    prev: 上一页的分页对象
	next:下一页的分页对象
    iter_pages:页码迭代器(1,2,3,4,...都在此迭代器中) 
    显示当前的页码数  如果显示不下 则显示...
```



晚上完成 

1. 帖子的详情页
2. 贴字的评论的回复    
3. 点击查询我发表过的帖子



















