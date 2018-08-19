## Numpy

### 创建ndarray

#### 1.使用np.array()由python list创建

```
dtype=（float，int，str）  可以指定
```

```python
l = [3,1,4,5,9,6]
n = np.array(l)    # array里面需要传列表    则创建成功
n
np.array([[3,4,7,1],[3,0,1,8],[2,4,6,8]])
```

#### 2. 使用np的routines函数创建

```python
包含以下常见创建方法：
# 创建全为1的数组  
(1) np.ones(shape, dtype=None, order='C')
如：
np.ones((40,80,3),dtype=int)    # ones  创建出来的值都是1

# 创建全为0的数组
(2) np.zeros(shape, dtype=float, order='C')
np.zeros((100,200,5))   # 创建出来的值都是0

# 创建指定值的数组
(3) np.full(shape, fill_value, dtype=None, order='C')
np.full((20,30),fill_value=8.88)    #  指定创建的数组里面的值

# 创建满秩矩阵
4) np.eye(N, M=None, k=0, dtype=float)
对角线为1其他的位置为0
np.eye(5)

# 创建线性矩阵
(5) np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# retstep=True 输出步数多少   # endpoint=False  最后一个150要不要显示 
np.linspace(start = 0,stop = 150,num = 50,endpoint=False,retstep=True,dtype=np.int8)   
# 将数据均匀的划分

# 创建均等步长矩阵
(6) np.arange([start, ]stop, [step, ]dtype=None)
np.arange(0,100,step = 3)    # arange   让数据从0开始  到100停止 step步数等于3   并且取不到100

# 以下的方法可以创建多维的随机数组
(7) np.random.randint(low, high=None, size=None, dtype='l')
#  从-100  到100之间随机生成数   并且是2维  4行5列的数组
np.random.randint(-100,100,size = (4,5))

# 创建标准正太分布
(8) np.random.randn(size)
#  标准正太分布，就是大部分围绕在1的值   10行10列
np.random.randn(10,10)

# 也是生成正太分布的数组
(9)np.random.normal(loc=0.0, scale=1.0, size=None)
# 也是生成正太分布，可以指定loc的值，在这个附近浮动，  scale是浮动的大小，1是最接近  size尺寸
np.random.normal(175,1,56)

# 生成0-1的随机数，左闭右开
(10) np.random.random(size=None)
np.random.random(size = 10)

```

### ndarray的属性

4个必记参数： 

ndim：维度

 shape：形状（各维度的长度） 

size：总长度

dtype：元素类型

### ndarray的基本操作

#### 1.索引

n = np.random.randint(0,100,size = 10)

n[3]

#### 2.切片

n[3:6]  	#  array([64, 73, 88])

n[3:6:2]  # 取第3到6的值，步长为2

将数据反转

n[::-1]

#### 3.变形

使用reshape函数，注意参数是一个tuple！

n = np.random.randint(0,255,size = 998640)

让数组变形，但是值相乘要等于 size  # 如果是负数，则直接转化成一维的数组

把上面1维的数组变成3维的数组

image2 = n.reshape((456,730,4))   

#### 4.级联

1. np.concatenate() 级联需要注意的点：
2. 级联的参数是列表：一定要加中括号或小括号
3. 维度必须相同
4. 形状相符
5. 【重点】级联的方向默认是shape这个tuple的第一个值所代表的维度方向
6. 可通过axis参数改变级联的方向

```python
 # axis  默认是0   以行的方式进行级联    参数1 是以列进行级联
np.concatenate((n1,n2),axis = 0)  
np.concatenate((n1,n2),axis = 1)

np.hstack与np.vstack
# 水平级联与垂直级联,处理自己，进行维度的变更
n4 = np.hstack(np.hstack(cat))  # 一维的猫了
n5 = np.vstack(np.vstack(n4))  # 二维的猫，每个元素都只有一个
```

#### 5.切分

```python
# 与级联类似，三个函数完成切分工作：
np.split
np.vsplit
np.hsplit

# 以行方向对第1,2个元素进行拆分,生成了3个新的数组   # 默认是以vsplit形式拆分   有axis的参数，同上
np.split(n,(1,2))  
np.vsplit(n,(1,2))   # 结果同上
np.hsplit(n,(2,4))     # 以列方向对第2,4个元素进行拆分，生成了3个新的数组
```

#### 6.副本

所有赋值运算不会为ndarray的任何元素创建副本。对赋值后的对象的操作也对原来的对象生效。

可使用copy()函数创建副本

n2 = n.copy()



### ndarray的聚合操作

```python
	Function Name	NaN-safe Version	Description
    # 求和
    np.sum	np.nansum	Compute sum of elements
    # 返回给定轴上的数组元素的乘积。
    np.prod	np.nanprod	Compute product of elements
    #  平均值	
    np.mean np.nanmean	Compute mean of elements
    # 标准差 	
    np.std  np.nanstd	Compute standard deviation   数据的离散程度
    # 方差
    np.var	np.nanvar	Compute variance
    # 最小值
    np.min	np.nanmin	Find minimum value
    # 最大值
    np.max	np.nanmax	Find maximum value
    # 最小值索引
    np.argmin	np.nanargmin	Find index of minimum value
    # 最大值索引
    np.argmax	np.nanargmax	Find index of maximum value
    # 中位数
    np.median	np.nanmedian	Compute median of elements
    np.percentile	np.nanpercentile	Compute rank-based statistics of elements
    np.any	N/A	Evaluate whether any elements are true
    np.all	N/A	Evaluate whether all elements are true
    # 幂运算
    np.power 
```

### nadrray的矩阵操作

#### 1.加减乘除

如ddd+10

会对ddd矩阵数值全部都加10

#### 2.矩阵之间的操作

```python
# 两个矩阵相加
n2 = np.random.randint(0,10,size=(4,5))
# 元素对应相加
n2 + n2

# 当矩阵不对应时,不可以相加
n3 = np.random.randint(0,10,size=(4,3))
# 报错
n2 + n3
```

#### 3.矩阵积np.dot()

```python
n1 = np.random.randint(0,10,size=(2,3))  
# array([[5, 0, 6],
#       [4, 6, 3]])
n2 = np.random.randint(0,10,size=(3,4))
# array([[6, 1, 9, 5],
#       [4, 2, 4, 8],
#       [3, 5, 4, 7]])
np.dot(n1,n2)
# 结果是  行：为n1的行  列:n2 的列
# 48=5*6+0*4+6*4
# 35=5*1+0*2+6*5
# 31=4*1+6*2+3*5
array([[48, 35, 69, 67],
       [57, 31, 72, 89]])

```

#### 广播机制

```python
【重要】ndarray广播机制的两条规则
规则一：为缺失的维度补1
规则二：假定缺失元素用已有值填充
m = np.ones((2,3),dtype=int)
# array([[1, 1, 1],
#       [1, 1, 1]])
n = np.arange(3)
# array([0, 1, 2])
m + n 
array([[1, 2, 3],
       [1, 2, 3]])
```

### ndarray的排序

#### 1.快速排序

```python
np.sort()与ndarray.sort()都可以，但有区别：

np.sort()不改变输入
ndarray.sort()本地处理，不占用空间，但改变输入
np.sort(n)  # 不改变n的值
n.sort()	# 改变n的值
```

#### 2.部分排序

```python
np.partition(a,k)
有的时候我们不是对全部数据感兴趣，我们可能只对最小或最大的一部分感兴趣。
当k为正时，我们想要得到最小的k个数
当k为负时，我们想要得到最大的k个数
# 实例

n = np.random.randint(0,100,size=10)
n
array([48, 31, 80, 55, 86, 22, 54, 60, 54, 54])
np.partition(n,-3)
array([22, 48, 54, 54, 31, 54, 55, 60, 80, 86])
np.partition(n,3)
array([22, 31, 48, 54, 54, 54, 55, 60, 80, 86])
```

## Pandas

Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的

### Series

Series是一种类似与一维数组的对象，由下面两个部分组成：

- values：一组数据（ndarray类型）
- index：相关的数据索引标签

导入:

from pandas import Series

#### 1.Seroes的创建

