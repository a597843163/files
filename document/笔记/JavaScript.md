# JavaScript

## ECMAScript

​	包含的是js的语法

#### 1.引入方法

1.内部

在head或者body中添加<script>JS的内容</script>

2.外部

在head或者body中添加<script src=“JS的url”></script>

变量定义，与python一样

声明变量时用VAR先声明

#### 2.数据类型

Undefined   定义变量只声明未赋值产生   派生自Null

Null 		空对象，特殊的对象值

Boolean   	true (1) /false(0)

​			Boolean(变量)可转化为Boolean类型

​				str  空为false  非空为true

​				Number非0为true

​				Object非null为true

​				undefined为false

Number			数值类型

NaN			非数值类型

String			字符串类型	

​	提取子串    str.substr(start,end);  substr(2,5)

​			  str.substring(strat，end) 同上

​			 str.slice(start,end)  同上

​	查找     		str.indexof("a") 返回某个子串第一次出现的位置

​	大写		str.toUpperCase()

​	小写		str.toLowerCase()

​	切割	strs = str.split("a")   得到是数组(list)

​	替换	 str.replace("a","A")

arry   			数组类型

在后面添加元素     array.push("hello",100,108);   

在头部添加		array.unshift("我","是","头")；

直接以角标添加	array[10] = "byebye"  中t间没有的元素为空

删除尾部  		array.pop();

删除头部			array.shift();

删除指定位置		array.splice(指定位置，删除个数);

删除后替换		array.splice(指定位置，删除个数,替换元素)

​				如array.splice(1,1,"new")

不删除替换		array.splice(1,0,"five")



提取子数组		array.slice(start,end)

拼接成字符串		array.join("指定字符串")

排序		comapre(){if(arguments[0]>arguments[1])}

array.sort(comapre)



#### 3.运算符

算术运算符	+  -  *  /  %

​		a++,先取a的值，再自加1

​		++a，先自加，再取a值

关系运算符	>	<  >=  <=  ==  !=

​			关系运算之后的结果是boolean类型的

逻辑运算符	&&(and)		||(or)	!(not)

赋值运算符	=   +=   -=  *=  /=

三元运算符	条件表达式 ?  表达式1  : 表达式2	

位运算符		&,	|,	^,	~,	>>,		<<,		>>>,

#### 4.流程控制语句

顺序结构：从上自下

分支结构语句1：if-----判断结构

​			if(条件表达式){执行语句}else{执行语句2}

分支结构语句2：switch-----判断结构(选择题，表达式和值是固定的)

​			switch(表达式){

​		case 值  : 执行操作;break ....default:执行的操作break;

}

循环语句结构:

while循环		跟python一样，但是没有while-else

while(条件表达式){执行语句}  		

do-while循环		跟while比至少循环一次

do{执行语句}while(条件表达式);

for循环		格式不一样

for (var i =1; i < 11; i++ ){执行语句}

break	---退出循环结构

continue	---结束当次，继续下一次

#### 5.函数

function  函数名(变量1，变量2....){

​	return

}

#### 6.object对象

创建对象	var  obj = new Object();

添加特征属性	obj.name="小牧"

添加行为		obj.study =function()}{}

一次性多添加

​	obj = {

name:"小牧",

age:18,

run:function(){}}

删除字段  delete   obj.name;

#### 7.date

时间	Webday05

#### 8.Math

随机数   Math.random()	随机数[0,1)

四舍五入	Math.round(3.6)

最大最小	max		min

向上向下	ceil			floor

次方	.pow(2,5)

开方	.sqrt(9)

绝对值	abs(-10)

## BOM

Browser Object Model	浏览器对象模型

window对象下常用的一下方法

			1.弹框的几种使用方式
				alert
			2.带有确认键 的弹框
				confirm
			3. 带有输入框的弹框
				prompt
		
			4.在当前页面中操作打开一个新的窗口
				open("新窗口中显示的网页地址", "指定打开目标", "新建窗口的设置")
			
			5. 延时器
				setTimeOut(code, millis)
				
				code一般设置的是函数
			6. 定时器
				setInterval(code, millis)
				code一般设置的是函数
			7.location
				提供了与当前窗口加载的文档的相关信息
					比较常用的有一个字段 href ---> 获取当前页面的网址
						---> 在当前窗口加载新的文档信息
			8.history
				保存了用户上网的记录 从网页窗口打开的那一刻保存的
				length 记录了由该窗口进入的浏览了多少网页
## DOM

文档对象模型		Document Object Model

			----> Document Object Model
				文档对象模型
				可以访问HTML页面 并对页面和样式进行操作
				
				D --- 文档
					整个WEB加载的网页文档
				O ---- 对象
					documnet ---> 来操作网页的对象
				M ---- 模型
					网页文档的树结构模型
			
			在树结构模型中 是由节点组成的
				元素节点 ---> div
				属性节点 ----> id
				文本节点 -----> div测试文本
			
				<div id="d">div测试文本</div>
			在树结构模型中 是由根节点和子节点之分的
				根基点就是只有子节点没有父节点