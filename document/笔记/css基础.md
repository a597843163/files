# html(day1)

## frameset框架集

1,不能有body

2,<frameset rows(行分级)/cols(列分级) 20%,* />

​	<frame src ="url"  /> 

​	<frame src = "url"  />

## css

1.查询（http://www.w3school.com.cn/）

2.格式 ：选择器{属性值1=属性;属性值2=属性}

### 选择器	

#### 1.全局选择器*{}

#### 2.属性选择器

​	id选择器  #id名{}

​	类别选择器	.class名{}

​	其他属性选择器   选择器[属性名,如name]{}

#### 3.标签选择器

​	标签元素的名字{}

#### 4.包含选择器

​	父标签>子标签（一级）{}

​	父标签   子标签 (所有级){}

#### 5.组合选择器

​	标签选择器1，标签选择器2{}

#### 6.伪类选择器(大部分a标签使用)

​	选择器:link{}       	未被浏览的状态

​	选择器:visited{} 	 浏览过的状态

​	选择器:hover{}       鼠标悬浮状态

​	选择器:active{}       点击的状态

针对块级标签有以下

​	<u>选择器:first-letter{}       第一个字符样式</u>

​	<u>选择器:first-line{}		  第一行样式</u>   

​	<u>选择器:first-before{}   	  添加头部</u>

​	<u>选择器:first-after{}   	  添加尾部</u>

#### 7.结构选择器

​	页面根节点选择器[<html标签>]

​	:root{}

​	空节点[只有标签，没有内容<title>]

​	:empty

​	否定选择器[除了这个标签以外]

​	:not(选择器)

查找被包含标签中的第几个子标签

​	：first-child{}   第一个

​	:   last-child{}    最后一个

child后面加（odd）奇数行

child后面加（even）偶数行

​	:   nth-child{}  从上往下数  

​	:   nth-last-child{}   从下往上数（倒数）



### 背景样式的设计

#### 	背景颜色

​	background-color

​		1.rgb()  (0-255)

​		2.十六进制

​		3.英文名

​		4.hsl()  (0-360,)饱和度(0%-100%)亮度(0,100%)

#### 	背景图

​	background-image:url   插入图

​	background-repeat:      铺放方式

​		no-repeat 不进行平铺

​		repeat-x 水平方向平铺

​		repeat-y 垂直方向平铺

​	background-position:    摆放位置

​		第一个值表示水平方向

​	 值：left   center  right  自定义数据

​		第二个值表示垂直方向

​	值：top    ceter    bottom  自定义数据

#### 	 渐变色

​	中心扩散  默认形状为椭圆

  backgroud:radial-gradient(circle,red,yellow,pink)

​	方向性扩散   默认自上而下

  backgroud:linear-gradient(red,green,blue)  上到下变		

   ...........................	    ...        ..（to right,...）  左到右	

...........................	    ...        ..（to bottom right,...）  往右下

​	利用角度定位方向	

  background: linear-gradient(90deg, red, yellow)  左到右

### 	字体样式设计

设置字体：font-family:字体  可写多个，支持哪个用哪个

设置文字颜色:color:  颜色

设置字号: font-size:  20px（大小）         

​						em(当前字体倍数)	

​						pt(网页的单位)  9pt=12px

设置字体粗细: font-weight:

字体风格,斜度: font-style:



首行缩进2个字符:text-indent:2em

标签内容对齐方式:text-align:

文本划线修饰:        text-decoration

line-through删除线	underline下划线	none取消划线

​	文本阴影：		text-shadow :后接四个值

​	1.水平层次感 2.垂直 3.羽化度 4.阴影颜色

​	如:text-shadow:5px  5px  5px   red；

内容的行高:  		line-height:    如果等于标签高，则垂直居中

标签内容溢出处理: overflow:  

​	1.hidden  隐藏	2.scroll,滚动查看溢出  3.visible可见的

字符间的间隙:    letter-spacing:  10px;

单词间间隙    :   word-spacing:10px;





#### 列表的样式设计

设置项目符号样式:  list-style-type:none()去除

设置项目符号为图片：list-style-image:url  

设置项目符号的位置:list-style-position:



### 盒子模型

#### 标准盒子

![盒子模型的内容](F:\python千峰课件\Web前端\WebDay02\盒子模型的内容.png)

height:30px  内容高

margin:30px  外边距

padding：10px  内边距

border : 3px  blue 边框颜色及宽度  (double为双线)

box-shadow:3px 3px 3px green，  标签阴影

border-radius:8px		切圆角

#### 怪异盒子

​	当不想高度/宽度发生变化 还是原来设定的高度

​	box-sizing:border-box



### css布局方式

#### display

​	标签显示模式

​	inline行内标签 不换行，宽高无效

​	block块级标签，换行，宽高有效

​	inline-block行内块级标签，不换行，宽高有效



#### 隐藏方式

display:none  位置不保存，标签隐藏

visibility:hidden 位置保存，标签隐藏	

#### 定位布局

float ： 浮动定位

​	left  向左浮动

​	right 向右浮动

clear:both  清楚浮动

​	left       清除左浮动标签

​	  right	清除右浮动标签

position  定位

四个值：

1.static  默认定位值

2.relative  把此标签设为参照物

3.absolute  参照物为relative的位置

4.fixed  参照物为窗口

设置位置：

top[与参照物顶部的距离]

bottom[底部距离]

left[左部距离]

right[右部距离]



### 形变和过渡

形变 transform:

1.scale()  形变  如(0.5,1.5)  (1.2)

2.rotate()  旋转   如(45deg)

设置旋转点:  transform-origin: center top;

过渡  transition:  3个参数

1.标签或者all   2.时间   3.次数或者infinte

### 动画

1.@keyframes 动画名字{

​		from()  默认状态时无需设置

​		to()

}

2.@keyframes 动画名字{

​	0%()

​	30%()

​	90%()

​	100%()

}

启用动画:

animation:动画名字  时间  次数  动画样式

​	如:circle  5s 2 linear