```python
两种创建方式：

(1) 由列表或numpy数组创建
    默认索引为0到N-1的整数型索引
    n = np.array([0,2,4,6,8])
    li = [1, 2, 3, 4, 5]
    #Series和ndarray差别，有没有具体的索引
    s1 = Series(n)						# array创建
    s2 = Series(li)						# 列表创建
    #Series包含ndarray
    #Series功能就会强大，索引，检索方便很多
    s.values
    # 拿到数据的索引
    s.index
    # 还可以通过设置index参数指定索引
    s.index = list('abcde')
    # 修改值
    s1[0] = 100     s1会改变值
    s2[0] = 100     s2 不会改变值
   
(2) 由字典创建
    # 字典创建
    s1 = Series({'语文':150,'数学':150,'英语':150,'理综':300})
    s1
    输出:
      语文    150
      数学    150
      英语    150
      理综    300
      dtype: int64
```

#### 2.Series的索引和切片

##### (1) 显式索引：

- 使用index中的元素作为索引值
- 使用.loc[]（推荐）
- 显示索引是双闭区间

```PYTHON
s1 = Series({'语文':150,'数学':150,'英语':150,'理综':300})
# 单个index元素索引取值
      s1['理综']
      输出:
          150
      # 多个索引，要加中括号
      s1[['语文','数学']]
      输出:
          150
          150
      # 语文到理综的索引全部都拿出来
      s1['语文':'理综']
      输出:
          语文    150
          数学    150
          英语    150
          理综    300

 # 使用loc来取值  
		# 单个索引取值
		s1.loc['语文']
		输出:
        	150
		# 多个索引值
		s1.loc[['语文','数学']]		
        输出:
            语文    150
            数学    150
            dtype: int64
```

##### (2) 隐式索引：

- 使用整数作为索引值

- 使用.iloc[]（推荐）

- 注意，此时是半开区间

  ```python
  # 默认会有一个隐式的索引下标
  s1 = Series({'语文':150,'数学':150,'英语':150,'理综':300})
  # 使用隐式索引下标取值
  		s1[0]
    		输出:
        		150
          s1[0:2]
          输出:
            语文    150
            数学    150
            dtype: int64		
           
  # 使用iloc来取值
  		s1.iloc[[1,2]]
    		输出:
        		数学    150
  			英语    150		
          #左闭右开
          s1.iloc[0:2]
          	语文    136
              数学     69
              dtype: int64

  ```



#### 3.Series的基本概念

##### (1)可以把Series看成一个定长的有序字典

可以通过shape，size，index,values等得到series的属性

```python
s1.shape   # Serier的形状
s1.size    # Serier的大小
s1.values  # Serier的所有值
s1.index   # Serier的所有索引

可以通过head(),tail()快速查看Series对象的样式
s1.head(3)	# 查看头部前面3条的值和索引
s1.head(3)	# 查看尾部3条的值和索引
```

##### (2)当索引没有对应的值时，可能出现缺失数据显示NaN（not a number）的情况

```python
s = Series(data = ['张三','Sara',None])
s
输出:
	0      张三
	1    Sara
	2    None
	dtype: object
      
	# # 判断值是否为空
	pd.isnull(s)
    输出:
      0    False
      1    False
      2     True
    #判断是否有值
	pd.notnull(s)
    输出:
      0     True
      1     True
      2    False
    # 简写:
	s.notnull
    s.isnull
    
    #过滤掉空值(2种方式)
	s[pd.notnull(s)]
    s[s.notnull()]
```

##### 3.Series对象本身及其实例都有一个name属性

```python
#标识Series数据是什么意思
s.name = '姓名'
s
输出:
  0      张三
  1    Sara
  2     NaN
  Name: 姓名, dtype: object
```

#### 4.Series的运算

##### (1) 适用于numpy的数组运算也适用于Series

​			如  加减乘除

##### (2) Series之间的运算

- 在运算中自动对齐不同索引的数据

- 如果索引不对应，则补NaN

  ```python
  s1 = Series(data = np.random.randint(0,100,size = 5))
  s2 = Series(np.random.randint(0,10,size=10))

  # #当两个Series进行相加时，如果索引不对应，那么就会填补Nan
  # + 算数运算符
  s1 + s2
  输出:
  0    27.0
  1    78.0
  2    16.0
  3     5.0
  4    83.0
  5     NaN
  6     NaN
  7     NaN
  8     NaN
  9     NaN
  dtype: float64
  ```

  - 注意：要想保留所有的index，则需要使用.add()函数

  - 函数有 fill_value的参数  如果seriers不对应,有空值,则默认用fill_value的值来运算

  - | Python Operator | Pandas Method(s) |
    | --------------- | ---------------- |
    | +               | add()            |
    | -               | sub()            |
    | *               | mul()            |
    | /               | div()            |
    | //              | floordiv()       |
    | %               | mod()            |
    | **              | pow()            |

```python
s1 = Series({'语文':150,'数学':150,'英语':150,'理综':300})
s1
输出:
      语文    150
      数学    150
      英语    150
      理综    300
      dtype: int64
s2 = Series({'文综':250})
s2
输出:
      文综    250
      dtype: int64

s1.add(s2,fill_value=1)
输出:
      数学    150.0
      文综    250.0
      理综    301.0
      英语    150.0
      语文    150.0
      dtype: float64
```





### DataFrame

DataFrame 
类似于Excel，DataFrame组织数据，处理数据

- 行索引：index
- 列索引：columns
- 值：values（numpy的二维数组）

#### 1.DataFrame的创建

##### (1)字典创建

```python
dic = {'name':['张三','石六','Sara'],'age':[22,33,18],'sex':['male','female','male']}
df = DataFrame(dic,columns=['name','age','sex','salary']
# 字典的key和columns就是对应列的值   如果传入的列与字典的键不匹配，则相应的值为NaN
```

![微信截图_20180612174935](C:\Users\sdsd\Desktop\笔记\img\微信截图_20180612174935.png)

```python
#行：代表样本，列：样本的属性
df2 = DataFrame(data = np.random.randint(0,150,(5,4)),
                columns=['语文','数学','Python','物理'],
               index = list('ABCDE'))
df2
```

![微信截图_20180612175656](C:\Users\sdsd\Desktop\笔记\img\微信截图_20180612175656.png)

#### 2.DataFrame属性：

values			dataframe的值  如:

```
array([[142,  22, 133,  41],       
[ 40,  91,  63,  45],      
 [149,  27, 144,  23],       
[135,  76,  95, 134],       
[115,  91,  43,  29]])
```

columns			dataframe的列索引  如:

```
Index(['name', 'age', 'sex'], dtype='object')
```

index			dataframe的行索引 如:(5, 4)

```
RangeIndex(start=0, stop=3, step=1)
```

shape			dataframe的形状  如:(5, 4)

```
(5, 4)
```

#### 3.DataFrame的索引

##### (1) 对列进行索引

- 通过类似字典的方式
- 通过属性的方式

每一个DataFrame的列,都是一个Seriers.

返回的Series拥有原DataFrame相同的索引，

并且name的值是列名

```python
# 属性的调用形式：df2.xxx
df.张三
输出:
  语文    150
  数学    150
  英语    150
  理综    300
	Name: 张三, dtype: int64
返回的是Seriers   ,可以继续操作

# 通过类似字典的方式

```

##### (2) 对行进行索引

- 使用.loc[]加index来进行行索引
- 使用.iloc[]加整数来进行行索引

 同样返回一个Series，index为原来的columns。

```python
df.loc['语文'].loc['张三']  # 先行,再列
df.loc['语文']
# 英语   先第2行,第0个元素
df.iloc[2,0]
#0：检索行--->series,1 就相当于检索列
df2.iloc[0,1]
```

##### (3) 对元素索引的方法

- 使用列索引

- 使用行索引(iloc[3,1]相当于两个参数;iloc[[3,3]] 里面的[3,3]看做一个参数)

- 使用values属性（二维numpy数组）

  ```python
  df2.iloc[[3,3]]
  ```

#### 4.DataFrame的运算

##### （1） DataFrame之间的运算

同Series一样：

- 在运算中自动对齐不同索引的数据
- 如果索引不对应，则补NaN

##### （2） Series与DataFrame之间的运算

【重要】

- 使用Python操作符：以行为单位操作（参数必须是行），对所有行都有效。（类似于numpy中二维数组与一维数组的运算，但可能出现NaN）

- 使用pandas操作函数：

  ```
    axis=0：以列为单位操作（参数必须是列），对所有列都有效。
    axis=1：以行为单位操作（参数必须是行），对所有行都有效。
  ```

```python
# python操作符操作
	# DataFrame
    df1
    # Seriers
    s = df1.loc['lucy']  # 以行取出来的的Seriers
    s1 = df1.张三			# 以列取出来的操作
    # 相加

# pandas操作函数操作
	df1.add(s,axis=1)   # 以行来操作	 ,只能与列的seriers相运算
  	df1.add(s1,axis=0)	# 以列来操作  ,只能与列的seriers相运算

```

### 处理丢失数据

#### 1.None和nan

None是Python自带的，其类型为python object。因此，None不能参与到任何计算中。

```python
n1 = np.array([1,2,None])
n2 = np.array([1,2,np.nan])

#  'int' and 'NoneType'   None是python的类型  不能进行运算
# n1.sum()
#nan not a number可以进行计算
n2.sum()

!!!DataFreme中  如果赋予了None值,会自动转换成Nan
```

#### 2.pandas中None与np.nan的操作

- `isnull()`	判断函数
- `notnull()`     判断函数
- `dropna()`: 过滤丢失数据
- `fillna()`: 填充丢失数据

```python
判断函数:
    # 是否是Nan值
    df.isnull()

    !!!特别注意,此处的axis和正常的axis相反!!!
    # 只要列中有一个nan的值  整列都返回true
    df.isnull().any()   # 默认有参数axis = 0  是列
    # 按行来判断如果有一个nan的值  整行都返回true
    df.isnull().any(axis=1)   

    # 只有一列全是nan的值  返回true
    df.isnull().all()

    #notnull(),all(axis = 1) 配合索引，就可以获取不为空的数据
    # 意味着把行中有nan的行过滤掉
    df[df.notnull().all(axis = 1)]

过滤函数:
  dropna()
	可以选择过滤的是行还是列（默认为行）
    # 把当前一列有nan的数据全部过滤掉
	df.dropna(axis = 1)
    # 把当前选择全部都是nan的行/列 中删除掉
    df.dropna(how = 'all',inplace=True)  # inplace 是否替换原DataFrame

填充函数:
  	# 以50来填充nan的值
	df.fillna(value=50)
    
    # ffill 是向选择向前填充  取前面的值填充  bfill是取后面的值填充  
	df.fillna(method='bfill')
    
    选择填充的轴axis
    - axis=0：index/行
	- axis=1：columns/列
    
    # 指定以列来为参照物   默认axis=0,取前面一行来填充   
	df.fillna(method='ffill',axis=1)
```

### 层次化索引

#### 1.创建多层次化索引

##### (1) 隐式构造

- Series也可以创建多层索引
- 实际上就是在构造时,index或者columns传入两个或者更多的数组

```python
# Series创建多层索引
index = [['一班','一班','一班','一班','一班','二班','二班','二班','二班','二班'],[1,2,3,4,5,1,2,3,4,5]]
s = Series(data=np.random.randint(0,150,size=10),index=index)
s

# DataFrame创建多层索引
data = np.random.randint(0,150,size=(10,6))
columns = [['期中','期中','期中','期末','期末','期末'],['语文','数学','英语','语文','数学','英语']]
df = DataFrame(data=data,columns=columns)
df

```

##### (2)显式构造

- 使用数组array

  ```python
  data = np.random.randint(0,150,size=(10,6))
  #  pd.MultiIndex.from_arrays里面也放一个数组
  columns = pd.MultiIndex.from_arrays([['期中','期中','期中','期末','期末','期末'],['语文','数学','英语','语文','数学','英语']])
  index = [['一班','一班','一班','一班','一班','二班','二班','二班','二班','二班'],[1,2,3,4,5,1,2,3,4,5]]
  df = DataFrame(data=data,columns=columns,index=index)
  df
  ```

- 使用tuple

  ```python
  data = np.random.randint(0,150,size=(10,6))
  #  pd.MultiIndex.from_arrays里面也放一个数组
  columns = pd.MultiIndex.from_arrays([['期中','期中','期中','期末','期末','期末'],['语文','数学','英语','语文','数学','英语']])
  # index = [['一班','一班','一班','一班','一班','二班','二班','二班','二班','二班'],[1,2,3,4,5,1,2,3,4,5]]
  # pd.MultiIndex.from_tuples里面放一个列表包含元组
  index = pd.MultiIndex.from_tuples([('一班',1),('一班',2),('一班',3),('一班',4),('一班',5),('二班',1),('二班',2),('二班',3),('二班',4),('二班',5)])
  df = DataFrame(data=data,columns=columns,index=index)
  df
  ```

- 使用product

  最简单，推荐使用

```python
data = np.random.randint(0,150,size=(10,6))
# pd.MultiIndex.from_product里面放2个列表
columns = pd.MultiIndex.from_product([['期中','期末'],['语文','数学','英语']])
index = pd.MultiIndex.from_product([['一班','二班'],np.arange(1,6)])
df = DataFrame(data=data,columns=columns,index=index)
df
```

#### 2. 多层索引对象的索引与切片操作

##### (1)对于Series来说,与中括号[]和.loc使用完全一样

①索引

```python
s['一班']

s.loc['一班']

s.loc['一班',2]

s.loc['一班'].loc[2]

s.loc['一班'][2]
```

② 切片

```python
s.loc['一班',2:4]

s.loc['一班'][2:4]
```

##### (2)DataFrame的操作

① 可以直接使用列名称来进行列索引

```python
# 列 切片
df['期中']

# 两层列选择
# 列  切片
df['期中','语文']

# 行
df.loc['一班'].loc[1:3]
```

##### 3.索引的堆（stack）

讲index或者columns对换位置

- stack()

- unstack()

  (小技巧)

  使用stack()的时候，level等于哪一个，哪一个就消失，出现在行里

  ​

  ```python
  # stack 改变列   0 ,1,2,3...为列的索引
  df.stack(level=0)
  ```

  ​

##### 4.聚合操作

- 需要指定axis
- 【小技巧】和unstack()相反，聚合的时候，axis等于哪一个，哪一个就保留

```python
# 把每一行的都加起来了
df.sum(axis=0)  

# 把二班的成绩和一班的成绩以行相加
df.sum(axis=0,level=1)   
```

### pandas的拼接操作

pandas的拼接分为两种：

- 级联：pd.concat, pd.append
- 合并：pd.merge, pd.join

#### 1. 使用pd.concat()级联

pandas使用pd.concat函数，与np.concatenate函数类似，只是多了一些参数：

```python
objs						# 传入的两个要级联的数组	
axis=0						# 指定以0(行)链接,还是1(列)链接  默认是行级联
join='outer'				# 交集,并集   默认outer,所有都会级联,   inner只级联共同有的
join_axes=None				# 指定以哪一边的列级联,另外一边抛弃,  如:[df3.columns]
ignore_index=False			# 不理会原索引,自己重新生成索引
keys = [value1,value2...]	# 为级联后新添加新的索引,  df1 为value1,  df2为value2

匹配级联:
  简单级联:
      # 默认行级联
      pd.concat((df1,df2),sort=True)
      # 修改级联方向
	  pd.concat((df1,df2),axis=1,sort=True)
      
  忽略之前的索引:
    # 忽略索引,重新分配索引
	pd.concat((df3,df4),ignore_index=True)
  
  或者使用多层索引 keys :
    # kesys 在这里可以使我们合并zhi
	pd.concat((x,y),keys=['X','Y'])	  # x,y新的行索引是  X,Y
    
    
不匹配级联:
  df1 = make_df([1,3],list('AB'))
  df2 = make_df([2,4],list('BC'))
  有3种连接方式：
	外连接：补NaN（默认模式）
    # 默认是外链接out   会将所有的属性进行合并
	pd.concat([df1,df2],sort=True)
    输出:
            A	B	C
        1	A1	B1	NaN
        3	A3	B3	NaN
        2	NaN	B2	C2
        4	NaN	B4	C4

    内连接：只连接匹配的项
    # 内连接   合并了共有的属性,交集
	pd.concat([df1,df2],join='inner')
    输出:
             B
        1	B1
        3	B3
        2	B2
        4	B4
      
    连接指定轴 join_axes
    # 以df3的轴为数据,例如下面,以某一个datafreme的列,索引为新的列索引值,不指定时,默认讲两个进行合并
	pd.concat((df3,df4),join_axes=[df3.columns])
    
```

#### 2.使用append()函数添加

把两个列表拼接,相加

```python
df1 = make_df([0,1,2,3,4],['大众','福克斯'])
df2 = make_df([5,6,7,8,9],['大众','福克斯'])
# 用于数据的添加,合并
# concat方法属于 pandas模块
# append方法属于DataFrame里面的方法
df1.append(df2)
输出:
  	大众	福克斯
0	大众0	福克斯0
1	大众1	福克斯1
2	大众2	福克斯2
3	大众3	福克斯3
4	大众4	福克斯4
5	大众5	福克斯5
6	大众6	福克斯6
7	大众7	福克斯7
8	大众8	福克斯8
9	大众9	福克斯9
```

#### 3. 使用pd.merge()合并

merge需要根据共有的行/列来合并

##### 一对一合并

```python
df1 = DataFrame({'emplyee':['po','Sara','Danis'],
                 'group':['sail','counting','marcketing']})
df2 = DataFrame({'emplyee':['po','Sara','Bush'],
                 'work_time':[2,3,1]})

# 一对一合并
# 两个参数 ,左dataf,右dataf
pd.merge(df1,df2)

输出:
  
        	emplyee	group	work_time
        0	po		sail		2
        1	Sara	counting	3


```

##### 多对一合并

```python
df1 = DataFrame({'emplyee':['po','Sara','Danis'],
                 'group':['sail','counting','marcketing']})
# 有两个po
df2 = DataFrame({'emplyee':['po','po','Bush'],
                 'work_time':[2,3,1]})

# 多对一的情况
pd.merge(df1,df2)

输出:
  	
        	emplyee	group	work_time
        0	po		sail		2
        1	po		sail		3
```

##### 多对多合并

```python
# 有两个po
df1 = DataFrame({'emplyee':['po','po','Danis'],
                 'group':['sail','counting','marcketing']})
# 有两个po
df2 = DataFrame({'emplyee':['po','po','Bush'],
                 'work_time':[2,3,1]})

# 在进行多对多合并时,每一个数据都没有放过
pd.merge(df1,df2)

输出:
                emplyee		group	work_time
            0		po		sail		2
            1		po		sail		3
            2		po		counting	2
            3		po	c	ounting		3
```

##### key的规范化

- 使用on=显式指定哪一列为key,当有多个key相同时使用

```python
df3 = DataFrame({'employee':['Po','Summer','Flower'],
                 'group':['sail','marketing','serch'],
                 'salary':[12000,10000,8000]})
df4 = DataFrame({'employee':['Po','Winter','Flower'],
                 'group':['marketing','marketing','serch'],
                 'work_time':[2,1,5]})

# 指定以某一列进行合并
pd.merge(df3,df4,on='employee')

输出:
  	employee	group_x	salary	group_y	work_time
0		Po		sail	12000	marketing	2
1		Flower	serch	8000	serch		5
```

​	

- 如果两个表,名字不一样进行合并时,用left_on和right_on合并

```python
# 如果写错字了,属性不同部门写的不一样(employer,Team)
df3 = DataFrame({'employer':['Po','Summer','Flower'],
                 'Team':['sail','marketing','serch'],
                 'salary':[12000,10000,8000]})
df4 = DataFrame({'employee':['Po','Winter','Flower'],
                 'group':['marketing','marketing','serch'],
                 'work_time':[2,1,5]})

# 当一个表和另外一个表不一样的时候,可以使用这个
pd.merge(df3,df4,left_on='employer',right_on='employee')

输出:
  	employer	Team	salary	employee	group	work_time
0	Po			sail	12000	Po			marketing	2
1	Flower		serch	8000	Flower		serch		5


实例2:
 # 先写的df3参数1,为左..df4参数2  为右
pd.merge(df3,df4,left_on='Team',right_on='group')
```

##### 内合并与外合并

```python
df1 = DataFrame({'age':[18,22,33],'height':[175,169,180]})
df2 = DataFrame({'age':[18,23,31],'weight':[65,70,80]})

# 内合并,默认的
pd.merge(df1,df2)

输出:
	age	height	weight
0	18	175	65

# 外合并就是并集,所有的数据都会合并
pd.merge(df1,df2,how='outer')

输出:
  	age	height	weight
0	18	175.0	65.0
1	22	169.0	NaN
2	33	180.0	NaN
3	23	NaN	70.0
4	31	NaN	80.0

拓展:
  左合并、右合并：how='left'，how='right'

```

##### 列冲突的解决

当列有冲突,重名的时候时

用suffixes=自己指定后缀

```python
df3 = DataFrame({'employee':['Po','Summer','Flower'],
                 'group':['sail','marketing','serch'],
                 'salary':[12000,10000,8000]})
df4 = DataFrame({'employee':['Po','Winter','Flower'],
                 'group':['marketing','marketing','serch'],
                 'work_time':[2,1,5]})

# 指定以某一列进行合并,suffixes是更名
pd.merge(df3,df4,on='group',suffixes=['_期中','_期末'])


输出:
  	employee_期中	group	salary	employee_期末	work_time
0	Summer		marketing	10000	Po			2
1	Summer		marketing	10000	Winter		1
2	Flower		serch		8000	Flower		5
```

### pandas数据处理

#### 1.删除重复元素

```python
# duplicated()检测重复的行,返回bool值  
df.duplicated()

# bool值取反
np.logical_not(df.duplicated())

# 使用drop_duplicates()函数删除重复的行
df.drop_duplicates()

```

#### 2.映射

包含三种操作：

- replace()函数：替换元素
- !!!最重要!!!   map()函数：新建一列
- rename()函数：替换索引

原Datafrema:

![微信截图_20180614174925](C:\Users\sdsd\Desktop\笔记\img\微信截图_20180614174925.png)

##### replace()函数：替换元素

```python
# 定义需要映射的字典
dic = {'red':10,'green':20,'cyan':40}
# 将映射字典放入函数即可
df.replace(dic)

输出:
  新增了一列
  
        	color	weight
        0	10		10
        1	20		20
        2	yellow	30
        3	40		40
        4	10		10
        5	20		20
        
#  replace还经常用来替换NaN元素
# 将df里面的nan值变成0.1
df.replace({np.nan:0.1})
```

##### !!!map()函数：新建一列!!!

```python
# 字典生成新列
	dic = {'red':9,'green':8,'cyan':6}
  	# 新建一列   ,但是不知道怎么去对应值  ,所以定义一个字典,作为一个映射
	df['price'] = df['color'].map(dic)
    输出:
      		# 生成了新的一列price
           		 color	weight	price	
            0	red		10.0	9.0	
            1	green	20.0	8.0	
            2	NaN		NaN		NaN	
            3	cyan	40.0	6.0	
            4	red		10.0	9.0	
            5	green	20.0	8.0	
# map()函数中可以使用lambda函数生成新列
    # 传入一个x   返回一个两倍
    # 意味着可以传一个函数
    df['price2'] = df['price'].map(lambda x: x*2)
    
    输出:
      	生成了新的一列price2
        	color	weight	price	price2
        0	red		10.0	9.0		18.0
        1	green	20.0	8.0		16.0
        2	NaN		NaN		NaN		NaN
        3	cyan	40.0	6.0		12.0
        4	red		10.0	9.0		18.0
        5	green	20.0	8.0		16.0

        
# 传入函数生成新列
      def socre(x):
          if x > 9 :
              return '超贵'
          if x > 8 :
              return '好贵'
          else:
              return '一般'
      # map第三种使用方法,传函数
      df['评价'] = df['price'].map(socre)
      df
      
      输出:
       
          	color	weight	price	price2	评价
          0	red		10.0	9.0		18.0	好贵
          1	green	20.0	8.0		16.0	一般
          2	NaN		NaN		NaN		NaN		一般
          3	cyan	40.0	6.0		12.0	一般
          4	red		10.0	9.0		18.0	好贵
          5	green	20.0	8.0		16.0	一般		

# map函数修改列的值
      # 修改值
  	  dic = {18:28,16:30,12:60}
      df['price2'] = df['price2'].map(dic)
      df
      
      输出:
        	此时price2的值修改成了dic上面的值
          	color	weight	price	price2	评价	评价2
          0	red		10.0	9.0		28.0	好贵	好贵
          1	green	20.0	8.0		30.0	一般	一般
          2	NaN		NaN		NaN		NaN		一般	一般
          3	cyan	40.0	6.0		60.0	一般	一般
          4	red		10.0	9.0		28.0	好贵	好贵
          5	green	20.0	8.0		30.0	一般	一般
          
拓展:
  transform()和map()类似
  # 一样可以通过映射添加新的列
  df['评价2'] = df['price'].transform(socre)
  df
```

##### rename()函数：替换索引

```python
# 传字典修改索引
dic = {'weight':'一餐吃..kg','price2':'一斤/rmb'}
# 使用rename()函数替换行索引
df.rename(columns=dic)
```

#### 3.异常值检测和过滤

使用describe()函数查看每一列的描述性统计量

![微信截图_20180614185809](C:\Users\sdsd\Desktop\笔记\img\微信截图_20180614185809.png)

过滤实例:

![微信截图_20180614190109](C:\Users\sdsd\Desktop\笔记\img\微信截图_20180614190109.png)

![微信截图_20180614190119](C:\Users\sdsd\Desktop\笔记\img\微信截图_20180614190119.png)

#### 4.排序

使用.take()函数排序

可以借助np.random.permutation()函数随机排序

随机抽取数据分析时,使用这个方式

```python
np.random.permutation(np.arange(4))
输出:
  # 随机输出
  array([1, 2, 0, 3])
  
# take放的是隐式索引,随机抽样
df.take(np.random.permutation(np.arange(4)))
```

#### 5.数据聚合【重点】

```python
# 指定以颜色列来分组,返回的一个分组对象,当成dataFrema来使用就可以
group_co = df.groupby('color')
group_co

# 可以查看分组情况
group_co.groups  

# 分组后的平均值
group_co.mean()

# 分组后的求和
group_co.sum()
```

#### 6.高级数据聚合

在transform或者apply中传入需要调用的聚合函数即可

```python
# 原函数实现sum功能
df_sum = df.groupby('color').sum()

# 可以用transform和apply实现同样的功能
df.groupby('color').transform(sum)

# apply会求和,但是字符串也是一样会做运算
df.groupby('color').apply(sum)

# 去掉color,切片
df.groupby('color').apply(sum)[['price','weight']]
```

#### 7.数据类型转换

```python
# 数据类型转换
apple['Date'] = pd.to_datetime(apple['Date'])
```





### Pandas绘图函数

Series和DataFrame都有一个用于生成各类图表的plot方法

##### 1.线形图

###### 简单的Series展示:

```python
nd = np.linspace(0,100,num=50)
s = Series(nd)
# Series间接使用到了matplotlib
s.cumsum().plot()
```

![P线形图1](C:\Users\sdsd\Desktop\笔记\img\P线形图1.png)

###### 简单的DataFrame图表示例

```python
# 创建DataFrame
df = DataFrame(np.random.randint(0,30,size=(10,4)),index=list('abcdefjhil'),
               columns=list('ABCD'))

# 可指定表头,只支持英文
df.plot(title='DataFrame')
```

图:

![P线形图2](C:\Users\sdsd\Desktop\笔记\img\P线形图2.png)

##### 2.柱状图

柱状图示例,kind = 'bar'/'barh'

```python
# 竖直的柱状图bar
df.plot(kind = 'bar')
```

图:

![p柱状图1](C:\Users\sdsd\Desktop\笔记\img\p柱状图1.png)

```python
# 水平的柱状图
df.plot(kind='barh')
```

图:

![p柱状图2](C:\Users\sdsd\Desktop\笔记\img\p柱状图2.png)

##### 3.直方图

rondom生成随机数百分比直方图，调用hist方法

- 柱高表示数据的频数，柱宽表示各组数据的组距
- 参数bins可以设置直方图方柱的个数上限，越大柱宽越小，数据分组越细致
- 设置normed参数为True，可以把频数转换为概率

```python
# 创建Series
s = Series(np.random.randint(0,5,size=10))

# 看频数,出现的次数
# 横坐标  数值
# 纵坐标次数
s.hist()
```

图:

![p直方图](C:\Users\sdsd\Desktop\笔记\img\p直方图.png)

```python
#  小数
# 反应密度
s = Series(np.random.random(100))

# bin  可以设置数据之间的间隔
s.hist(bins=100)
```

图:

![p直方图2](C:\Users\sdsd\Desktop\笔记\img\p直方图2.png)

kde图

```python
# 也是看密度分布的图,有两种方式,这是另外一种,一般会同时与上一种一起出现
comp1 = np.random.normal(0,1,size=200)
comp2 = np.random.normal(1,2,size=200)

values = Series(np.concatenate((comp1,comp2)))

# 直方图
values.hist(bins=100,density=True,color='y')
# ked图
values.plot(kind='kde',style='--',color='b')
```

图:

![pkde图](C:\Users\sdsd\Desktop\笔记\img\pkde图.png)



##### 4.散布图

用来观察数据之间的关系

```python
nd = np.random.randint(0,50,size=(50,5))
df = DataFrame(nd,columns=list('XYWZP'))
# 传列索引的名称
df.plot('X','Y',kind='scatter')
```

图:

![p散布图](C:\Users\sdsd\Desktop\笔记\img\p散布图.png)

当要看多个点之间的关系时:

使用函数：pd.plotting.scatter_matrix(),

- 参数diagnol：设置对角线的图像类型

```python
pd.plotting.scatter_matrix(df,diagonal='kde',color='r')
```

图:

![p散步2](C:\Users\sdsd\Desktop\笔记\img\p散步2.png)

### Pandas读取文件

```python
# 正常文件读取   sep,指定以哪个符号作为分割符  ,header=None  不使用文件的头,
	pd.read_csv('filename',sep='\t',header=None)

# 读取sqlite
    # 导包
    import sqlite3 as sqlite3
    # 要先创建连接
    con = sqlite3.connect('filename')  # 但是必须是sqlite文件
    # 选择查询语句
    sql = 'select * from weather '
    pd.read_sql(sql,con)
    
    # 设置行索引   index_col 以temp作为行索引
    pd.read_sql(sql,con,index_col = 'temp')
    
# 写入sqlite文件
con = sqlite3.connect('filename')  # filename自己明明
# 可写可不写,如果weather表存在,就删除再执行下面的
con.execute('drop table if exists weather ')

# 将weather 数据存入con数据库中的table表
weather.to_sql('table名',con)
```

读取网络数据

```python
# 此url需要是一个文件
url = '......'

pd.read_url(url)
```

数据的透视表和交叉表

数据汇总工具

更加迅速来看表结构

```python
# 数据汇总工具

import pandas as pd
from pandas import Series,DataFrame
import numpy as np

df = DataFrame({'sex':['male','female','male','female'],
                'smoke':['Yes','No','No','No'],
               'height':np.random.randint(158,180,4),
               'weight':np.random.randint(50,80,4)})
```

![微信截图_20180625185610](C:\Users\sdsd\Desktop\笔记\img\微信截图_20180625185610.png)



```python
# 行分组
# 类似分组,值默认都取的平均值   aggfunc指定选哪个作为值,但是不认识字符串
df.pivot_table(index='sex',aggfunc=max)



# 列分组表  以smoke作为列进行分组
df.pivot_table(columns = 'smoke')
```

![行分组](C:\Users\sdsd\Desktop\笔记\img\行分组.png)

![行分组](C:\Users\sdsd\Desktop\笔记\img\列分组.png)

```python
# 交叉表
#交叉表
# 创建Datafrema
df1 = DataFrame({'sex':['male','female','male','male','female','male','female','male','male','female','male','female','male','male','female'],
                'hand':['right','right','left','right','right','left','right','right','left','right','right','left','right','right','left']}) 

# 快速将数据作为展示.以性别,和hand作为展示
# margins 边界的意思  进行了总共的统计
pd.crosstab(df1['sex'],df1['hand'],margins=True)

```

![交叉表](C:\Users\sdsd\Desktop\笔记\img\交叉表.png)



## Scipy

### 实例Scipy感受

1.登月照片傅里叶消噪:

```python
# 导包
import scipy as sp
import scipy.fftpack as fftpack

# 读取文件
moon = plt.imread('./data/moonlanding.png')

# 傅里叶转化,fft2可以处理多维的数组
moon_fft = fftpack.fft2(moon)

# 对转换之后的数据进行噪点消除
# 参数1    替换成0的值  从哪里替换
moon_fft_r = np.where(np.abs(moon_fft) > 8e2,0,moon_fft)

# 逆运算
moon_ifft = fftpack.ifft2(moon_fft_r)

# 去虚数保实数
moon_real = np.real(moon_ifft)

# 完成
plt.figure(figsize=(12,9))
plt.imshow(moon_real,cmap='gray')
```

### 数值积分，求解圆周率

```python
# 导包
# 求面积 ,使用积分
import scipy.integrate as integrate

f = lambda x: (1 - x**2) ** 0.5
# integrate.quad 是一个函数  ,参数为  函数,x,y
pi,dviation = integrate.quad(f,-1,1)
# pi返回π的值
# dviation返回的是积分的值
```

### Scipy文件输入/输出

文件格式是.mat，标准的二进制文件

```python
读普通mat文件:
    # 导包
    import scipy.io as spio

    nd = np.random.randint(0,150,size=10)
    # 参数一:文件名,可给后缀可不给  
    # 参数二:我们的数据,以字典的形式进行存储
    spio.savemat('nd',{'data':nd})
	# 使用io.loadmat来读取数据
    # 读取数据,拿出来是字典,对应key值拿到值
    spio.loadmat('nd')['data']

读写图片文件:
  	# 导包
    # 升级后直接用imageio的包了,不需要通过scipy来用
    import imageio
    cat  = imageio.imread('./data/cat.jpg')
	
    # rotate(旋转)、resize(设置大小)、imfilter(图片过滤)
	import skimage.transform as st
	# 图片旋转
    cat_rotate = st.rotate(cat,angle=-90)
	plt.imshow(cat_rotate)	
    
    # 设置大小  mode='reflect'  让他不警告   (250,350)设置图片大小
	cat_resize = st.resize(cat,(250,350),mode='reflect')
    plt.imshow(cat_resize)
    
    # 图片过滤
    from PIL import Image, ImageFilter
    cat_pil = Image.open('./data/cat.jpg')
    
    # 过滤  ImageFilter.EDGE_ENHANCE  过滤方式
    cat_pil.filter(ImageFilter.EDGE_ENHANCE)
    
    
```

###  图片处理

scipy.misc.face(gray=True)获取图片，使用ndimage移动坐标、旋转图片、切割图片、缩放图片

```python
# 提供了一个默认图片
face = misc.face(gray=True)
# 正常图片显示
plt.imshow(face,cmap='gray')

# 导包，读取图片显示图片
from scipy import  ndimage

shift移动坐标:
  	# 向下移动300
	# mode是移动方式
    # {'reflect'反射,和镜像一样, 'constant', 
    # 'nearest'附近的色素, 'mirror'镜像, 'wrap将移走的部分放上去'}
    face_shift = ndimage.shift(face,(-300,0,0),mode='wrap')
	plt.imshow(face_shift,cmap='gray')
    
rotate旋转图片:
  	# 旋转  axes轴
	face_rotate = ndimage.rotate(face,angle=90,axes=(-1,-2))
	plt.imshow(face_rotate,cmap='gray')
    
zoom缩放图片:
  	# 拉伸  缩放
    face_zoom = ndimage.zoom(face,zoom=0.3)
    plt.imshow(face_zoom,cmap='gray')
    
切割图片:
  	face_mini = face[300:500,600:900]
	plt.imshow(face_mini,cmap='gray')
    
```

### 图片进行过滤

添加噪声方便后续处理:

```python
# 拷贝face并改变数据类型
face_noisy = face.copy().astype(float)

# 加噪点
face_noisy += face.std()*0.3*np.random.standard_normal((768,1024))

# 完成添加噪声的图片
plt.imshow(face_noisy,cmap='gray')
```

#### 1.高斯滤波

```python
# 高斯滤波sigma：高斯核的标准偏差
# 将噪点高斯滤波后更清晰了
face_gaussian = ndimage.gaussian_filter(face_noisy,sigma=0.9)

# 展示图片
plt.imshow(face_gaussian,cmap='gray')
```

#### 2.中值滤波

```python
# 中值滤波参数size：给出在每个元素上从输入数组中取出的形状位置，定义过滤器功能的输入

# 中值滤波,不能为小数
face_median = ndimage.median_filter(face_noisy,size=2)
# 展示图片
plt.imshow(face_median,cmap='gray')
```

#### 3.signal中维纳滤波

```python
# signal维纳滤波mysize：滤镜尺寸的标量
导包:
  import scipy.signal as signal
  face_winner = signal.wiener(face_noisy,mysize=5)
  # 展示图片
  plt.imshow(face_winner,cmap='gray')
```



## Matplotlib

### 图片灰度处理

本质将第三列的颜色数组,变成一个数据

```python
# 三种方法

导包:
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  %matplotlib inline	
  
  # 读取文件
  j = plt.imread('./data/jizhengen.png')
  plt.imshow(j)
  
  # 使用平均值
  		# 对第三列,求平均值 这时候就变成2维数组了
		j_mean = j.mean(axis=2)
  		plt.imshow(j_mean,cmap='gray')
        
  # 使用最大值
        j_max = j.max(-1)
        plt.imshow(j_max,cmap='gray')

  # 加权平均值
        # color_list是固定值,绿红蓝权重比
  		color_list = [0.299,0.587,0.114]
      	# np.dot矩阵积乘完变成2维数组
        j_weight = np.dot(j,color_list)
        plt.imshow(j_weight,cmap='gray')
```

### Matplotlib基础知识

#### Matplotlib画图

Matplotlib中的基本图表包括的元素

- x轴和y轴
  水平和垂直的轴线


- x轴和y轴刻度
  刻度标示坐标轴的分隔，包括最小刻度和最大刻度


- x轴和y轴刻度标签
  表示特定坐标轴的值


- 绘图区域
  实际绘图的区域

##### 单一曲线图

```python
n = np.arange(10)
# 传入x  轴 y轴的值就可以了
plt.plot(n,n**2)
```



![m单一图1](C:\Users\sdsd\Desktop\笔记\img\m单一图1.png)

##### 包含多个曲线的图

1、可以使用多个plot函数（推荐）

```python
# 多个曲线一起画,要用多个plot
x = np.linspace(-np.pi,np.pi,1000)
y = x*3
plt.plot(x,y)
plt.plot(x,(1-x**2)**0.5)
plt.plot(x,np.cos(x))
```

图:

![m多个曲线1](C:\Users\sdsd\Desktop\笔记\img\m多个曲线1.png)

2、也可以在一个plot函数中传入多对X,Y值，在一个图中绘制多个曲线

```python
# 多个曲线一起画,效果同上
x = np.linspace(-np.pi,np.pi,1000)
y = x*3
plt.plot(x,y,x,(1-x**2)**0.5,x,np.cos(x))
```

图:

![m多个曲线2](C:\Users\sdsd\Desktop\笔记\img\m多个曲线2.png)

##### 网格线

```python
x = np.linspace(-10,10,1000)
y = np.cos(x)
plt.plot(x,y)
# 添加网格线  axis默认是both    X Y都有线
# 如果指定axis的值,则显示该轴的网格线
plt.grid(b=True,axis='y',color='red')
```

图:

![p网格线1](C:\Users\sdsd\Desktop\笔记\img\p网格线1.png)

设置grid参数（参数与plot函数相同）

- lw代表linewidth，线的粗细
- alpha表示线的明暗程度
- color代表颜色

```python
# 设置画布属性,用设置好的画布来画图
# 一次性画三个图
figure = plt.figure(figsize=(12,5))
# 设置占一行 3列当中的第一列
axes1 = figure.add_subplot(131)    
axes1.plot(x,y)
axes1.grid(True,color='gray',lw=2)

axes2 = figure.add_subplot(132)
axes2.plot(x,y)
axes2.grid(True,color='r',lw=1)

axes3 = figure.add_subplot(133)
axes3.plot(x,x**2)
axes3.grid(True,color='green',linestyle='--')
```

图:

![m网格图](C:\Users\sdsd\Desktop\笔记\img\m网格图.png)

#### Matplotlib坐标轴属性

##### 坐标轴界限

###### 通过axis来设置

```python
plt.plot(x,y)
# -10,8   设置x的区间
# -1,2    设置y的区间
plt.axis([-10,8,-1,2])
```

图:

![m坐标轴界限1](C:\Users\sdsd\Desktop\笔记\img\m坐标轴界限1.png)

```python
plt.plot(x,(1-x**2)**0.5,x,-(1-x**2)**0.5)
# 设置图形在中间
# 可以指定类型  按shift+tab显示类型
plt.axis('equal')
```

![m坐标轴界限2](C:\Users\sdsd\Desktop\笔记\img\m坐标轴界限2.png)

###### xlim方法和ylim方法

除了plt.axis方法，还可以通过xlim，ylim方法设置坐标轴范围

```python
x = np.linspace(-1,1,1000)
plt.plot(x,(1-x**2)**0.5,x,-(1-x**2)**0.5)
# 将画布从x = 0开始切  切到x = 2
plt.xlim(0,2)
# 将画布从y = 0开始切  切到y = 2
plt.ylim(0,2)
```

![mxy设置](C:\Users\sdsd\Desktop\笔记\img\mxy设置.png)

##### 坐标轴标签

###### x,y轴标签

```python
# 设置坐标轴属性
plt.plot(x,y)
# 对x轴进行说明
xlabel = plt.xlabel('half circle',fontsize=20)
# 对xlabel这个对象进行操作  设置边框,颜色之类的.
xlabel.set_bbox(dict(facecolor='red', alpha=0.5))
ylabel = plt.ylabel('f(x)=cos(x)',fontsize=20)
ylabel.set_bbox(dict(facecolor='red', alpha=0.3))
ylabel.set_rotation(20)
ylabel.set_position((0,1.1))
```

![坐标轴标签1](C:\Users\sdsd\Desktop\笔记\img\坐标轴标签1.png)

###### 标题

```python
# 设置标题方法
plt.plot(x,y)
title = plt.title('This is a cos function',fontsize=15,bbox=dict(facecolor='red', alpha=0.5))
# 设置背景颜色
title.set_backgroundcolor('green')
# 设置字体颜色
title.set_color('white')
```

![M标题](C:\Users\sdsd\Desktop\笔记\img\M标题.png)

#### Matplotlib相关设置

###### 图例(线名)

###### 设置图例

两种传参方法：

- 【推荐使用】在plot函数中增加label参数
- 在legend方法中传入字符串列表

```python
# 通过legend方法传参
plt.plot(x,y)
plt.plot(x,x**3)
# 参数1,名称     参数2,loc   是位置
plt.legend(['sin','x**3'],loc=1)
```

![m图例](C:\Users\sdsd\Desktop\笔记\img\m图例.png)

```python
#  通过plot后面传入label参数设置
plt.plot(x,y,label='sin')
plt.plot(x,x**3,label='x**3')
# 参数1,名称     参数2,loc   是位置
# 需要调用一下lengend函数,才能把图例显示
# loc=(0,1)  将图例名称放外面
plt.legend(loc=(0,1))
```

![m图例2](C:\Users\sdsd\Desktop\笔记\img\m图例2.png)

###### loc参数

ncol参数    设置 columns的数量

```python
# 设置位置, 设置图例列数
plt.plot(x,y,label='sin')
plt.plot(x,x**3,label='x**3')
# 参数1,名称     参数2,loc   是位置
# 需要调用一下lengend函数,才能把图例显示
# loc=(0,1)  将图例名称放外面
plt.legend(loc=(0,1),ncol=2)
```

![mloc参数](C:\Users\sdsd\Desktop\笔记\img\mloc参数.png)

##### 修改线条样式

 在plot上面设置

```python
# 设置线的类型,图例,线的颜色,线宽,落笔点类型
x1 = np.random.normal(loc=10,scale=6,size=100)*10
x2 = np.random.normal(loc=20,scale=3,size=100)*10
x3 = np.random.normal(loc=35,scale=10,size=100)*10
# marker是落笔标志
plt.plot(x1,linestyle='-.',label='line1',color='r',linewidth=2,marker='o')
plt.plot(x2,ls='--',label='line2',color='b',lw=2,marker='v')
plt.plot(x3,ls=':',label='line3',color='g',lw=3,marker='d')
plt.legend(loc=(0,1),ncol=3)
```

![样式](C:\Users\sdsd\Desktop\笔记\img\样式.png)

##### 保存图片

```python
# 获取figure对象
figure = plt.figure()
# 加图片进figure
axes = figure.add_subplot(111)
axes.plot(x1,linestyle='-.',label='line1',color='r',linewidth=2,marker='o')
axes.plot(x2,ls='--',label='line2',color='b',lw=2,marker='v')
axes.plot(x3,ls=':',label='line3',color='g',lw=3,marker='d')
axes.legend(loc=(0,1),ncol=3)
# dpi是分辨率
figure.savefig('./data/save1.png',dpi=500,facecolor='green')
```

输出结果.....

保存图片save1

##### 设置plot的风格和样式

###### 点和线的样式

![plot样式1](C:\Users\sdsd\Desktop\笔记\img\plot样式1.png)

###### 透明度[¶](http://localhost:8888/notebooks/1%20Data%20analysis/Matplotlib/matplotlib-1.ipynb#%E9%80%8F%E6%98%8E%E5%BA%A6)

alpha参数

```python
# 透明度
plt.plot(x,y,alpha=0.3)
```

###### 背景色

设置背景色，通过plt.subplot()方法传入facecolor参数，来设置坐标轴的背景色

```python
# 透明度
plt.subplot(111,facecolor='c')
plt.plot(x,y,c='#000000')
```

###### 线型

参数linestyle或ls

![线型](C:\Users\sdsd\Desktop\笔记\img\线型.png)

画阶梯线

```python
x = np.linspace(-1,1,150)
y = (1-x**2)**0.5
# 用阶梯线来画
plt.plot(x,y,ls='steps')
```

![阶梯线样式](C:\Users\sdsd\Desktop\笔记\img\阶梯线样式.png)

###### 线宽

linewidth或lw参数

```python
# 线宽
plt.plot(x,y,lw='10')
```

![线宽](C:\Users\sdsd\Desktop\笔记\img\线宽.png)

###### 自定义线

dashes参数
设置破折号序列各段的宽度

```python
x = np.linspace(-1,1,1000)
y = np.sin(x)
# dashes设置点的个性
# 5个点,10个空格,1个点,2个空格
plt.plot(x,y,dashes=[5,10,1,2],c='r')
```

![自定义线](C:\Users\sdsd\Desktop\笔记\img\自定义线.png)

###### 点型

marker参数

![点型1_副本](C:\Users\sdsd\Desktop\笔记\img\点型1_副本.png)

向下三角架

```python
x = np.linspace(-1,1,15)
y = (1-x**2)**0.5
plt.figure(figsize=(12,12))
plt.plot(x,y,marker='1')
```

![点型2](C:\Users\sdsd\Desktop\笔记\img\点型2.png)

星号

```python
x = np.linspace(-np.pi,np.pi,10)
y = np.sin(x)
plt.figure(figsize=(12,9))
# markersize  设置点型大小
plt.plot(x,y,marker='*',markersize=30)
```

图:

![点型5](C:\Users\sdsd\Desktop\笔记\img\点型5.png)

###### 多参数连用和更点线的设置

颜色、点型、线型

![更多点线的设置](C:\Users\sdsd\Desktop\笔记\img\更多点线的设置.png)

```python
x = np.linspace(-np.pi,np.pi,10)
y = np.sin(x)
plt.figure(figsize=(12,9))
plt.plot(x,y,marker='d',markersize=30,c='r',ls='--',markeredgecolor='g',markeredgewidth=5)
```

![更多点线设置2](C:\Users\sdsd\Desktop\笔记\img\更多点线设置2.png)

##### 在一条语句中为多个曲线进行设置样式

多个曲线同一设置

属性名声明

plt.plot(x1, y1, x2, y2, fmt, ...)

```python
x = np.linspace(-np.pi,np.pi,10)
# 为三条曲线一起设置样式
plt.plot(x,x**2,x,np.sin(x),x,np.cos(x),ls='--',marker='d')
```

![同时设置样式1](C:\Users\sdsd\Desktop\笔记\img\同时设置样式1.png)

多个曲线不同设置

```python
plt.figure(figsize=(12,9))
x = np.linspace(-np.pi,np.pi,10)
# 多个曲线设置
plt.plot(x,x**2,'r','o','--',x,np.sin(x),'g','d','-',x,np.cos(x),ls='--',marker='d')
```

![同时设置3](C:\Users\sdsd\Desktop\笔记\img\同时设置3.png)

###### 三种设置方式

1.关键字参数

```python
x = np.linspace(-np.pi,np.pi,10)
# 关键字参数
plt.plot(x,x**2,x,np.sin(x),x,np.cos(x),ls='--',marker='d')
```

2.对实例使用一系列的setter方法

```python
x = np.linspace(-np.pi,np.pi,10)
line, = plt.plot(x,x**2)
# 设置绿色
line.set_color('g')
```

3.使用setp()方法

```python
# set propeties  设置属性
line, = plt.plot(x,y)
plt.setp(line,ls='--')
```

##### X、Y轴坐标刻度

###### xticks()和yticks()方法

```python
line, = plt.plot(x,y)
# 自定义x轴刻度
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           ['-pi','-pi/2','0','pi/2','pi'])
plt.yticks([-1,0,1],
           ['min',0,'max'])
```

![x,y刻度1](C:\Users\sdsd\Desktop\笔记\img\x,y刻度1.png)

###### 面向对象方法

```python
# 创建对象
figure = plt.figure()
# 创建画布
axes = figure.add_subplot(111)
axes.plot(x,y)
#设置刻度属性
axes.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           )
# 设置label
axes.set_xticklabels(['-pi','-pi/2','0','pi/2','pi'],
                    fontsize=20,rotation=30)
```

![mxy设置](C:\Users\sdsd\Desktop\笔记\img\mxy设置2.png)

###### 希腊字母

```python
# LaTex语法，用 ππ 等表达式在图表上写上希腊字母
# 创建对象
figure = plt.figure()
# 创建画布
axes = figure.add_subplot(111)
axes.plot(x,y)
#设置刻度属性
axes.set_xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           )
# 设置label
# 拉丁字母显示
axes.set_xticklabels(['-$\pi$','-$\pi$/2','0','$\pi$/2','$\pi$'],
                    fontsize=20,rotation=30)
```

![mxy设置3](C:\Users\sdsd\Desktop\笔记\img\mxy设置3.png)

##### 图形内文字

1.使用text()

2.使用figtext()

```python
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x,y)
# 添加图形内文字
# 0.3,0表示位置
plt.text(0.3,0, 'sin(0)=0')
plt.text(np.pi,0, 'sin(π)=0')
# figtext 的位置,与text()的不一样.注意哦!!!
plt.figtext(0.65,0.15,'sin(3π/2)=-1')
```

![图形内文字](C:\Users\sdsd\Desktop\笔记\img\图形内文字.png)

##### 注释

annotate()  
xy参数设置箭头指示的位置，xytext参数设置注释文字的位置  
arrowprops参数以字典的形式设置箭头的样式  
width参数设置箭头长方形部分的宽度，headlength参数设置箭头尖端的长度，  
headwidth参数设置箭头尖端底部的宽度，  
facecolor设置箭头颜色  
shrink参数设置箭头顶点、尾部与指示点、注释文字的距离（比例值） 

```python
x = np.array([14,11,13,12,13,10,30,12,11,13,12,12,11,12])
plt.plot(x)
# 把y轴拉长
plt.ylim(ymax=40)
'''
 ==========   ======================================================
    Key          Description
    ==========   ======================================================
    width        the width of the arrow in points
    headwidth    the width of the base of the arrow head in points
    headlength   the length of the arrow head in points
    shrink       fraction of total length to 'shrink' from both ends
    ?            any key to :class:`matplotlib.patches.FancyArrowPatch`
    ==========   ======================================================
'''
# 注解
# 参数1  要描述的字符串  参数2,箭头位置 参数3  文字位置
plt.annotate('This spot must really mean something',(6,30),(8,33),        arrowprops=dict(width=10,headwidth=15,headlength=10,shrink=0.2,facecolor='black'))
```

![注释](C:\Users\sdsd\Desktop\笔记\img\注释.png)

#### 2D图形

饼图:![m饼图](C:\Users\sdsd\Desktop\笔记\img\m饼图.png)

```python
# 饼图
# 加起来,看每部分占多少
n = [3,4,5]
# n = [0.3,0.4,0.2]
# 标准圆
plt.figure(figsize=(8,8))  
# labels  设置名字  labeldistance  设置位置   explode  让饼分割开来
# autopct  把比例显示出来  startangle 旋转角度
plt.pie(n,labels=['red','green','blue'],
        labeldistance=1.2,
        explode=[0.2,0,0],
       colors=['red','green','blue'],
       autopct='%0.2f%%',
       startangle=60,
       shadow='optional')
```





#### 3D图形![3D图形](C:\Users\sdsd\Desktop\笔记\img\3D图形.png)

```python
# 导包
from mpl_toolkits.mplot3d.axes3d import Axes3D

x1 = [1,2,3,4]
y1 = [1,2,3,4,5]
# 使用,x,y生成一个面
X1,Y1 = np.meshgrid(x1,y1)
display(X1,Y1)

# 生成数据

x = np.linspace(0,2*np.pi,100)
y = np.linspace(0,2*np.pi,100)

# 使用,x,y生成一个面
X,Y = np.meshgrid(x,y)
# plt.plot(X,Y)
# 生成z轴
Z = X*0.7 + Y*0.66 +np.sin(X) + np.cos(Y)
plt.figure(figsize=(12,9))
# 生成3D的坐标轴  设置projection可以画Z轴
axes1 = plt.subplot(121,projection='3d')
# 把Z在3D坐标轴中画出来.
axes1.plot_surface(X,Y,Z,cmap='summer')

Z = np.sin(X) + np.cos(Y)
# 生成3D的坐标轴  设置projection可以画Z轴
axes2 = plt.subplot(122,projection='3d')
# 把Z在3D坐标轴中画出来.
p = axes2.plot_surface(X,Y,Z,cmap='rainbow')
plt.colorbar(p,shrink = 0.5)
```

#### 玫瑰图/极坐标条形图

通用函数

```python
def show_rose(values,title):
    # 玫瑰图花瓣的个数 8,每一瓣45度
    n = 8
    # 设置角度  总共360度   每一瓣360/8度
    angle = np.arange(0,2*np.pi,2*np.pi/n)
    
    # 绘制的数据values   每个数据以半径来显示
    radius = np.array(values)
    # axis  代表x轴,y轴
    # axes   代表的是整个画面,画布
    # polar  == True 是否使用极坐标
    plt.axes([0,0,2,2],polar = True)
    
    # 设置颜色
    color = np.random.random(size = 24).reshape((8,3))
    
    plt.bar(angle, radius, color = color)
    plt.title(title,loc = 'left')
```



使用np.histogram计算一组数据的直方图

```python
# wind数据  
# 4  分成几份
# 怎么分,从1,4进行等分
#返回第一个array是数据数量,统计的数据
# 第二个array是分割标准(距离)
degree, ranges = np.histogram(wind,bins=8,range=[0,360])
show_rose(degree,'wind')
```

![下载](C:\Users\sdsd\Desktop\笔记\img\下载.png)